##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas

MY_EMAIL = "tttttttest4234@gmail.com"
MY_PASSWORD = "247235823jsdfkj"

# Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# If true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy Birthday!\n\n{contents}"
    )



