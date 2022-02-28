import tkinter as tk
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CYCLES = 4


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global Timer, work, reps
    window.after_cancel(Timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0
    work = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0
work = 0


def start_timer():
    global reps, timer_text, work
    reps += 1
    check_marks.config(text="✓" * work)

    if reps % (CYCLES * 2) == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Grab a coffe!")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break!")
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Work!")
        work += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
Timer = ""


def count_down(count):
    global Timer
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        Timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

title = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=RED)
title.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(text="", bg=PINK, fg=RED, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
