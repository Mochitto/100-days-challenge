# Password manager - to keep your secrets (kindaaa) safe.
#
#
import tkinter as tk
from tkinter import messagebox
import json

import pyperclip

from password_generator import generator

# ---------------------------- PASSWORD BUTTON METHODS ------------------------------- #
counter = 10
timer = ""


def clear():
    """Clear the L_message and reset clipboard."""
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    pyperclip.copy("")
    L_message.config(text="")


def count_down():
    """Count down from 10 to 0 in the L_message."""
    global counter, timer
    if counter > 0:
        L_message.config(text=f"Password copied! Clipboard reset in {counter}.", fg=FONT_FG)
        counter -= 1
        timer = window.after(1000, count_down)
    else:
        clear()


def password_button():
    """Create a pop-up window to get the length of the password."""
    global timer, counter
    if timer:
        window.after_cancel(timer)
        L_message.config(text="")
        pyperclip.copy("")
        counter = 10

    def create_passsword():
        """Generate password and insert in E_password, call count_down and close pop_up window."""
        try:
            password = generator(int(E_length.get()))
        except ValueError:
            messagebox.showerror(title="Error", message="Please make sure you are using a positive integer.")
        else:
            E_password.delete(0, "end")
            E_password.insert("end", string=password)
            count_down()
            win.destroy()

    # ---------------------------- Pop-up window ---------------------------- #
    win = tk.Toplevel(bg=BACKGROUND_COLOR, padx=20, pady=20)
    win.wm_title("Password generator")
    win.attributes("-topmost", True)

    # **************** Lables ****************
    L_length = tk.Label(win, text="Length of your password: ", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=5)
    L_length.grid(row=0, column=0)

    # **************** Entries ****************
    E_length = tk.Entry(win, bg=ENTRY_BUTTON_BG, justify="center", font=BUTTON_FONT, highlightthickness=0,
                        fg=BACKGROUND_COLOR, width=5)
    E_length.grid(row=0, column=1)
    E_length.focus()

    # **************** Buttons ****************
    B_ok = tk.Button(win, text="Generate", command=create_passsword, font=BUTTON_FONT, bg=ENTRY_BUTTON_BG,
                     fg=BACKGROUND_COLOR, highlightthickness=0, height=1, pady=1, padx=2, width=10)
    B_ok.grid(row=2, column=0, columnspan=2)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save password to a json file."""
    website = E_website.get()
    user = E_user.get()
    password = E_password.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        clear()
        L_message.config(text="Password added!", fg="#9bdeac")
        window.after(2000, clear)
        try:
            with open("Passwords.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("Passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("Passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        E_user.delete(0, "end")
        E_password.delete(0, "end")
        E_website.delete(0, "end")


def load():
    """Load the password from the database and insert it in the entries."""
    entry = E_website.get()
    try:
        with open("Passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Password.json not found.")
        return None
    try:
        E_user.delete(0, "end")
        E_user.insert("end", data[entry]["email"])
        E_password.delete(0, "end")
        E_password.insert("end", data[entry]["password"])
    except KeyError:
        messagebox.showerror(title="Error", message=f"No entry called \"{entry}\" was found.")
        return None


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()

# **************** CONSTANTS ****************
X_LOGO = 200
Y_LOGO = 193

BACKGROUND_COLOR = "#1e2021"
FONT_FG = "#d4483b"
ENTRY_BUTTON_BG = "#c97878"

LABEL_FONT = ("Courier", 13, "bold")
ENTRY_FONT = ("Script", 10, "bold")
BUTTON_FONT = ("Script", 9, "bold")

# **************** Window's settings ****************
window.minsize(int(X_LOGO * 2.5), int(Y_LOGO * 2))
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
window.title("Password Manager")

# **************** Image ****************
canvas = tk.Canvas(width=X_LOGO, height=Y_LOGO, bg=BACKGROUND_COLOR, highlightthickness=0)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(X_LOGO // 2, Y_LOGO // 2, image=image)
canvas.grid(column=1, row=0)

# **************** Labels ****************
L_website = tk.Label(text="Website/Name:", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=5)
L_website.grid(column=0, row=1)

L_user = tk.Label(text="Email/Username:", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=5)
L_user.grid(column=0, row=2)

L_password = tk.Label(text="Password:", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=5)
L_password.grid(column=0, row=3)

L_add = tk.Label(text="", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=5)
L_add.grid(column=0, row=4)

L_message = tk.Label(text="", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=FONT_FG, pady=10)
L_message.grid(column=0, columnspan=3, row=5)

# **************** Entries ****************
E_website = tk.Entry(width=30, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                     fg=BACKGROUND_COLOR)
E_website.grid(column=1, row=1)

E_user = tk.Entry(width=45, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                  fg=BACKGROUND_COLOR)
E_user.grid(column=1, columnspan=2, row=2)

E_password = tk.Entry(width=30, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                      fg=BACKGROUND_COLOR)
E_password.grid(column=1, row=3)

# **************** Buttons ****************
B_website = tk.Button(text="Search", font=BUTTON_FONT, bg=ENTRY_BUTTON_BG, fg=BACKGROUND_COLOR,
                      highlightthickness=0, height=1, pady=1, padx=0, command=load, width=17)
B_website.grid(column=2, row=1)
B_password = tk.Button(text="Generate password", font=BUTTON_FONT, bg=ENTRY_BUTTON_BG, fg=BACKGROUND_COLOR,
                       highlightthickness=0, height=1, pady=1, padx=2, command=password_button)
B_password.grid(column=2, row=3)
B_add = tk.Button(text="Save", font=BUTTON_FONT, bg=ENTRY_BUTTON_BG, fg=BACKGROUND_COLOR,
                  highlightthickness=0, height=1, pady=1, padx=2, width=51, command=save)
B_add.grid(columnspan=2, row=4, column=1)

# Main Loop
window.mainloop()
