from tkinter import *
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

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
data = {"Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "Monthly Income": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Food": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Utilities": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Travel": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Housing": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Debt": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Insurance": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }


def calculate():
    global monthly_money, money, expenses, month_value, data
    month_value = root.get()
    month_index = data["Month"].index(month_value)
    monthly_money = float(income_grabber.get())
    data["Monthly Income"][month_index] = f"${monthly_money}"
    food = float(food_grabber.get())
    data["Food"][month_index] = f"${food}"
    utilities = float(utilities_grabber.get())
    data["Utilities"][month_index] = f"${utilities}"
    travel = float(travel_grabber.get())
    data["Travel"][month_index] = f"${travel}"
    housing = float(housing_grabber.get())
    data["Housing"][month_index] = f"${housing}"
    debt = float(debt_grabber.get())
    data["Debt"][month_index] = f"${debt}"
    insurance = float(insurance_grabber.get())
    data["Insurance"][month_index] = f"${insurance}"
    data_dataframe = pandas.DataFrame(data)
    data_dataframe.to_csv("Money_Tracked.csv")
    expenses = food + utilities + travel + housing + debt + insurance
    money += monthly_money - expenses
    total_money.config(text=f"Total Money: ${money}")
    monthly_money_printer.config(text=f"Monthly Money Remaining: {monthly_money}")


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


#Monthly income grabber
income_title = Label(text="Monthly Income:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
income_title.grid(row=2, column=0)
income_grabber = Entry(width=40)
income_grabber.grid(row=2, column=1)


#Expence grabber
food_title = Label(text="Food and Groceries:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
food_title.grid(row=3, column=0)
food_grabber = Entry(width=40)
food_grabber.grid(row=3, column=1)


utilities_title = Label(text="Utilities:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
utilities_title.grid(row=4, column=0)
utilities_grabber = Entry(width=40)
utilities_grabber.grid(row=4, column=1)


travel_title = Label(text="Travel:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
travel_title.grid(row=5, column=0)
travel_grabber = Entry(width=40)
travel_grabber.grid(row=5, column=1)


housing_title = Label(text="Housing:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
housing_title.grid(row=6, column=0)
housing_grabber = Entry(width=40)
housing_grabber.grid(row=6, column=1)


insurance_title = Label(text="Insurance:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
insurance_title.grid(row=7, column=0)
insurance_grabber = Entry(width=40)
insurance_grabber.grid(row=7, column=1)


debt_title = Label(text="Debt:", fg="white", bg=blue, highlightthickness=0, font=sub_font)
debt_title.grid(row=8, column=0)
debt_grabber = Entry(width=40)
debt_grabber.grid(row=8, column=1)


debt_button = Button(text="Submit", command=calculate)
debt_button.grid(row=11, column=1)


#Total Money printer
total_money = Label(text=f"Total Money: ${money}", bg=blue, fg="white", highlightthickness=0, font=sub_font)
total_money.grid(row=10, column=1)


#Monthly Money printer
monthly_money_printer = Label(text=f"Monthly Money Remaining: {monthly_money}", bg=blue, fg="white", highlightthickness=0, font=sub_font)
monthly_money_printer.grid(row=9, column=1)


window.mainloop()