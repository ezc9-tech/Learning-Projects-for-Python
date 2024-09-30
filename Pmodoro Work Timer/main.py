from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    counter(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, counter, count -1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx= 100, pady= 50, bg= YELLOW)
window.title("Pomodoro")


timer_text = Label(text="Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 35, "bold"))
timer_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness= 0)
tomato = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Pmodoro Work Timer\tomato.png")
canvas.create_image(100, 112, image= tomato)
timer = canvas.create_text(100, 130, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start = Button(text="Start", bg= YELLOW, highlightthickness= 0, command=start_timer)
start.grid(row=2,column=0)

reset = Button(text= "Reset", bg= YELLOW, highlightthickness= 0)
reset.grid(row=2,column=2)

check_marks = Label(text= "✓", fg=GREEN, bg= YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()