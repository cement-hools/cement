class MoneyBox:
    def __init__(self, capacity, coin=0):
        self.capacity = capacity # конструктор с аргументом – вместимость копилки
        self.coin = coin
    def can_add(self, v):
        if self.capacity <= v:
            return True
        else:
            return False # True, если можно добавить v монет, False иначе
    def add(self, v):
        if self.can_add(v):
            self.coin += v
            self.capacity -= v
        # положить v монет в копилку

class Buffer:
    def __init__(self, base=[]):
    # конструктор без аргументов
        self.base = base
    def add(self, *a):
    # добавить следующую часть последовательности
        for i in a:
            self.base.append(i)
            if len(self.base) == 5:
                print(sum(self.base))
                self.base = []
    def get_current_part(self):
    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.base

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            list.append(self, x) #Аналог super().append(x)
            print('В список добавилось:', x, 'Список выглядит:', self)
        else:
            raise NonPositiveError('Мое Исключение')
    def __iadd__(self, y):  # для унарного плюса
        self.append(y)
        return self


w = PositiveList()

w.append(1)
w.append(12)
w.append(0)

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)

y = Buffer()
y.add(1,2,3)
y.add(4, 5, 6)
y.add(7, 8, 9, 10)
print(y.get_current_part())
y.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(y.get_current_part())