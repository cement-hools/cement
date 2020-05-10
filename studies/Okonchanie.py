n = 1

def ending(n):
    if 0 <= n <= 1000:
        if 11 <= n % 100 <= 19:
            print(n, 'программистов')
        elif n % 10 == 1:
            print(n, 'программист')
        elif 2 <= n % 10 < 5:
            print(n, 'программиста')
        elif n % 10 >= 5 or n % 10 == 0:
            print(n, 'программистов')



'''for i in range(0, 1001):
    ending(i)'''