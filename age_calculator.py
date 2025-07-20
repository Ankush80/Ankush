#Accurate age calculator
from datetime import datetime
from dateutil.relativedelta import relativedelta

y = int(input("Enter your year of birth: "))
m = int(input("Enter your month of birth: "))
d = int(input("Enter your day of birth: "))

try:
    birth_date = datetime(y, m, d)
    today = datetime.today()
    age = relativedelta(today, birth_date)
    print(f"You are {age.years} years, {age.months} months and {age.days} days old")
except:
    print("Invalid Input")