import tkinter as gui
from tkinter import ttk as components  # Some components
from PIL import Image, ImageTk


# Quit Application
def quit_application():
    frame.destroy()


# Create Frame From Templaye
def create_frame(section, transaction):
    # frame
    global frame
    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank App")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # transaction label
    transaction_label = components.Label(
        frame, text=(f"{section} Section"), font=("Quicksand", "15", "bold")
    )
    transaction_label.pack(pady=50)

    # image
    image = Image.open("resources/money.jpg")
    resized_photo = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_photo)

    label1 = components.Label(frame, image=photo)
    label1.image = photo
    label1.pack()

    # input section
    input_label = components.Label(
        frame,
        text=f"How much money would you like to {transaction}?",
        font=("Quicksand", "11"),
        anchor="w",
    )
    input_amount = components.Entry(
        frame, width=33, font=("Quicksand", 11), justify="left"
    )

    input_label.pack(pady=(50, 5))
    input_amount.pack(pady=(0, 20))

    # button frame
    button_frame = gui.Frame(frame)
    button_frame.pack()

    # buttons
    # Custom style
    style.configure(
        "Custom.TButton",
        font=("Quicksand", 10, "bold"),
        width=32,
        padding=3,
        foreground="black",
        background="green",
    )

    button = components.Button(
        button_frame,
        text="Deposit",
        style="Custom.TButton",
        # Function Call
        command=lambda: transaction(),
    )
    button.pack()

    frame.mainloop()
