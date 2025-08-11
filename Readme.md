#!/usr/bin/env python3
import os
import sys
import subprocess

def check_nmap():
    """Check if Nmap is installed"""
    try:
        subprocess.run(["nmap", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def run_scan(target):
    """Run Nmap scan on target"""
    print(f"[+] Scanning target: {target}")
    command = ["nmap", "-sV", target]  # -sV for service/version detection
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 nmap_tool.py <target>")
        sys.exit(1)

    if not check_nmap():
        print("[-] Nmap is not installed. Please install it using:")
        print("    sudo apt install nmap")
        sys.exit(1)

    target = sys.argv[1]
    run_scan(target)

if __name__ == "__main__":
    main()
