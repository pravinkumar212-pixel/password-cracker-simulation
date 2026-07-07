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
   
## Defensive Takeaway
This simulation demonstrates why simple, predictable words (like secret123 or admin) are highly vulnerable to automated guessing. In a real-world enterprise environment, these attacks should be mitigated by implementing:

1. Multi-Factor Authentication (MFA)
2. Account Lockout Policies (e.g., locking an account after 5 failed attempts)
3. Rate Limiting to prevent rapid, automated requests.
