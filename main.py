
from tkinter import *
from tkinter import messagebox
from constants import *
import json
import pyperclip
import random
import string
import re


class Password_Manager_App:
    def __init__(self):
        """Initialize the app by setting up the main window, canvas, labels, entry boxes, and buttons."""
        self.main_window_setup()
        self.canvas_for_logo()
        self.labels()
        self.entry_boxes()
        self.buttons()

    def main_window_setup(self):
        """Set up the main Tkinter window."""
        self.main_window = Tk()
        self.main_window.config(padx=20, pady=20, width=500, height=500)
        self.main_window.title("Password manager")
        self.main_window.resizable(0,0)
        
    def canvas_for_logo(self):
        """Display the app logo on the canvas."""
        self.canvas = Canvas(width=250, height=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=1, column=1)
# ---------------------------- WEBSITE FIELD ------------------------------- #
    def website_label(self):
        """Create the label for the website field."""
        self.website = Label(padx=2, pady=2, text="Website:", font=(FONT_NAME, 10, "bold"))
        self.website.grid(row=2, column=0, sticky="E")

    def website_entry_box(self):
        """Create the entry box for the website URL."""
        self.website_entry = Entry(width=40)
        self.website_entry.grid(row=2, column=1, sticky="W")
        self.website_entry.focus()

# ---------------------------- USERNAME FIELD ------------------------------- #    
    def username_label(self):
        """Create the label for the username field."""
        self.username = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
        self.username.grid(row=3, column=0, sticky="E")

    def username_entry_box(self):
        """Create the entry box for the username."""
        self.username_entry = Entry(width=60)
        self.username_entry.grid(row=3, column=1, columnspan=2, sticky="W")
        self.username_entry.insert(0, "your_email@domain.com")

# ---------------------------- PASSWORD FIELD ------------------------------- #
    def password_label(self):
        """Create the label for the password field."""
        self.password = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
        self.password.grid(row=4, column=0, sticky="E")

    def password_entry_box(self):
        """Create the entry box for the password."""
        self.password_entry = Entry(width=30)
        self.password_entry.grid(row=4, column=1, sticky="W")

    def password_generator_button(self):
        """Create the 'Generate Password' button."""
        self.password_button = Button(width=24, text="Generate Password", command=self.generate_password)
        self.password_button.grid(row=4, column=1, sticky="E", padx=1, pady=1, columnspan=2)
# ---------------------------- 'ADD' BUTTON ---------------------------------- #
    def add_button_field(self):
        """Create the 'Add' button to save the entry."""
        self.add_button = Button(width=50, text="Add", command=self.save)
        self.add_button.grid(row=5, column=1, sticky="E", padx=1, pady=1, columnspan=3)
# ---------------------------- SEARCH BUTTON --------------------------------------------- #
    def search_password(self):
        """Create the 'Search' button to find your password."""
        self.search_button = Button(width=15, text="Search", command=self.search)
        self.search_button.grid(row=2, column=1, columnspan=2, sticky="E", padx=1, pady=1,)

# ---------------------------- SAVE LOGIC ---------------------------------- #
    def save(self):     
        """Save the entered data (website, username, and password) to a JSON file."""
        self.website_c = self.website_entry.get()
        self.username_c = self.username_entry.get()
        self.password_c = self.password_entry.get()
        self.new_data = { 
            self.website_c: {
                "email" : self.username_c,
                "password": self.password_c,   
            }}

        if self.website_c and self.username_c and self.password_c:
            self.is_ok = messagebox.askokcancel(title="Data Entry Confirmation", message=f"This are the details entered:\nWebsite: {self.website_c}"
                                                f"\nEmail/Username: {self.username_c}"
                                                f"\nPassword: {self.password_c}"
                                                f"\nIs it ok to save?")
            if self.is_ok:
                    try:
                        with open("data.json", "r") as data_file:
                            self.data = json.load(data_file)
                    except FileNotFoundError:
                        with open("data.json", "w") as data_file:
                            json.dump(self.new_data, data_file, indent=4)
                    else:
                        self.data.update(self.new_data)
                        with open("data.json", "w") as data_file:
                            json.dump(self.data, data_file, indent=4)
                    finally:
                        self.website_entry.delete(0, END)
                        self.password_entry.delete(0, END)

                    self.password_saved_label = Label(text="Password Saved!", fg="green", width=20 , font=(FONT_NAME, 10, "bold"))
                    self.password_saved_label.grid(row=6, column=0, padx=2, pady=2, columnspan=2)
                    self.password_saved_label.after(4000, self.clear_label)
        else:
            messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty!!")
    
    def clear_label(self):
        """Clear the 'Password Saved' label after a short delay."""
        self.password_saved_label.config(text="")
# ---------------------------- SEARCH PASSWORD -------------------------- #
    def search(self):
        """Search for a website in the JSON file and display the associated email and password."""
        self.website_search = self.website_entry.get()
        
        if self.website_search:
            try:
                with open("data.json", "r") as data_file:
                    self.data = json.load(data_file)

                    if self.website_search in self.data:
                        email = self.data[self.website_search]["email"]
                        password = self.data[self.website_search]["password"]
                        messagebox.showinfo(title="Details Found!",
                        message=f"Website: {self.website_search}\nEmail|Username: {email}\nPassword: {password}" )
                    else:
                        messagebox.showerror(title="Not Found :(",
                        message=f"No details for '{self.website_search}' found in the database.")
            except FileNotFoundError:
                messagebox.showerror(title="ERROR",
                message="File Not Found!")
            except json.JSONDecodeError:
                messagebox.showerror(title="ERROR",
                message="Data file is corrupted!")
        else:
            messagebox.showwarning(title="Input Error", message="Please enter a website to search!")


# ---------------------------- PASSWORD GENERATOR -------------------------- #
    def generate_password(self, length=16):
        """Generate a random password and insert it into the password entry box."""
        self.password_entry.delete(0, END)
        
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.numbers = string.digits
        # Limited set of special characters to ensure compatibility
        self.special = "!@#$%^&*()_-+=<>?[]{}|;:,.~`"

        self.make_password = self.lower + self.upper + self.numbers + self.special
        self.password = ''.join(random.choice(self.make_password) for _ in range(length))

        while not self.password_validation(self.password):
            self.password = ''.join(random.choice(self.make_password) for _ in range(length))

        self.password_entry.insert(0, self.password)
        pyperclip.copy(self.password)


    def password_validation(self, password):
        """Validate the password to meet security requirements using a regex pattern."""
        # Regular expression to check if password meets the criteria
        regex = (
            r'^(?=.*[a-z])'        # At least one lowercase letter
            r'(?=.*[A-Z])'          # At least one uppercase letter
            r'(?=.*\d)'             # At least one digit
            r'(?=.*[' + re.escape(string.punctuation) + r'])'  # At least one special character
            r'.{' + str(8) + r',}$'  # Minimum length of 8 characters
        )
        
        # Check if the password matches the regex
        return bool(re.match(regex, password))

# -------------------------------------------------------------------------- #

    def labels(self):
        """Create labels for the website, username, and password fields."""
        self.website_label()
        self.username_label()
        self.password_label()
        
    
    def entry_boxes(self):
        """Create entry boxes for the website, username, and password fields."""
        self.website_entry_box()
        self.username_entry_box()
        self.password_entry_box()

    def buttons(self):
        """Create buttons for password generation and adding fields."""
        self.password_generator_button()
        self.add_button_field()
        self.search_password()
    
    def run(self):
        """Run the Tkinter main event loop."""
        self.main_window.mainloop()


if __name__ == "__main__":
    app = Password_Manager_App()
    app.run()