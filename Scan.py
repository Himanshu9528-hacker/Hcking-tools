#!/usr/bin/env python3
"""
nmap-automator: Simple, safe wrapper around nmap for authorized/learning use.

Usage examples:
  python3 scan.py --target example.com --type quick
  python3 scan.py --target 192.168.1.0/24 --type top-ports --ports 1-1000
  python3 scan.py --target example.com --type custom --flags "-sS -p 22,80,443"
"""

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ---------- Config ----------
OUT_DIR = Path("scans")
ALLOWED_SCAN_TYPES = {"quick", "full", "top-ports", "custom", "os-service"}
# ----------------------------

def check_nmap():
    if shutil.which("nmap") is None:
        print("[!] nmap not found. Install nmap first (e.g., apt install nmap).")
        sys.exit(1)

def build_nmap_command(args):
    cmd = ["nmap"]

    if args.type == "quick":
        # quick TCP SYN default top ports
        cmd += ["-T4", "-sS", "--top-ports", "1000", "--open"]
    elif args.type == "full":
        # full TCP scan, service/version detection, scripts
        cmd += ["-T4", "-sS", "-sV", "-A", "-p", "1-65535"]
    elif args.type == "top-ports":
        ports = args.ports or "1-1000"
        cmd += ["-T4", "-sS", "-p", ports, "--open"]
    elif args.type == "os-service":
        # OS detection + service/version
        cmd += ["-O", "-sV", "--script=banner", "--open"]
    elif args.type == "custom":
        if not args.flags:
            print("[!] custom type requires --flags.")
            sys.exit(1)
        # split flags by space but keep as separate list items
        cmd += args.flags.strip().split()
    else:
        raise ValueError("Unsupported scan type")

    # target
    cmd.append(args.target)

    # output to XML and normal
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    base = OUT_DIR / f"{args.target.replace('/', '_')}_{args.type}_{ts}"
    cmd_xml = cmd + ["-oX", str(base) + ".xml"]
    cmd_std = cmd + ["-oN", str(base) + ".txt"]
    return cmd_xml, cmd_std, base

def confirm_permission():
    print("⚠️  IMPORTANT: Only use this tool on systems you own or have explicit permission to test.")
    confirm = input("Type 'I HAVE PERMISSION' to continue: ").strip()
    if confirm != "I HAVE PERMISSION":
        print("Permission not confirmed. Exiting.")
        sys.exit(1)

def run_cmd(cmd):
    print("Running:", " ".join(cmd))
    try:
        completed = subprocess.run(cmd, check=True)
        return completed.returncode == 0
    except subprocess.CalledProcessError as e:
        print("[!] nmap exited with error:", e)
        return False

def main():
    parser = argparse.ArgumentParser(description="nmap-automator — small wrapper for authorized nmap scans")
    parser.add_argument("--target", "-t", required=True, help="Target host or network (e.g., example.com or 192.168.1.0/24)")
    parser.add_argument("--type", "-T", default="quick", choices=sorted(ALLOWED_SCAN_TYPES),
                        help="Scan type: quick, full, top-ports, os-service, custom")
    parser.add_argument("--ports", "-p", help="Port range for top-ports type or custom (e.g., 1-1000)")
    parser.add_argument("--flags", "-f", help="Raw nmap flags for custom type (wrap in quotes)")
    parser.add_argument("--no-confirm", action="store_true", help="Skip the permission confirmation (use with care)")
    args = parser.parse_args()

    check_nmap()
    if not args.no_confirm:
        confirm_permission()

    cmd_xml, cmd_std, base = build_nmap_command(args)

    print(f"[i] Results will be saved to: {base}.txt and {base}.xml")
    ok1 = run_cmd(cmd_xml)
    ok2 = run_cmd(cmd_std)
    if ok1 or ok2:
        print(f"[✓] Scan finished. Files saved under {OUT_DIR.resolve()}")
    else:
        print("[!] Scan did not complete successfully.")

if __name__ == "__main__":
    main()
