# Hotel Management System

## Information:
### Brief Description:
A Hotel Management System with the MVP being: Rooms, (Add, Edit, Reservation History, etc.) Customers, (Add, Edit, etc.) Services, (Add, edit, etc.) and full control over Reservation (Extending stay, canceling, etc.) and simple statistical overview of the hotel

### Technologies Used:

- Python 3.7
- PyQt5: For the GUI and database connection management throught QtSql submodule
- SQLite3: As the database
- FBS: For deploying and packaging of the project

### Aim:
I aim to build a reliable Hotel Management system with data accessibility and user-friendliness as the main focus, achieving that with charts and minimal interface.

## Getting Started

### Debugging:
`cd` into the repository and `fbs run`
*Note: `fbs run` doesn't work because of importing QtChart, please use `py main.py` instead*

### Deploying:
`cd` into the repository and `fbs freeze` which will generate a `target` file. Open that file and go into the `HotelManagementSystem` file and run `HotelManagementSystem.exe`
