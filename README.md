# Contact Book (Python)

A simple command-line Contact Book application implemented in Python
using Object-Oriented Programming. This project allows users to add,
view, update, and delete contacts that include a name, phone number, and
email address.

## Features

-   Add a new contact with name, phone, and email\
-   View a specific contact's details\
-   Update an existing contact's phone or email\
-   Delete a contact\
-   Simple CLI menu for interaction

## Requirements

-   Python 3.x

No external libraries are required except for Python's built-in
`collections` module.

## How to Run

1.  Save the script as `contact_book.py`

2.  Open a terminal and navigate to the file directory:

    ``` bash
    cd path/to/your/file
    ```

3.  Run the script:

    ``` bash
    python contact_book.py
    ```

## Usage

After running the script, a menu will appear:

    1. Add Contact
    2. View Contact
    3. Update Contact
    4. Delete Contact
    5. Exit

Enter the number of the action you want, then follow the prompts.

### Example

**Add Contact**

    Enter name: John
    Enter phone (optional): 12345
    Enter email (optional): john@example.com
    Contact 'John' added successfully.

**View Contact**

    Enter name to view: John
    Name: John
    Phone: 12345
    Email: john@example.com

## Code Structure

-   `ContactBook` class
    -   `add_contact()`\
    -   `view_contact()`\
    -   `view_contact()`\
    -   `update_contact()`\
    -   `delete_contact()`

Uses `defaultdict` to manage contact entries.

## License

Free to use, modify, and share.
