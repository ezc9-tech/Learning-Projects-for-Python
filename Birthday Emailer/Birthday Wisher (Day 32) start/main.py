import smtplib

my_email = "chapmanzane21@gmail.com"
password = "anniebug66"

new_connection = smtplib.SMTP("smtp.gmail.com")
new_connection.starttls()
new_connection.login(user=my_email, password=password)
new_connection.sendmail(from_addr=my_email, to_addrs="ezc9@outlook.com", msg="hello")
new_connection.close()