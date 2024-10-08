import tkinter as gui
from tkinter import ttk as components
from PIL import Image, ImageTk
import connection as con
from functools import partial
import user


# Quit Function
def quit_application():
    frame.destroy()


# Back function
def exit():
    frame.destroy()
    import main

    main.main()


# Exit To Accounts Function
def exit_to_accounts(uId):
    frame.destroy()
    import accounts

    accounts.main(uId)


# User Logged In Screen Redirection
def user_logged_in(accId):
    frame.destroy()
    user.main(accId)


# User Login Redirection
def user_login():
    frame.destroy()
    import userlogin

    userlogin.main()


# Login Screen
def user_login_screen(uId, accId=None):
    global frame
    global accId_text, password_text, message_label, system_label

    # frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank - Account Login")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)
    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # header
    welcome_font = ("Quicksand", "20", "bold")
    label = components.Label(frame, text="Account Login", font=welcome_font)
    label.pack(pady=50)

    image = Image.open("resources/lock.png")
    resized_image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    imgLabel = components.Label(frame, image=photo)
    imgLabel.image = photo
    imgLabel.pack()

    # form
    accId_label = components.Label(frame, text="Enter your Account ID", justify="left")
    accId_label.pack(pady=(15, 0))
    accId_text = components.Entry(
        frame,
        width=25,
        font=("Quicksand", 12),
        justify="left",
    )
    if accId:
        accId_text.insert(0, str(accId))
    accId_text.pack()

    password_label = components.Label(frame, text="Enter your Password", justify="left")
    password_label.pack(pady=(15, 0))
    password_text = components.Entry(
        frame, width=25, font=("Quicksand", 12), justify="left", show="*"
    )
    password_text.pack()

    style.configure(
        "Custom.TButton",
        font=("Quicksand", 12),
        width=25,
        foreground="green",
        background="blue",
    )

    style.configure(
        "Custom1.TButton",
        font=("Quicksand", 12),
        width=25,
        foreground="red",
        background="black",
    )

    # buttons
    login_button = components.Button(
        frame,
        text="Account Login",
        style="Custom.TButton",
        command=login_process,
    )
    login_button.pack(padx=10, pady=(20, 0))

    user_login_button = components.Button(
        frame,
        text="User Login",
        style="Custom.TButton",
        command=user_login,
    )
    user_login_button.pack(padx=10, pady=(10, 10))

    # exit button
    if accId != 0:
        button_exit1 = components.Button(
            frame,
            text="Back",
            style="Custom1.TButton",
            command=lambda: exit_to_accounts(uId),
        )
        button_exit1.pack(padx=10)
    else:
        button_exit = components.Button(
            frame, text="Back", style="Custom1.TButton", command=exit
        )
        button_exit.pack(padx=10)

    # labels
    label_frame = gui.Frame()
    label_frame.pack()

    style.configure("Label", foreground="blue")

    system_label = components.Label(
        label_frame, text="", font=("Quicksand", 10, "bold"), style="Label"
    )
    message_label = components.Label(label_frame, text=" ", font=("Quicksand", 10))

    system_label.pack(side="left")
    message_label.pack(side="left")

    frame.mainloop()


# Login Function
def login_process():
    accId = accId_text.get()
    password = password_text.get()

    if accId.isdigit():
        system_label.config(text="")
        message_label.config(text=(""))

        accId = int(accId)  # Account ID
        password = str(password)  # Password

        # Search Query
        resultset = con.search(
            f"SELECT * FROM `accounts` WHERE `account_id` = '{accId}' AND `password` = '{password}'"
        )

        if len(resultset) == 1:
            system_label.config(text="SYSTEM:")
            message_label.config(text=("Logged in Successfully"))
            user_logged_in(accId)
        else:
            system_label.config(text="SYSTEM:")
            message_label.config(text=("Account ID or Password error"))
    else:
        system_label.config(text="SYSTEM:")
        message_label.config(text=("Please enter a valid Account ID"))


# Main method
def main(uId, accId=None):
    user_login_screen(uId, accId)
