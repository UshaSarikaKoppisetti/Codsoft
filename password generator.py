import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, uppercase, digits, special_characters):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        uppercase = uppercase_var.get()
        digits = digits_var.get()
        special_characters = special_var.get()

        password = generate_password(length, uppercase, digits, special_characters)

        result_label.config(text=f"Generated Password: {password}", fg="green")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid length.")
        result_label.config(text="Error", fg="red")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.config(bg="#e6e6e6")  


length_label = tk.Label(root, text="Enter the length of the password:", bg="#e6e6e6")
length_label.pack()

length_entry = tk.Entry(root, bg="white")
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, bg="#e6e6e6")
uppercase_checkbox.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var, bg="#e6e6e6")
digits_checkbox.pack()

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, bg="#e6e6e6")
special_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, bg="#4CAF50", fg="white")
generate_button.pack()

result_label = tk.Label(root, text="", bg="#e6e6e6")
result_label.pack()


root.mainloop()
