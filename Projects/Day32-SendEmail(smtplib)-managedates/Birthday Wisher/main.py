#CHECK SECURITY SETTINGS FIRST
import smtplib
import datetime as dt
import random

my_email = "newemail@gmail.com"
my_password = "12345abcd"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    #with smtplib.SMTP("smtp.gmail.com") as connection:
        #connection.starttls()
        #connection.login(my_email, my_password)
        #connection.sendmail(
            #from_addr=my_email,
            #to_addrs=my_email,
            #msg=f"Subject:Monday Motivation\n\n{quote}"
        #)
