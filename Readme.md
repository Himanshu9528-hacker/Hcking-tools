# Nmap Scanning Tool 🔍

A simple Python-based Nmap automation tool for network scanning and basic vulnerability detection.  
**This tool is made for educational and ethical purposes only.**

---

## 🚀 Features
- Fast Nmap scanning
- Detect open ports
- Identify services and versions
- Basic vulnerability scanning
- Simple & easy to use

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/Himanshu9528-hacker/Nmap-Scanning-Tool.git
cd Nmap-Scanning-tool

Install required dependencies:
pip install -r requirements.txt

🛠 Usage
Run the tool:

python main_tool.py
Example:
python main_tool.py 192.168.1.1


📋 Example Output
plaintext
Copy
Edit
Starting Nmap Scan...
Host: 192.168.1.1
Open Ports:
  22/tcp  open  ssh
  80/tcp  open  http
Service Info: Apache httpd 2.4.41 ((Ubuntu))
Vulnerabilities:
  - Possible outdated Apache version


⚠️ Disclaimer
This project is for educational purposes only.
The author is not responsible for any misuse of this tool.
Use only on networks you own or have permission to test.

--------------HOW TO USE SCAN.PY--------------
([-t mean -target]"hmme kis per target krna chahte hai agr aapke pass ip addres hai to ip address de jaise ki niche de rakha hai agr aapko ip address nhi pta hai to ip addess ki jagah naam dalde site ka jaise ki  - google.com , microsoft.com etc")

1.Quick Scan
python3 Scan.py -t 192.168.126.2 --type quick

2.Full Scan
python3 Scan.py -t 192.168.126.2 --type full

3.OS & Service Detection Scan
python3 Scan.py -t 192.168.126.2 --type os-service

3.Top Ports Scan
python3 Scan.py -t 192.168.126.2 --type top-ports

4.Custom Ports Scan
python3 Scan.py -t 192.168.126.2 --type custom --ports 21,22,80,443

5.Custom Flags Scan
python3 Scan.py -t 192.168.126.2 --flags "-A -O"

5.Without Confirmation
python3 Scan.py -t 192.168.126.2 --type full --no-confirm
⚡ Tip:
192.168.126.2 ko apne target IP ya domain se replace karo.
Agar tumko Scan.py --help likhoge, to tumhe saare available options ka list mil jayega:

python3 Scan.py --help
