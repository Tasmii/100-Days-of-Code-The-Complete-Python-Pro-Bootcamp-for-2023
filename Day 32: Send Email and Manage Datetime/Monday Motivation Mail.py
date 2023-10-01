import smtplib
import datetime as dt
import random

my_mail = "girllucky680@gmail.com"
password = "waqpxwohvpensuxg"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open(r"Day 32 Send Email and Manage DateTime\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, 
                            to_addrs="shivanshmishradpsmbd@gmail.com", 
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                        )
    #connection.close()
