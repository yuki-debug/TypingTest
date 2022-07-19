import tkinter as tk
import requests
import time

# -------GLOBAL VARS----------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
global o_text, start_time, stop_time


# ---------------FUNCTIONS-----------
def get_text():
    global o_text, start_time
    start_time = time.perf_counter()
    data = requests.get(url="http://metaphorpsum.com/sentences/1")
    o_text = data.text
    typing_text.config(text=o_text)
    textbox.delete("1.0", "end")
    textbox.focus_set()


def submit(event=None):
    title_label.focus_set()
    global o_text, stop_time
    stop_time = time.perf_counter()
    input_text = textbox.get("1.0", "end-1c")
    compare(input_text)


def compare(input_text):
    count = 0
    space_count = 0
    in_len = len(input_text)
    o_len = len(o_text)
    if in_len > o_len:
        in_len = o_len
    for n in range(in_len - 1):
        if o_text[n] == input_text[n]:
            count += 1
    for n in range(o_len):
        if o_text[n] == " ":
            space_count += 1
    display(o_len, count, space_count)


def display(o_len, count, space_count):
    global start_time, stop_time
    minutes = (stop_time - start_time) / 60
    accuracy = (count / o_len) * 100
    words = space_count + 1
    result_per.config(text=f"Accuracy: {round(accuracy)}")
    result_wpm.config(text=f"wpm: {round(words / minutes)}")


# --------------LAYOUT--------------
window = tk.Tk()
window.title("Typing Test")
window.config(background=YELLOW)

window.bind('<Return>', submit)

title_label = tk.Label(text="Typing Test", fg=GREEN, bg=YELLOW, font=("Comic Sans MS", 50))
title_label.grid(row=0, column=0, columnspan=3)

typing_text = tk.Label(text="press start to get started", fg="black", bg=YELLOW, font=(FONT_NAME, 16)
                       , padx=5, pady=5)
typing_text.grid(row=1, column=0, columnspan=3, padx=5, pady=20)

textbox = tk.Text(window, height=5, width=50, padx=5, pady=5)
textbox.config(font=(FONT_NAME, 16))
textbox.grid(row=3, column=0, columnspan=3, pady=15, padx=20)

submit_button = tk.Button(text="Submit", command=submit, padx=50, pady=5)
submit_button.grid(row=4, column=2)

start_button = tk.Button(text="Start", command=get_text, padx=50, pady=5)
start_button.grid(row=4, column=0)

result_per = tk.Label(font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg="grey")
result_per.grid(row=5, column=0, pady=15)

result_wpm = tk.Label(font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg="grey")
result_wpm.grid(row=5, column=1, pady=15)

window.mainloop()
