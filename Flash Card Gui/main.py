from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
ENGLISH_FONT = ("Ariel", 40, "italic")
FRENCH_FONT = ("Ariel", 60, "bold")

#-------------------------- User Interface -----------------------------#
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\card_front.png")
card_image2 = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\card_back.png")
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card.create_image(400, 263, image=card_image)
card.create_text(400, 150, text="French", fill="black", font=ENGLISH_FONT)
card.create_text(400, 263, text="trouve", fill="black", font=FRENCH_FONT)
card.grid(column=0, row=0, columnspan=2)


no_button_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\wrong.png")
no_button = Button(image=no_button_image, highlightthickness=0)
no_button.grid(column=0, row=1)

yes_button_image = PhotoImage(file= r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Flash Card Gui\images\right.png")
yes_button = Button(image= yes_button_image, highlightthickness=0)
yes_button.grid(column= 1, row= 1)

window.mainloop()

