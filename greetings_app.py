import tkinter as tk
import greetings

def display_greeting(language):
    if language == "English":
        greeting_label.config(text=greetings.english_greeting())

    elif language == "French":
        greeting_label.config(text=greetings.french_greeting())

    elif language == "Spanish":
        greeting_label.config(text=greetings.spanish_greeting())

    elif language == "Swahili":
        greeting_label.config(text=greetings.swahili_greeting())


#Main application window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x300")

#Welcome label
welcome_label = tk.Label(root, text = "Click a button to see a greeting", font = ("Arial, 12"))
welcome_label.pack(pady=20)

# Dynamic label to display the greeting
greeting_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
greeting_label.pack(pady=20)


buttons = [
    ("English", "English"),
    ("French", "French"),
    ("Spanish", "Spanish"), 
    ("Swahili", "Swahili")
]

# Create buttons dynamically
for text, language in buttons:
    button = tk.Button(root, text=text, command=lambda lang=language: display_greeting(lang))
    button.pack(pady=5)

# Start the tkinter main loop
root.mainloop()
