import tkinter as gui
from tkinter import ttk as components
from PIL import Image, ImageTk
import connection

# Quit Function
def quit_application():
    frame.destroy()

# Back Function
def back(accId):
    frame.destroy()
    import user
    user.main(accId)
    
# Transaction Redirection
def transaction_redirect(transaction, accId):
    if transaction == "deposit" or transaction == "withdraw":
        basic_transaction_process(transaction, accId)
    else:
        transfer_transaction_process(accId)

# Basic Transactions
def basic_transaction_process(transaction, accId):
    amount = input_amount.get()
    if amount.isdigit():
        amount = int(amount)
        if amount == 0:
            system_result_label.config(text="SYSTEM:")
            result_label.config(text="Please enter the amount of money")
        else:
            resultset = connection.search(
                f"SELECT * FROM `balance` WHERE `accId` = '{accId}'"
            )
            current_balance = resultset[0][1]
            current_balance = int(current_balance)

            if transaction == "deposit":
                new_balance = current_balance + amount
                connection.iud(
                    f"UPDATE `balance` SET `balance` = '{new_balance}' WHERE `accId` = '{accId}'"
                )
                connection.iud(
                    f"INSERT INTO `transactions` (`accId`,`transOperation`,`amount`) VALUES ('{accId}','{transaction}','{amount}')"
                )
                input_amount.delete(0, "end")
                system_result_label.config(text="SYSTEM:")
                result_label.config(text="Money deposited successfully")
            else:
                new_balance = current_balance - amount
                connection.iud(
                    f"UPDATE `balance` SET `balance` = '{new_balance}' WHERE `accId` = '{accId}'"
                )
                connection.iud(
                    f"INSERT INTO `transactions` (`accId`,`transOperation`,`amount`) VALUES ('{accId}','{transaction}','{amount}')"
                )
                input_amount.delete(0, "end")
                system_result_label.config(text="SYSTEM:")
                result_label.config(text="Money withdrawn successfully")
    else:
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="Please enter a valid amount of money")

# Transfer Function
def transfer_transaction_process(accId):
    print("F")

# Main, Create Frame
def create_frame(section, transaction, accId):
    global frame
    global system_result_label, result_label, input_amount

    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank App")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW",quit_application)

    transaction_label = components.Label(
        frame, text=f"{section} Section", font=("Quicksand", "15", "bold")
    )
    transaction_label.pack(pady=50)

    # Handle Image
    try:
        image = Image.open("resources/money.jpg")
        resized_photo = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_photo)
        label1 = components.Label(frame, image=photo)
        label1.image = photo 
        label1.pack()
    except Exception as e:
        print(f"Error loading image: {e}")

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

    button_frame = gui.Frame(frame)
    button_frame.pack()

    style.configure(
        "Custom.TButton",
        font=("Quicksand", 10, "bold"),
        width=32,
        padding=3,
        foreground="black",
        background="green",
    )
    
    style.configure(
        "Custom1.TButton",
        font=("Quicksand", 10, "bold"),
        width=32,
        padding=3,
        foreground="red",
        background="green",
    )

    button = components.Button(
        button_frame,
        text=f"{section}",
        style="Custom.TButton",
        command=lambda: transaction_redirect(transaction, accId),
    )
    button_exit = components.Button(
        button_frame,
        text="Back",
        style="Custom1.TButton",
        command = lambda: back(accId) 
    )
    
    button.pack()
    button_exit.pack(pady=10)

    label_frame = gui.Frame()
    label_frame.pack(pady=25)

    style.configure(
        "Label",
        foreground="blue",
    )

    system_result_label = components.Label(
        label_frame, text="", font=("Quicksand", 10, "bold"), style="Label"
    )
    result_label = components.Label(label_frame, text="", font=("Quicksand", 10))

    system_result_label.pack(side="left")
    result_label.pack(side="left")

    frame.mainloop()
