# 1
class Shakllar:
    def yuza(self, a, b):
        return a * b

    def perimetr(self, a, b):
        return 2 * (a + b)

s = Shakllar()
print(s.yuza(4, 5))
print(s.perimetr(4, 5))


# 2
class Doira:
    pass

d = Doira()
print(isinstance(d, Doira))


# 3
class Kalkulyator:
    def qoshish(self, a, b):
        return a + b

k = Kalkulyator()
print(k.qoshish(3, 7))


# 4
class Maxfiy:
    def __init__(self):
        self.__sir = 'yashirin'

    def sir_ol(self):
        return self.__sir

m = Maxfiy()
print(m.sir_ol())


# 5
class Avtomobil:
    davlat = "O'zbekiston"

a1 = Avtomobil()
a2 = Avtomobil()
a1.davlat = 'Rossiya'
print(a1.davlat)
print(a2.davlat)



# 6
class Doira:
    def __init__(self, r):
        self.r = r

    def yuza(self):
        return 3.14 * self.r ** 2

d = Doira(3)
print(d.yuza())
