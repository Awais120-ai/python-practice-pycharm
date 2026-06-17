# import random
#
# chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
#
# length = int(input("Enter password length: "))
#
# password = ""
#
# for i in range(length):
#     password += random.choice(chars)
#
# print("Generated Password:", password)
#
import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(entry.get())

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = ""
    for _ in range(length):
        password += random.choice(chars)

    result_label.config(text="Password: " + password)


# Window setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x300")

# Label
label = tk.Label(window, text="Enter Password Length:")
label.pack(pady=10)

# Input box
entry = tk.Entry(window)
entry.pack(pady=5)

# Button
button = tk.Button(window, text="Generate Password", command=generate_password)
button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run app
window.mainloop()
