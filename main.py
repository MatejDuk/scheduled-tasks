##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd
import os

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
day = today.day
month = today.month

if day in birthdays["day"].values and month in birthdays["month"].values:
    birthday_today = birthdays[(birthdays["day"]==day) & (birthdays["month"]==month)]
    for index,bt in birthday_today.iterrows():
        rnd_num = random.randint(1,3)
        letter = f"./letter_templates/letter_{rnd_num}.txt"
        with open(letter, "r") as f:
            ltr = f.read()
            ltr = ltr.replace("[NAME]",bt["name"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=bt["email"],
                                msg=f"HAPPY BIRTHDAY:Quote\n\n{ltr}")

# 4. Send the letter generated in step 3 to that person's email address.




