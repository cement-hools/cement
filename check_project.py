from Dev.hw_python_oop.homework import *
import datetime as dt

a1 = Record(amount=1186, comment="Кусок тортика. И ещё один.")
a2 = Record(amount=84, comment="Йогурт.")
a3 = Record(amount=1140, comment="Баночка чипсов.", date="01.07.2020")
w = CaloriesCalculator(2000)
w.add_record(a1)
w.add_record(a2)
w.add_record(a3)
print(w.records)
print(w.get_calories_remained())
print(w.get_today_stats())
print(w.get_week_stats())
b1 = Record(amount=1186, comment="Кусок тортика. И ещё один.")
b2 = Record(amount=84, comment="Йогурт.")
b3 = Record(amount=1140, comment="Баночка чипсов.", date="01.07.2020")
q = CashCalculator(1000)
q.add_record(b1)
q.add_record(b2)
q.add_record(b3)
print(q.records)
print(q.get_today_stats())
print(q.get_week_stats())
print(q.get_today_cash_remained('eur'))
print(q.get_today_cash_remained('rub'))
print(q.get_today_cash_remained('usd'))

# USD_RATE = 71.19
# EURO_RATE = 80.62
# RUB_RATE = 1
# currencies = {
#     'eur': ('Euro', EURO_RATE),
#     'usd': ('USD', USD_RATE),
#     'rub': ('руб', RUB_RATE),
# }
#
# print(currencies['eur'][0])
