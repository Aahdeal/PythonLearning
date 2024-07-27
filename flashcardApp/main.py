from tkinter import *
import random
import pandas
from pandas import *

# ----------------- CONSTANTS ----------------- #
BACKGROUND_COLOR = "#B1DDC6"

# -----------------DATA FRAME------------------ #
data = pandas.read_csv("./data/french_words.csv")
data = data.to_dict()
# ----------------- ADD CARD ------------------ #
french = [word for word in data["French"].values()]
english = [word for word in data["English"].values()]

index = [random.randint(0, len(english)-1) for _ in range(len(english))]
count = 0
correct = []
incorrect = []
timer = ''

def nextCard():
    global count
    for items in img.find_withtag("text"):
        img.delete(items)
    if count < len(french):
        img.create_text(400, 186, text="French", font=("Arial", 20, "italic"), fill='black', tags="text")
        img.create_text(400, 262, text=french[index[count]], font=("Arial", 35, "bold"), fill='black', tags="text")
        flipCard()
    else:
        img.create_text(400, 186, text="Complete", font=("Arial", 20, "italic"), fill='black', tags="text")
        img.create_text(400, 262, text=f"Your Score: {len(correct)}", font=("Arial", 35, "bold"), fill='black', tags="text")


def backCard():
    global count
    for items in img.find_withtag("text"):
        img.delete(items)
    img.create_text(400, 186, text="English", font=("Arial", 20, "italic"), fill='black', tags="text")
    img.create_text(400, 262, text=english[index[count]], font=("Arial", 35, "bold"), fill='black', tags="text")


def flipCard():
    global timer
    timer = window.after(5000, backCard)

def yes_on_click(event):
    global timer
    global count
    window.after_cancel(timer)
    if count < len(french):
        correct.append(french[index[count]])
        count += 1
        nextCard()

def no_click(event):
    global timer
    global count
    window.after_cancel(timer)
    if count < len(french):
        incorrect.append(french[index[count]])
        count+=1
        nextCard()

# ------------------- UI FRONT CARD ---------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

img = Canvas(window, width=800, height=524, highlightthickness=0, bg=BACKGROUND_COLOR)
file = PhotoImage(file='./images/card_front.png')
img.create_image(400,262, image=file)
title = "Hello"
word = "Press the check to start"
img.create_text(400, 186, text=title, font=("Arial", 20, "italic"), fill='black', tags="text")
img.create_text(400, 262, text=word, font=("Arial", 35, "bold"), fill='black', tags="text")
img.grid(column=0, row=0, columnspan=2)

rightImg = Canvas(window, width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
fileright = PhotoImage(file='./images/right.png')
rightImg.create_image(50,50, image=fileright)
rightImg.bind("<Button-1>", yes_on_click)
rightImg.grid(column=0, row=3)

wrongImg = Canvas(window, width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
filewrong = PhotoImage(file='./images/wrong.png')
wrongImg.create_image(50,50, image=filewrong)
wrongImg.bind("<Button-1>", no_click)
wrongImg.grid(column=1, row=3)

nextCard()

window.mainloop()
