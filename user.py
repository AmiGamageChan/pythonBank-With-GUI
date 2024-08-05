import tkinter as gui
from tkinter import ttk as components  # Some components
from PIL import Image, ImageTk
import connection as con

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
    user = resultset[0][1] #Username

    frame.title(f"Welcome {user}")
    frame.geometry("400x570")
    frame.resizable(width=False, height=False)

    frame.protocol("WM_DELETE_WINDOW", quit_application)
    
    frame.mainloop()


def main(accId):
    user_screen(accId)
    
main(1)
