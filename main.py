import tkinter as gui
from tkinter import ttk as components  # Some components
from PIL import Image, ImageTk
import login
import signin


# Quit Function
def quit_application():
    frame.destroy()

# User Login Redirection
def redirect_user_login():
    frame.destroy()
    # Function Call
    login.main()
    
def redirect_user_signIn():
    frame.destroy()
    # Function Call
    signin.main()


# Welcome Screen
def welcome_screen():
    global frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank App")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # header
    welcome_font = ("Quicksand", "24", "bold")
    label = components.Label(frame, text="Welcome to Ami Bank", font=welcome_font)
    label.pack(pady=10)

    # image
    image = Image.open("resources/bank.png")
    resized_image = image.resize((400, 400), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    label1 = components.Label(frame, image=photo)
    label1.image = photo
    label1.pack()

    # buttons
    button_frame = gui.Frame(frame)
    button_frame.pack(pady=25)

    style.configure("Custom.TButton", font=("Quicksand", 12), width=10, padding=3)

    login_button = components.Button(
        button_frame,
        text="User Login",
        style="Custom.TButton",
        # Function Call
        command=redirect_user_login,
    )

    signin_button = components.Button(
        button_frame,
        text="User Sign In",
        style="Custom.TButton",
        # Function Call
        command=redirect_user_signIn,
    )

    quit_button = components.Button(
        button_frame,
        text="❌",
        style="Custom.TButton",
        # Function Call
        command=quit_application,
    )

    login_button.pack(side="left", padx=1)
    signin_button.pack(side="left", padx=1)
    quit_button.pack(side="left", padx=1)

    # Run
    frame.mainloop()


# Main Method
def main():
    welcome_screen()


main()
