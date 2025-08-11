# nmap-automator

A small, **ethical** wrapper around `nmap` to run commonly used scans and save outputs.  
**Use only on systems you own or have explicit permission to test.**

## Features
- Quick scan, full scan, top-ports scan, OS/service detection, custom flags
- Saves results as `.txt` and `.xml` under `/scans` with timestamp
- Simple permission confirmation to avoid accidental misuse

## Requirements
- Python 3.6+
- `nmap` installed on system (`sudo apt install nmap`)

## Usage
```bash
# quick scan
python3 scan.py --target example.com --type quick

# top ports 1-500
python3 scan.py -t 192.168.1.0/24 --type top-ports --ports 1-500

# custom
python3 scan.py --target example.com --type custom --flags "-sS -p22,80,443"

# skip confirmation (careful)
python3 scan.py --target example.com --type quick --no-confirm
