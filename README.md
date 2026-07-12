# Simple Banking System (Python OOP)

A simple command-line banking system built in Python using Object-Oriented Programming (OOP) concepts. This project demonstrates classes, objects, encapsulation, and interaction between objects through a basic banking simulation.

## Features

- Create a new bank account
- Deposit money
- Withdraw money
- Check account balance
- Change account PIN
- View transaction history
- Delete an account

## Tech Stack

- Python 3

## OOP Concepts Used

- **Classes & Objects** – `Account` and `Bank` classes model real-world entities
- **Encapsulation** – Account details (balance, PIN, transactions) are managed within the `Account` class
- **Abstraction** – Users interact with simple methods like `deposit()` and `withdraw()` without worrying about internal logic
- **Object Interaction** – The `Bank` class manages and authenticates multiple `Account` objects

## Project Structure

```
banking-system/
│
├── banking_system.py   # Main source code
└── README.md            # Project documentation
```

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/banking-system.git
   cd banking-system
   ```

2. Run the script
   ```bash
   python banking_system.py
   ```

## Usage

On running the program, you'll see a menu:

```
===== Simple Banking System =====
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Change PIN
6. Show Transactions
7. Delete Account
8. Exit
```

Enter the corresponding number to perform an action. Each account is protected by a PIN, which is required for authentication before performing any sensitive operation.

## Future Improvements

- Persistent storage using a database or file (JSON/SQLite)
- Interest calculation for savings accounts
- Multiple account types (Savings, Current)
- GUI or web-based interface

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Feel free to connect or contribute to this project!
