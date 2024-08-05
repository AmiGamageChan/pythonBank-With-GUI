import tkinter as gui
from tkinter import ttk as components
from PIL import Image, ImageTk
import connection as con

# Transactions
import transactions.deposit as deposit
import transactions.withdraw as withdraw
import transactions.transfer as transfer


# Quit Function
def quit_application():
    frame.destroy()


# Main User Screen
def user_screen(accId):
    global frame

    # frame
    frame = gui.Tk()
    style = components.Style()

    # Search Query
    resultset = con.search(f"SELECT * FROM `user` WHERE `id` = '{accId}'")
    resultset1 = con.search(f"SELECT * FROM `balance` WHERE `accId` = '{accId}'")
    user = resultset[0][1]  # Username
    balance = resultset1[0][1]  # Balance

    frame.title("Ami Bank")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # user frame
    user_frame = gui.Frame(frame)
    user_frame.pack(pady=(50, 10))

    # user label
    system_user_label = components.Label(
        user_frame, text="Welcome user:", font=("Quicksand", "12", "bold")
    )
    user_label = components.Label(user_frame, text=f"{user}", font=("Quicksand", "12"))

    system_user_label.pack(side="left")
    user_label.pack()

    # balance frame
    balance_frame = gui.Frame(frame)
    balance_frame.pack()

    # balance label
    system_balance_label = components.Label(
        balance_frame, text="Your current balance:", font=("Quicksand", "12", "bold")
    )
    balance_label = components.Label(
        balance_frame, text=f"{balance}$", font=("Quicksand", "12")
    )

    system_balance_label.pack(side="left")
    balance_label.pack()

    # topic label
    topic_label = components.Label(
        frame, text=("Select Your Transaction"), font=("Quicksand", "12")
    )
    topic_label.pack(pady=25)

    # button frame
    button_frame = gui.Frame(frame)
    button_frame.pack()

    # buttons
    #Custom style
    style.configure(
        "Custom.TButton",
        font=("Quicksand", 10, "bold"),
        width=25,
        padding=10,
        foreground="black",
        background="blue",
    )

    deposit_button = components.Button(
        button_frame,
        text="Deposit",
        style="Custom.TButton",
        # Function Call
        command=lambda: transaction(1),
    )
    withdraw_button = components.Button(
        button_frame,
        text="Withdraw",
        style="Custom.TButton",
        # Function Call
        command=lambda: transaction(2),
    )
    transfer_button = components.Button(
        button_frame,
        text="Transfer",
        style="Custom.TButton",
        # Function Call
        command=lambda: transaction(3),
    )

    deposit_button.pack(pady=(25, 15))
    withdraw_button.pack(pady=15)
    transfer_button.pack(pady=15)

    frame.mainloop()


# Transaction Redirection
def transaction(id):
    id = int(id)
    if id == 1:
        frame.destroy()
        # Function Call
        deposit.main()
    elif id == 2:
        # Function Call
        withdraw.main()
    elif id == 3:
        # Function Call
        transfer.main()


# Main Function
def main(accId):
    user_screen(accId)


main(1)
