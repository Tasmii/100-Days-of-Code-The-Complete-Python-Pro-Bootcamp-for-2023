#import smtplib
#my_mail = ""
#password = ""
#
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_mail, password=password)
#    connection.sendmail(from_addr=my_mail, 
#                        to_addrs="shivanshmishradpsmbd@gmail.com", 
#                        msg="Subject:Hello\n\nThis is the body of the email.")
##connection.close()

#import datetime as Dt
#now = Dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(day_of_week)

#Birthday Wisher App
from datetime import datetime
import pandas
import random
import smtplib

my_mail = ""
password = ""
today= (datetime.now().month, datetime.now().day)
data = pandas.read_csv(r"Day 32 Send Email and Manage DateTime\birthdays.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day 32 Send Email and Manage DateTime\letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP()("smtp.gmail.com") as connection:
        connection.startls()
        connection.login(my_mail, password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
