import os
import smtplib
import datetime as dt
import random

qu_list = []
my_email = "EMAIL"
password = "naaawlaxbitpohtq"

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", "r") as file:
    for line in file.readlines():
        qu_list.append(line)

motive_quote = random.choice(qu_list)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if day_of_week == 2:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="TTetw90@gmail.com",
            msg=f"Subject:motivation\n\n{motive_quote}"
        )

