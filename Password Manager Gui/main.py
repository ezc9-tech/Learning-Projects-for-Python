from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list= []

    for number in range(1,12):
        password_list.append(random.choice(letters))

    for number in range(1,2):
        password_list.append(random.choice(numbers))

    for number in range(1):
        password_list.append(random.choice(symbols))

    password_returned = ""
    random.shuffle(password_list)

    for char in password_list:
        password_returned += char

    password_text.insert(index=0, string=password_returned)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    password_content = password_text.get()
    website_content = website_text.get()
    email_content = email_text.get()
    new_data = {
        website_content: {
            "email": email_content,
            "password": password_content,
        }
    }

    if len(password_content) == 0 or len(website_content) == 0 or len(email_content) == 0:
        messagebox.showerror(title="Error", message="One or more entries is empty.")

    else:
        is_ok = messagebox.askyesno(title="Are you sure?", message=f"Are you sure these are the details:"
                                        f"\n{website_content}\n{email_content}\n{password_content}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    website_text.delete(0, END)
                    password_text.delete(0, END)
            except JSONDecodeError or FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

                    website_text.delete(0, END)
                    password_text.delete(0, END)
#----------------------------- Search ---------------------------------#
def search():
    website_content = website_text.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website_content in data:
                password_content = data[website_content]["password"]
                messagebox.showinfo(title="Password Detected", message=f"{website_content}'s password is:\n{password_content}")
            else:
                messagebox.showerror(title="Not Found", message="No details for the website exists.")
    except JSONDecodeError or FileNotFoundError:
        messagebox.showerror(title="File not found", message="No data file found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

#put your image file path into the photo image
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2)

website_button = Button(text="Search", command=search)
website_button.grid(column=3, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_text = Entry(width=35)
email_text.insert(0, "ezc9@outlook.com")
email_text.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_text = Entry(width=21)
password_text.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command= add)
add_button.grid(column=1, row=4, columnspan=2,)

window.mainloop()