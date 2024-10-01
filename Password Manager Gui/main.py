from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    password_content = password_text.get()
    website_content = website_text.get()
    email_content = email_text.get()
    with open("data.txt", "a") as file:
        file.write(f"{website_content} | {email_content} | {password_content}\n")
        password_text.delete(0, END)
        website_text.delete(0, END)
    file.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

logo = PhotoImage(file=r"C:\Users\ezc9\Documents\GitHub\Learning-Projects-for-Python\Password Manager Gui\logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_text = Entry(width=35)
email_text.insert(0, "ezc9@outlook.com")
email_text.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_text = Entry(width=21)
password_text.grid(column=1, row=3)

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, command= add)
add_button.grid(column=1, row=4, columnspan=2,)

window.mainloop()