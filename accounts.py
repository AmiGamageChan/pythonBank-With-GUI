import tkinter as gui
from tkinter import ttk as components
import connection as con
from functools import partial


# Quit Function
def quit_application():
    frame.destroy()


# Label Click Function
def label_click(event, accId, uId):
    frame.destroy()

    import login

    login.main(uId, accId)


# Main User Screen
def accounts_screen(uId):
    global frame

    # frame
    frame = gui.Tk()
    style = components.Style()

    # Search Query
    username_resultset = con.search(f"SELECT * FROM `user` WHERE `id` = '{uId}'")
    username = username_resultset[0][1]

    frame.title("Ami Bank - User Accounts")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

    # user frame
    user_frame = gui.Frame(frame)
    user_frame.pack(pady=(30, 10))

    style.configure(
        "Custom1.TButton",
        font=("Quicksand", 12),
        width=25,
        foreground="red",
        background="black",
    )

    # user label
    system_user_label = components.Label(
        user_frame, text="Welcome user:", font=("Quicksand", "12", "bold")
    )
    user_label = components.Label(
        user_frame, text=f"{username}", font=("Quicksand", "12")
    )

    system_user_label.pack(side="left")
    user_label.pack()

    # Search Query
    accounts = con.search(
        f"SELECT `account_id` FROM `accounts` WHERE `user_id` = '{uId}' "
    )

    # Canvas and Scrollbar
    canvas = gui.Canvas(frame)
    scrollbar = components.Scrollbar(frame, orient="vertical", command=canvas.yview)

    # Create a Frame for the Canvas
    canvas_frame = gui.Frame(canvas)
    canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

    # Pack Canvas and Scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configure scrollbar to work with canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Update the Canvas scroll region
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas_frame.bind("<Configure>", on_frame_configure)

    # Label Frame
    label_frame = gui.Frame(canvas_frame)
    label_frame.pack(padx=50, pady=(15, 0), fill="x")

    # Label making for accounts
    for result in accounts:
        accId = result[0]  # AccID

        acc_balance_result = con.search(
            f"SELECT `balance` FROM `balance` WHERE `accId` = {accId}"
        )
        acc_balance = acc_balance_result[0][0]

        # Border Frame
        id_label_frame = gui.Frame(
            label_frame, borderwidth=2, relief="solid", padx=30, pady=10
        )
        id_label_frame.pack(
            padx=15, pady=10, fill="x"
        )  # Adjust the padding between labels

        id_label_frame.bind("<Button-1>", partial(label_click, accId=accId, uId=uId))

        # Label with account ID
        id_label = components.Label(
            id_label_frame, text=f"Account ID: {accId}", font=("Quicksand")
        )
        id_label.bind("<Button-1>", partial(label_click, accId=accId, uId=uId))
        balance_label = components.Label(
            id_label_frame, text=f"Account Balance: {acc_balance}", font=("Quicksand")
        )
        id_label.pack(side="top", anchor="w")
        balance_label.bind("<Button-1>", partial(label_click, accId=accId, uId=uId))
        balance_label.pack(side="top", anchor="w")

    # Initial canvas configuration
    on_frame_configure(None)

    frame.mainloop()


def main(uId):
    accounts_screen(uId)
