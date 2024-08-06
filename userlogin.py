import tkinter as gui
from tkinter import ttk as components
from PIL import Image, ImageTk
import connection
import accounts


# Quit Function
def quit_application():
    frame.destroy()


# Sign In Process
def logIn_process():
    nic = nic_text.get()

    if nic.isdigit():
        nic = int(nic)

        nic_result = connection.search(f"SELECT `id` FROM `user` WHERE `nic` = '{nic}'")
        uId = nic_result[0][0]
        
        frame.destroy()
        accounts.main(uId)
        
    else:
        system_label.config(text="SYSTEM:")
        message_label.config(text="Please enter a valid NIC")


# Back Function
def back():
    frame.destroy()
    import login

    login.main(0,0)


# Sign In Screen
def user_login_screen():
    global frame
    global message_label, system_label, nic_text

    # frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank - User Sign In")
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

    nic_label = components.Label(frame, text="Enter your NIC", justify="left")
    nic_text = components.Entry(frame, width=25, font=("Quicksand", 12), justify="left")

    nic_label.pack(pady=(15, 0))
    nic_text.pack()

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
        text="User Log In",
        style="Custom.TButton",
        # Function Calling
        command=logIn_process,
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
    user_login_screen()