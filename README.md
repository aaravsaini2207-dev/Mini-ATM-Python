# 🏦 Mini ATM System - Python

A secure ATM simulation system with PIN verification, OTP authentication, and transaction history tracking.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-complete-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## ✨ Features
- 🔐 **Secure Authentication**: PIN + OTP verification
- 💳 **Account Masking**: Shows only last 4 digits for security
- 🔒 **Account Locking**: Locks after 3 incorrect PIN attempts
- 📊 **Transaction History**: Tracks all debit/credit operations
- 🔄 **PIN Management**: Secure PIN change with OTP verification
- 💰 **Balance Operations**: Check, debit, and credit functions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation

```bash
git clone https://github.com/yourusername/mini-atm.git
cd mini-atm

DEMO:
Enter 10-digit account number: 1234567890
Enter current balance: $5000
Set 4-digit PIN: 1234

---------------ATM MENU-------------
1.Check balance
2.Debit Amount  
3.Credit Amount
4.Transaction History
5.Change PIN
6.Exit

Choose Option: 1
Enter PIN: 1234
Current balance: $5000

Project Structure
Mini-ATM-Python/
├── Mini_ATM.py          # Main Python program
├── README.md            # This documentation
└── .gitattributes       # Git configuration

Code Example
# The account class handles all banking operations
class account:
    def __init__(self, accNo, balance, pin):
        self.balance = balance
        self.accNo = accNo
        self.pin = pin
        self.history = []
        self.pin_attempts = 0
        self.locked = False
    
    def verifyPin(self):
        # Secure PIN verification with lockout
        pass
    
    def debit(self, amount):
        # Secure debit operation
        pass

🛠️ Technologies Used
Python 3 - Core programming language

OOP - Object-Oriented Programming

Random Module - For OTP generation

 Future Enhancements
GUI interface using Tkinter

Database integration

Email/SMS OTP

Web interface with Flask

🤝 Contributing
Feel free to fork and submit pull requests!

📄 License
MIT License

👨‍💻 Author
Aarav Saini

GitHub: @aaravsaini2207-dev

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/581b4872-402b-4c98-b8d8-0a0a3c4c2e53" />

