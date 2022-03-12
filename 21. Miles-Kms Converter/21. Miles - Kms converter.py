# Converts Miles into Kms
import tkinter as tk


def CalculateKM():
    """Convert the user_input to Kilometers and update the resut label."""
    if user_input.get().isdigit() or user_input.get().replace(".", "").isdecimal():
        kilometers = round(float(user_input.get()) * 1.609344, 2)
        result.config(text=str(kilometers))
    else:
        result.config(text="Error")


# Window
window = tk.Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(pady=10, padx=10)

# User input
user_input = tk.Entry(width=10)
user_input.grid(column=1, row=0)

# Labeles
Miles_label = tk.Label(text="Miles")
Miles_label.config(padx=10)
Miles_label.grid(column=2, row=0)

Kilometers_label = tk.Label(text="Km")
Kilometers_label.config(padx=10)
Kilometers_label.grid(column=2, row=1)

is_equal_to = tk.Label(text="is equal to")
is_equal_to.config(padx=10)
is_equal_to.grid(column=0, row=1)

result = tk.Label(text="0")
result.grid(column=1, row=1)

# Button
Calculate = tk.Button(text="Calculate", width=5, command=CalculateKM)
Calculate.grid(column=1, row=3)

window.mainloop()
