import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    characters = lowercase_letters + uppercase_letters + digits + special_chars

    if not characters:
        result_label.config(text="Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(text=password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label for length input
length_label = ttk.Label(window, text="Password Length:")
length_label.pack()

# Entry for password length
length_entry = ttk.Entry(window)
length_entry.pack()

# Checkboxes for including digits and special characters
include_digits_var = tk.BooleanVar()
include_special_chars_var = tk.BooleanVar()

include_digits_checkbox = ttk.Checkbutton(window, text="Include Digits (0-9)", variable=include_digits_var)
include_digits_checkbox.pack()

include_special_chars_checkbox = ttk.Checkbutton(window, text="Include Special Characters", variable=include_special_chars_var)
include_special_chars_checkbox.pack()

# Button to generate password
generate_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
password_display = ttk.Label(window, text="", font=("Helvetica", 16))
password_display.pack()

# Start the GUI main loop
window.mainloop()
