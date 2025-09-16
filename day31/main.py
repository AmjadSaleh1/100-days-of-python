from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
try:
    data = pandas.read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data\\french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
current_card = {}


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=get_translate)


def get_translate():
    canvas.itemconfig(card, image=card_background)
    canvas.itemconfig(card_word, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])


def is_known():
    data_dict.remove(current_card)
    data1 = pandas.DataFrame(data_dict)
    data1.to_csv("data\\words_to_learn.csv", index=False)
    generate_word()


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, get_translate)

canvas = Canvas(width=800, height=526)
card_background = PhotoImage(file='images\\card_back.png')
card_front = PhotoImage(file='images\\card_front.png')
card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

right_img = PhotoImage(file='images\\right.png')
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file='images\\wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

generate_word()

window.mainloop()
