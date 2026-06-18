print("hey i am your mini project!")
print("type 'bye' to exit\n")

while True:
    user = input("you : ")
    if user == "hello":
        print("welcome back")
    elif user == "how are you":
        print("i am fine what about you! ")
    elif user == "what is python!":
        print("python is a programming language.")
    elif user == "help":
        print("this is a help message")
    elif user == "bye":
        print("bye, good bye take care Awais")
        break
    else:
        print("i dont understand it !")



# ....................gui chat box ,,,........

import tkinter as tk

# window setup
window = tk.Tk()
window.title("Mini Chatbot")
window.geometry("400x500")

# chat display box
chat_area = tk.Text(window, height=20, width=50)
chat_area.pack()

# input box
user_input = tk.Entry(window, width=40)
user_input.pack()

# bot reply function
def send_message():
    user = user_input.get().lower()
    chat_area.insert(tk.END, "You: " + user + "\n")

    if user == "hello":
        reply = "Hello! 😊"

    elif user == "how are you":
        reply = "I'm fine 👍"

    elif user == "what is python":
        reply = "Python is a programming language 🐍"

    elif user == "bye":
        reply = "Goodbye 👋"
        chat_area.insert(tk.END, "Bot: " + reply + "\n")
        window.after(1000, window.destroy)
        return

    else:
        reply = "I don't understand 😅"

    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
    user_input.delete(0, tk.END)

# send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

window.mainloop()