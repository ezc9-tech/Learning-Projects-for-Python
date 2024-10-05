from tkinter import *
import pandas

blue = "#21abcd"
title_font = ("Ariel", 24, "bold")
sub_font = ("Ariel", 16, "bold")

window = Tk()
window.config(padx=50, pady= 50, bg=blue)
window.title("Money Manager")

#---------------------------------Adding Money----------------------------#
monthly_money = 0.0
money = 0
expenses = 0.0
month_value = ""
data = {"January": [0, 0],
        "February": [0, 0],
        "March": [0, 0],
        "April": [0, 0],
        "May": [0, 0],
        "June": [0, 0],
        "July": [0, 0],
        "August": [0, 0],
        "September": [0, 0],
        "October": [0, 0],
        "November": [0, 0],
        "December": [0, 0]}
file = pandas.DataFrame(data)
rows = file.iterrows()
print(rows)

def add_money():
    global monthly_money, file, money
    monthly_money = float(income_grabber.get())
    money += monthly_money
    total_money.config(text=f"Total Money: ${money}")
    if month_value in file.columns:
        file.at[0, month_value] = monthly_money
    print(file)


def subtract_money():
    global monthly_money, expenses, money
    expenses = float(expense_grabber.get())
    money -= expenses
    total_money.config(text=f"Total Money: ${money}")
    if month_value in file.columns:
        file.at[1, month_value] = -expenses
    print(file)
        

def get_month():
    global month_value, monthly_money, expenses
    monthly_money = 0
    expenses = 0
    month_value = root.get()




#-------------------------------------UI----------------------------------#

#title
title = Label(text="Money Manager", fg="white", bg=blue, highlightthickness=0, font=title_font)
title.grid(row=0, column=1)

#what month is it
month_title = Label(text="Month:" , fg= "white", bg=blue, highlightthickness=0, font= sub_font)
month_title.grid(row=1)
options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
root = StringVar(window)
root.set(options[0])
month = OptionMenu(window, root, *options,)
month.grid(row=1, column =1)
month_button = Button(text="Submit", command=get_month)
month_button.grid(row=1, column = 2)


#Monthly income grabber
income_title = Label(text="Monthly Income:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
income_title.grid(row=2, column=0)
income_grabber = Entry(width=40)
income_grabber.grid(row=2, column=1)
income_button = Button(text="Submit", command=add_money)
income_button.grid(row=2, column=2)

#Expence grabber
expense_title = Label(text="Expenses:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
expense_title.grid(row=3, column=0)
expense_grabber = Entry(width=40)
expense_grabber.grid(row=3, column=1)
expense_button = Button(text="Submit", command=subtract_money)
expense_button.grid(row=3, column=2)

#Total Money printer
total_money = Label(text=f"Total Money: ${money}", bg=blue, fg="white", highlightthickness=0, font=sub_font)
total_money.grid(row=4, column=1)

#Monthly Money printer
monthly_money_printer = Label(text=f"Monthly Money Remaining: {monthly_money}", bg=blue, fg="white", highlightthickness=0, font=sub_font)
monthly_money_printer.grid(row=5, column=1)






window.mainloop()