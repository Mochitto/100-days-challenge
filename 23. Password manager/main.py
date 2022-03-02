# Password manager - to keep your secrets (kindaaa) safe.
#
#
import tkinter as tk
from tkinter import messagebox

import pyperclip

from password_generator import generator

# ---------------------------- PASSWORD BUTTON METHODS ------------------------------- #
counter = 10
timer = ""


def clear():
    """Clear the L_message and reset clipboard."""
    pyperclip.copy("")
    L_message.config(text="")


def count_down():
    """Count down from 10 to 0 in the L_message."""
    global counter, timer
    if counter > 0:
        L_message.config(text=f"Password copied! Clipboard reset in {counter}.")
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
            E_password.delete(0, "end")
            E_password.insert("end", string=password)
            count_down()
            win.destroy()
        except ValueError:
            messagebox.showerror(title="Error", message="Please make sure to use an integer.")

    # ---------------------------- Pop-up window ---------------------------- #
    win = tk.Toplevel(bg=BACKGROUND_COLOR, padx=20, pady=20)
    win.wm_title("Password generator")

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
    """Ask for confirmation and append password to txt."""
    website = E_website.get()
    user = E_user.get()
    password = E_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {user} "
                                                              f"\nPassword: {password} \nDo you want to save them?")

        if is_ok:
            with open("Passwords.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                E_user.delete(0, "end")
                E_password.delete(0, "end")
                E_website.delete(0, "end")


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
E_website = tk.Entry(width=45, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                     fg=BACKGROUND_COLOR)
E_website.grid(column=1, columnspan=2, row=1)

E_user = tk.Entry(width=45, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                  fg=BACKGROUND_COLOR)
E_user.grid(column=1, columnspan=2, row=2)

E_password = tk.Entry(width=30, bg=ENTRY_BUTTON_BG, justify="center", font=ENTRY_FONT, highlightthickness=0,
                      fg=BACKGROUND_COLOR)
E_password.grid(column=1, row=3)

# **************** Buttons ****************
B_password = tk.Button(text="Generate password", font=BUTTON_FONT, bg=ENTRY_BUTTON_BG, fg=BACKGROUND_COLOR,
                       highlightthickness=0, height=1, pady=1, padx=0, command=password_button)
B_password.grid(column=2, row=3)
B_add = tk.Button(text="Save", font=BUTTON_FONT, bg=ENTRY_BUTTON_BG, fg=BACKGROUND_COLOR,
                  highlightthickness=0, height=1, pady=1, padx=2, width=51, command=save)
B_add.grid(columnspan=2, row=4, column=1)

# Main Loop
window.mainloop()
