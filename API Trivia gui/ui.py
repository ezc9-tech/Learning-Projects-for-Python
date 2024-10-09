from tkinter import *
from quiz_brain import QuizBrain
Font = ("Arial", 20, "italic")
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.window.title("API Quiz")

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white" )
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=Font, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.yes_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\API Trivia gui\images\true.png")
        self.yes = Button(image=self.yes_image, bg=THEME_COLOR, highlightthickness=0)
        self.yes.grid(row=2, column=0)

        self.no_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\API Trivia gui\images\false.png")
        self.no = Button(image=self.no_image, bg=THEME_COLOR, highlightthickness=0)
        self.no.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

