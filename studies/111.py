# объявление функции
def is_password_good(password):
    title = 0
    low = 0
    digit = 0
    if len(password) > 7:
        for i in password:
            if i.isdigit() or i.isalpha():
                if i.isdigit():
                    digit += 1
                if i.istitle():
                    title += 1
                if i.islower():
                    low += 1

            else: return False
        print(title, low, digit)
        if title > 0 and low > 0 and digit > 0:
            return True
        else:
            return False

    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))