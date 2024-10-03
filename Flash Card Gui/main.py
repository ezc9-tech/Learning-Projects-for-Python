from tkinter import *
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"
ENGLISH_FONT = ("Ariel", 40, "italic")
FRENCH_FONT = ("Ariel", 60, "bold")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\data\french_words.csv")
to_learn = data.to_dict(orient="records")
word = {}


#-------------------------- Button Function ----------------------#
def skip_button_function():
    global word
    global timer
    window.after_cancel(timer)
    word = random.choice(to_learn)
    card.itemconfig(english, text="French", fill="black")
    card.itemconfig(french, text = word["French"], fill="black")
    card.itemconfig(card_background, image=card_image)
    timer = window.after(3000, func= flip_card)

def flip_card():
    global word
    card.itemconfig(english, text= "English", fill="white")
    card.itemconfig(french, text= word["English"], fill="white")
    card.itemconfig(card_background, image=card_image2)

def skip_button_function_check():
    to_learn.remove(word)
    wow = pandas.DataFrame(to_learn)
    wow.to_csv("data/words_to_learn")
    skip_button_function()






#-------------------------- User Interface -----------------------------#
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

card_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\card_front.png")
card_image2 = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\card_back.png")
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = card.create_image(400, 263, image=card_image)
english = card.create_text(400, 150, text="French", fill="black", font=ENGLISH_FONT)
french = card.create_text(400, 263, text="trouve", fill="black", font=FRENCH_FONT)
card.grid(column=0, row=0, columnspan=2)


no_button_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\wrong.png")
no_button = Button(image=no_button_image, highlightthickness=0, command = skip_button_function)
no_button.grid(column=0, row=1)

yes_button_image = PhotoImage(file= r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\right.png")
yes_button = Button(image= yes_button_image, highlightthickness=0, command= skip_button_function_check)
yes_button.grid(column= 1, row= 1)

skip_button_function()

window.mainloop()

