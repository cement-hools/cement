import datetime

print(datetime.datetime.now())
n = datetime.date(2016,4,20) # создали дату
d = datetime.timedelta(days=2)# дельта в 2 дня
w = n + d
print(n)
print(d)
print(w.year, w.month, w.day)