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
        # Function Call
        basic_transaction_process(transaction, accId)
    else:
        # Function Call
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
                resultset = connection.search(
                    f"SELECT * FROM `balance` WHERE `accId` = '{accId}'"
                )
                balance = resultset[0][1]  # current_balance
                balance = int(balance)

                if amount > balance:
                    system_result_label.config(text="SYSTEM:")
                    result_label.config(text="Insufficient Funds")
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
    transfer_user = transfer_input_id.get()
    if not transfer_user.isdigit():
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="Enter a valid user ID")
        return

    recId = int(transfer_user)  # transfer user ID variable

    transfer_amount = input_amount.get()
    if not transfer_amount.isdigit():
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="Enter a valid amount of money")
        return

    amount = int(transfer_amount)  # amount variable
    if amount == 0:
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="Money value can't be zero")
        return

    if recId == accId:
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="You can't send money to yourself")
        return

    # Fetch balances
    rec_balance_result = connection.search(
        f"SELECT `balance` FROM `balance` WHERE `accId` = '{recId}'"
    )
    sender_balance_result = connection.search(
        f"SELECT `balance` FROM `balance` WHERE `accId` = '{accId}'"
    )

    if not rec_balance_result or not sender_balance_result:
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="No user exists with that ID")
        return

    rec_balance = rec_balance_result[0][0]
    sender_balance = sender_balance_result[0][0]

    rec_balance = int(rec_balance)  # recBalance
    sender_balance = int(sender_balance)  # senderBalance

    if amount > sender_balance:
        system_result_label.config(text="SYSTEM:")
        result_label.config(text="Insufficient funds")
        return

    rec_new_balance = rec_balance + amount
    sender_new_balance = sender_balance - amount

    # Update Query
    connection.iud(
        f"UPDATE `balance` SET `balance` = '{rec_new_balance}' WHERE `accId` = '{recId}'"
    )
    connection.iud(
        f"UPDATE `balance` SET `balance` = '{sender_new_balance}' WHERE `accId` = '{accId}'"
    )

    # Log the transaction
    connection.iud(
        f"INSERT INTO `transfers` (`senderId`, `recieverId`, `amount`) VALUES ('{accId}', '{recId}', '{amount}')"
    )

    input_amount.delete(0, "end")
    transfer_input_id.delete(0, "end")
    system_result_label.config(text="SYSTEM:")
    result_label.config(text="Money transferred successfully")


# Main, Create Frame
def create_frame(section, transaction, accId):
    global frame
    global \
        system_result_label, \
        result_label, \
        input_amount, \
        transfer_input_id, \
        transfer_input_label

    frame = gui.Tk()
    style = components.Style()

    frame.title("Ami Bank App")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)

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

    # input labels
    if transaction == "transfer":
        # transfer input label
        transfer_input_label = components.Label(
            frame,
            text="Enter the Recieving account ID",
            font=("Quicksand", "11"),
            anchor="w",
        )
        transfer_input_id = components.Entry(
            frame, width=33, font=("Quicksand", 11), justify="left"
        )
        transfer_input_label.pack(pady=10)
        transfer_input_id.pack()

    else:
        print("F")

    input_label = components.Label(
        frame,
        text=f"How much money would you like to {transaction}?",
        font=("Quicksand", "11"),
        anchor="w",
    )

    input_amount = components.Entry(
        frame, width=33, font=("Quicksand", 11), justify="left"
    )
    input_label.pack(pady=(15, 10))
    input_amount.pack(pady=(0, 10))

    # buttons
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
        button_frame, text="Back", style="Custom1.TButton", command=lambda: back(accId)
    )

    button.pack()
    button_exit.pack(pady=15)

    # info label
    label_frame = gui.Frame()
    label_frame.pack(pady=15)

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
