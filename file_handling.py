with open("user.txt", "w") as file:
    file.write("Name: Awais")
    file.write("\nage: 20")
with open("user.txt", "r") as file:
    print(file.read())

# ..................take it from user.............

name = input("Enter your name: ")
age = input("Enter your age: ")

with open("user.txt", "a") as file:
    file.write("\nName: " + name)
    file.write("\nAge: " + age)
with open("user.txt", "r") as file:
    print(file.read())

# ....................login system code ................


correct_username = "awais"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! 🎉")
else:
    print("Invalid username or password ❌")

    # ............................................

    import random

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    length = int(input("Enter password length: "))

    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Generated Password: ", password)

    # Save to files
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

    print("Password saved in file ✅")



