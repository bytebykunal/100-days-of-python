import smtplib
import datetime as dt
import random

my_email = "your_email@example.com"
password = "your_app_password"

now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 3:
    with open("quotes.txt") as file:
        quotes = file.readlines()


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kunal.dsdev@yahoo.com",
                            msg=f"Subject:Thursday Motivation\n\n{random.choice(quotes)}"
        )



