
try:
    a = float(input())
    b = float(input())
except ZeroDivisionError:
    print("Please don't divide by zero")
except ValueError:
    print("Please input real numb")
else:
    print(a / b)
finally:
    print('end of the programm')