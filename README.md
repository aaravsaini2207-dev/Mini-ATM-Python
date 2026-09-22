# Mini ATM System — Python

**Console-based ATM simulation built with Python and object-oriented programming, covering authentication, account operations, PIN management, and transaction history.**

> This is an early Python/OOP project focused on practicing classes, state management, validation, and control flow.

## Features

- **PIN verification** with a 3-attempt lockout
- **OTP verification** for secure access and PIN changes
- **Account masking** showing only the final four digits
- **Balance operations** for debit, credit, and balance checks
- **Transaction history** stored during the program session
- **PIN management** with confirmation and validation
- **Account validation** for 10-digit account numbers

## Technical concepts

**Python · OOP · Classes & Objects · Encapsulation · Conditional Logic · Loops · Lists · Input Validation · Random Module**

The project is implemented primarily through an `account` class that maintains account state such as balance, PIN, lock status, PIN attempts, and transaction history.

## Program flow

```text
Create Account
     ↓
Validate Account Number
     ↓
ATM Menu
 ┌───┼───────────────┐
 ↓   ↓   ↓   ↓   ↓   ↓
Balance Debit Credit History PIN  Exit
       ↓
   PIN Verification
       ↓
  Update Account State
```

## Run locally

Requirements:
- Python 3.8+

```bash
git clone https://github.com/aaravsaini2207-dev/Mini-ATM-Python.git
cd Mini-ATM-Python
python Mini_ATM.py
```

The application runs entirely in the terminal and does not require external packages.

## Project structure

```text
Mini-ATM-Python/
├── Mini_ATM.py
├── README.md
└── .gitattributes
```

## Scope and limitations

This is a **learning/demo application**, not a production banking system. Data is held in memory for the current session, and the OTP is printed to the console rather than delivered through an external authentication service.

Potential extensions include database persistence, a GUI, external OTP delivery, stronger input validation, and automated tests.

## Author

**Aarav Saini — @aaravsaini2207-dev**
