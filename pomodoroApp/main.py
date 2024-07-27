from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
global RESET

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global RESET
    RESET = True
    img.itemconfig(timer_config, text="0:0", fill='white', font=(FONT_NAME, 35))
    count.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global RESET
    RESET = False
    window.iconify()
    sprint = 0
    countdownWORK(WORK_MIN*60, sprint)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdownWORK(total_sec,sprint):
    heading.config(text="STUDY")
    if total_sec > 0 and not RESET:
        minutes = int(total_sec // 60)
        seconds = int(total_sec % 60)
        img.itemconfig(timer_config, text=f"{minutes}:{seconds}", fill='white', font=(FONT_NAME, 35))
        window.after(1000, countdownWORK, total_sec - 1, sprint)
    elif total_sec == 0 and not RESET and sprint <= 4:
        sprint += 1
        text = ''
        for i in range(0, sprint):
            text = f"{text}✅"
        count.config(text=text)
        img.itemconfig(timer_config, text="0:0", fill='white', font=(FONT_NAME, 35))
        countdownBREAK(SHORT_BREAK_MIN*60, sprint)
        if sprint == 4:
            longBREAK(LONG_BREAK_MIN*60)

def countdownBREAK(break_sec, sprint):
    heading.config(text="BREAK TIME")
    window.deiconify()
    if break_sec > 0 and not RESET and sprint != 4:
        minutes = int(break_sec // 60)
        seconds = int(break_sec % 60)
        img.itemconfig(timer_config, text=f"{minutes}:{seconds}", fill='white', font=(FONT_NAME, 35))
        window.after(1000, countdownBREAK, break_sec - 1, sprint)
    if break_sec == 0 and not RESET:
        img.itemconfig(timer_config, text="0:0", fill='white', font=(FONT_NAME, 35))
        window.after(1000, countdownWORK, WORK_MIN*60, sprint)


def longBREAK(long_break_sec):
    heading.config(text="BREAK TIME")
    window.deiconify()
    if long_break_sec > 0 and not RESET:
        minutes = int(long_break_sec // 60)
        seconds = int(long_break_sec % 60)
        img.itemconfig(timer_config, text=f"{minutes}:{seconds}", fill='white', font=(FONT_NAME, 35))
        window.after(1000, longBREAK, long_break_sec - 1)
    if long_break_sec == 0 and not RESET:
        img.itemconfig(timer_config, text="0:0", fill='white', font=(FONT_NAME, 35))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
img = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
timg= PhotoImage(file="tomato.png")
img.create_image(100, 112, image=timg)
img.grid(column=1, row=1)
timer_config = img.create_text(100, 130, text="", fill="white", font=("FONT_NAME",35, "bold"))

heading = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
heading.grid(column=1, row=0)

start = Button(text="Start", font=(FONT_NAME, 12), command=startTimer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 12), command=reset, highlightthickness=0)
reset.grid(column=2, row=2)

count = Label(text="", bg=YELLOW)
count.grid(column=1, row=4)

window.mainloop()