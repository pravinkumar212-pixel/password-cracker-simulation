# Python Brute-Force Password Cracker Simulation

A lightweight Python script that simulates a dictionary-based brute-force attack against a targeted password. This project demonstrates how automation can be leveraged by attackers to exploit weak credentials, highlighting the necessity of robust password policies and account lockout mechanisms.

## Features
- **Dictionary Attack Logic:** Iterates through a specified list of common passwords (`passwords.txt`).
- **Target Comparison:** Automatically detects when a password match is found and halts execution.
- **Terminal Visualization:** Provides clear console logging (`[~] Trying...`, `[+] SUCCESS!`) to simulate real-time attack tools.

## Installation & Usage
1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Open a terminal/PowerShell window inside the project directory.
4. Run the script:
   ```bash
   python cracker.py
