import smtplib
import datetime as dt
import random

my_email = "your_email@gmail.com"
password = "Your_password"

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivation\n\n{quote}")

# import smtplib
#
# my_email = "your_email@gmail.com"
# password = "your_password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="reciever_email@gmail.com",
#         msg="Subject:Hello\n\n This is the body of the email.")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=2002, month=3, day=25)
# print(date_of_birth)