import tkinter as gui
from tkinter import ttk as components
from PIL import Image, ImageTk
import connection


# Quit Function
def quit_application():
    frame.destroy()


# Sign In Process
def signIn_process():
    fname = fname_text.get()
    lname = lname_text.get()
    age = age_text.get()

    if fname.isalpha():
        fname = fname.capitalize()  # Capitalize first letter
        if lname.isalpha():
            lname = lname.capitalize()  # Capitalize first letter
            if age.isdigit():
                age = int(age)
                system_label.config(text="")
                message_label.config(text="")

                # Search Query
                user_result = connection.search(
                    f"SELECT * FROM `user` WHERE `fname` = '{fname}' AND `lname`='{lname}'"
                )
                if user_result:
                    system_label.config(text="SYSTEM:")
                    message_label.config(text="User already exists")
                else:
                    # Success Code

                    # Insert Query
                    connection.iud(
                        f"INSERT INTO `user` (`fname`,`lname`,`age`) VALUES ('{fname}','{lname}','{age}')"
                    )

                    system_label.config(text="SYSTEM:")
                    message_label.config(text="User registered Successfully")
            else:
                system_label.config(text="SYSTEM:")
                message_label.config(text="Please enter a valid age")
        else:
            system_label.config(text="SYSTEM:")
            message_label.config(text="Please enter a valid name")
    else:
        system_label.config(text="SYSTEM:")
        message_label.config(text="Please enter a valid name")


# Back Function
def back():
    frame.destroy()
    import main

    main.main()


# Sign In Screen
def user_signin_screen():
    global frame
    global fname_text, lname_text, message_label, system_label, age_text

    # frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("User Sign In")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # header
    welcome_font = ("Quicksand", "20", "bold")
    label = components.Label(frame, text="User Sign In", font=welcome_font)
    label.pack(pady=(35, 30))

    image = Image.open("resources/user.jpg")
    resized_image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)

    imgLabel = components.Label(frame, image=photo)
    imgLabel.image = photo
    imgLabel.pack()

    # form
    fname_label = components.Label(frame, text="Enter your first Name", justify="left")

    fname_text = components.Entry(
        frame,
        width=25,
        font=("Quicksand", 12),
        justify="left",
    )
    lname_label = components.Label(frame, text="Enter your last name", justify="left")

    lname_text = components.Entry(
        frame, width=25, font=("Quicksand", 12), justify="left"
    )
    age_label = components.Label(frame, text="Enter your age", justify="left")
    age_text = components.Entry(frame, width=25, font=("Quicksand", 12), justify="left")

    fname_label.pack(pady=(15, 0))
    fname_text.pack()
    lname_label.pack(pady=(15, 0))
    lname_text.pack()
    age_label.pack(pady=(15, 0))
    age_text.pack()

    style.configure(
        "Custom.TButton",
        font=("Quicksand", 12),
        width=25,
        foreground="blue",
        background="red",
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
        text="User Sign In",
        style="Custom.TButton",
        # Function Calling
        command=signIn_process,
    )
    login_button.pack(padx=10, pady=(20, 10))

    exit_button = components.Button(
        frame,
        text="Back",
        style="Custom1.TButton",
        # Function Calling
        command=back,
    )
    exit_button.pack(padx=10)

    # labels
    label_frame = gui.Frame()
    label_frame.pack()

    style.configure(
        "Label",
        foreground="blue",
    )

    system_label = components.Label(
        label_frame, text="", font=("Quicksand", 10, "bold"), style="Label"
    )
    message_label = components.Label(label_frame, text=" ", font=("Quicksand", 10))

    system_label.pack(side="left", pady=5)
    message_label.pack(side="left", pady=5)

    frame.mainloop()


# Main method
def main():
    user_signin_screen()


main()
