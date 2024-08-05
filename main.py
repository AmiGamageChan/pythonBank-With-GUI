import tkinter as gui
from tkinter import ttk as components  # Some components
from PIL import Image, ImageTk
import login


# Quit Function
def quit_application():
    frame.destroy()


# User Login Redirection
def redirect_user_login():
    frame.destroy()
    login.main()


# Welcome Screen
def welcome_screen():
    global frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank App")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # Header
    welcome_font = ("Quicksand", "24", "bold")
    label = components.Label(frame, text="Welcome to Ami Bank", font=welcome_font)
    label.pack(pady=10)

    # Image Section
    image = Image.open("resources/bank.png")
    resized_image = image.resize((400, 400), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    label1 = components.Label(frame, image=photo)
    label1.image = photo
    label1.pack()

    # Button Section
    button_frame = gui.Frame(frame)
    button_frame.pack(pady=25)

    style.configure("Custom.TButton", font=("Quicksand", 12), width=15, padding=4)

    login_button = components.Button(
        button_frame,
        text="User Login",
        style="Custom.TButton",
        command=redirect_user_login,
    )
    login_button.pack(side="left", padx=10)

    quit_button = components.Button(
        button_frame, text="Exit App", style="Custom.TButton", command=quit_application
    )
    quit_button.pack(side="left", padx=10)

    # Run
    frame.mainloop()


# Main Method
def main():
    welcome_screen()


main()
