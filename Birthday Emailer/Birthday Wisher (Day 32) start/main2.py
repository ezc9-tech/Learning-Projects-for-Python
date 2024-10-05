##################### Extra Hard Starting Project ######################
import smtplib
from datetime import datetime
import random
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)
my_email = "chapmanzane21@gmail.com"
password = "mikr gaej inwf ejrc"  # Use App Password if 2FA is enabled

data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}
print(new_dict)

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    letter_templates = [r"C:\Users\ezc9\OneDrive\Documents\GitHub\Learning-Projects-for-Python\Birthday Emailer\letter_templates\letter_1.txt",
                        r"C:\Users\ezc9\OneDrive\Documents\GitHub\Learning-Projects-for-Python\Birthday Emailer\letter_templates\letter_2.txt",
                        r"C:\Users\ezc9\OneDrive\Documents\GitHub\Learning-Projects-for-Python\Birthday Emailer\letter_templates\letter_3.txt"]
    letter_choice = random.choice(letter_templates)
    with open(letter_choice) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=password)
        new_connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=contents)
        print("Email sent successfully!")



