import smtplib
import datetime as dt
import random

my_email = "a.asmal101@gmail.com"
my_password = "gsnu wxlu syoj snvg"

with open("quotes.txt", "r") as f:
    quotes = f.read()
    quotes = quotes.split("\n")
    authors = [author.split(" - ", 1)[1] for author in quotes]
    f.close()

index = random.randint(0, len(authors) - 1)

date = dt.datetime.now()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if date.weekday() == 0:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='ilhaamwadee@gmail.com',
            msg=f"Subject: Mail from {authors[index]}\n\n{quotes[index]}"
        )
