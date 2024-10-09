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

        self.score_count = 0
        self.score = Label(text=f"Score: {self.score_count}", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250, bg="white" )
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=Font, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.yes_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\API Trivia gui\images\true.png")
        self.yes = Button(image=self.yes_image, bg=THEME_COLOR, highlightthickness=0, command=self.true)
        self.yes.grid(row=2, column=0)

        self.no_image = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\API Trivia gui\images\false.png")
        self.no = Button(image=self.no_image, bg=THEME_COLOR, highlightthickness=0, command=self.false)
        self.no.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz!")
            self.yes.config(state="disabled")
            self.no.config(state="disabled")
    def true(self):
        self.feedback(self.quiz.check_answer("True"))


    def false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
            self.score_count += 1
            self.score.config(text=f"Score: {self.score_count}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
