# Password Manager

## Description

This is a Password Manager built with Python and Tkinter, designed to help users securely store and generate passwords locally. The application allows users to enter and save their website, username, and password information, with the option to generate strong passwords. The project demonstrates the use of Object-Oriented Programming (OOP), graphical user interfaces (GUI), and file handling in Python.

## Features

- **Password Generation**: Generates secure random passwords with a combination of lowercase, uppercase, numbers, and special characters.
- **Password Saving**: Saves entered passwords to a file, allowing users to retrieve their saved passwords later.
- **Password Validation**: Ensures that generated passwords meet common security requirements such as length and character variety.
- **GUI Interface**: Provides an easy-to-use graphical interface for interacting with the password manager.

![Password Manager](Password%20manager_app.PNG)
  
## Requirements

- Python 3.x
- `pyperclip` (install via `pip install pyperclip`)
- `tkinter` (pre-installed with Python)
  
## How to Use

<details>
<summary>Click here for detailed instructions</summary>

1. **Start the Application**:
   - Run the `main.py` script using Python. This will open the password manager GUI.

2. **Input**:
   - **Website**: Enter the website for which you're saving credentials.
   - **Username**: Enter the associated username or email address.
   - **Password**: Enter the password for the website or generate a new one using the "Generate Password" button.

3. **Functionality**:
   - Click the "Generate Password" button to generate a new password, which will automatically be copied to your clipboard.
   - After filling in the details, click the "Add" button to save the credentials to a file (`data.txt`).
   - A confirmation message will show up to verify the saved data.

     ![Confirmation Message](Password%20manager%20confirmation.PNG)

4. **Empty Fields Warning**:
   - If any of the fields (Website, Username, or Password) are left empty and the "Add" button is clicked, a warning message will appear, asking the user to fill in all fields before saving.
  
     ![Warning Message](Password%20manager%20warning.PNG)
     
</details>

## Code Structure

The project consists of several files. Here is a breakdown of each file and its purpose:

<details>
<summary>Click here for file breakdown</summary>

### `main.py`
- **Purpose**: Contains the core logic for the Password Manager app, handling GUI elements, user inputs, and password management.
- **Key Functions**:
  - `__init__(self)`: Initializes the app and sets up the main window, labels, entry boxes, and buttons.
  - `generate_password(self)`: Generates a random password and inserts it into the password entry box.
  - `save(self)`: Saves the entered data (website, username, and password) to a file.
  - `password_validation(self)`: Validates the password to meet security requirements using a regex pattern.

### `constants.py`
- **Purpose**: Stores constant values like the font name used in the app.
  
### `data.txt`
- **Purpose**: Stores the saved website credentials (website, username, and password).

### `logo.png`
- **Purpose**: The image file for the logo that is displayed on the app's GUI.
</details>

## How to Run

1. Clone or download the project files.
2. Make sure Python 3.x is installed on your computer.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the application:
   ```bash
   python main.py
   ```

## Future Improvements

<details>
<summary>Click here for possible future improvements</summary>

- **Improvement 1**: Allow the user to edit or delete saved entries.
- **Improvement 2**: Add a feature to encrypt the saved passwords for better security.
- **Improvement 3**: Implement a password strength checker that gives feedback to the user.
- **Improvement 4**: Allow users to categorize or tag saved passwords for easier organization.
  
</details>

## Credits

This project was created as part of a personal project to learn about GUI development and password management using Python and Tkinter. Thank you to the Python community for providing resources and libraries that made this project possible.

## Change Log

<details>
<summary>Click here to view change log</summary>

### Version 1.0.0
- **Initial Release**: Basic functionality including password generation, saving, and GUI setup.

### Bug Fixes
- Fixed minor GUI layout issues for better visibility.

### Known Issues
- No known issues at this time.

</details>
