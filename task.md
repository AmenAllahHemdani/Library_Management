# Library Management System

## Objective
The goal is to create a Library Management System using Python that provides functionalities for managing books and library members, including borrowing and returning books. This task is intended to help beginners practice using Python's Object-Oriented Programming (OOP) concepts, list comprehensions, error handling, and creating a simple command-line interface (CLI).

## Features to Implement

### 1. Book Management
- **Add a New Book**: The system should allow users to add a new book by providing its title and author.
- **Remove a Book**: Users can remove a book by providing its title. The book will be deleted from the library's collection.
- **Search for Books**: Users can search for books by entering a search term (title). The system will display all books that contain the search term in their title.

### 2. Member Management
- **Add a New Member**: Users can add a new library member by providing the member's name.
- **Borrowed Books Tracking**: Each member can borrow books, and the system will keep track of borrowed books and their return dates in a dictionary format, where the key is the book title and the value is the return date.

### 3. Borrowing and Returning Books
- **Check Out Books**: Members can check out books by specifying their name, the book title, and the return date.
- **Return Books**: Members can return borrowed books by specifying their name and the book title. The system will remove the book from the member's borrowed books.

### 4. User Interface
Implement a simple command-line interface (CLI) that provides options to add, remove, search, check out, return books, and exit the system.

## Key Python Concepts to Use
- **Classes and Objects**: Use Python classes to model the system:
  - `Book` class to represent a book.
  - `Member` class to represent a library member and track borrowed books.
  - `Library` class to manage books and members.
- **List Comprehensions**: Replace traditional for loops with list comprehensions where possible for more concise and Pythonic code.
- **Generators**: Use generator expressions when appropriate to optimize memory usage, especially for large datasets or searches.
- **Error Handling**: Add error handling to provide feedback for invalid actions, such as trying to borrow a book that does not exist or returning a book that wasn't borrowed.

## Suggested Code Enhancements
- **Add Docstrings**: Provide clear docstrings for all classes, methods, and functions to improve code readability and maintainability.
- **Type Hints**: Use Python type hints for function parameters and return types to make the code easier to understand and maintain.
- **Code Cleanup and Optimization**: Ensure code is clean, well-organized, and optimized for performance. Use list comprehensions where applicable.

## Explanation of Borrowed Books Tracking
### Borrowed Books Dictionary
In the `Member` class, there is a dictionary called `borrowed_books` that keeps track of the books each member has borrowed. The dictionary's structure is as follows:

```python
borrowed_books = {
    "Book Title 1": "YYYY-MM-DD",
    "Book Title 2": "YYYY-MM-DD",
    ...
}

**Key:** The title of the book.  
**Value:** The return date in the format YYYY-MM-DD.

When a member borrows a book, the book's title and the return date are added to the `borrowed_books` dictionary of the member. This allows the system to keep track of which books are borrowed and when they are due to be returned.

When a member returns a book, the system checks if the book title exists in the member's `borrowed_books` dictionary. If it does, the entry (key-value pair) is removed from the dictionary, indicating that the book has been returned.
