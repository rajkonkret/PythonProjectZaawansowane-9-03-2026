import time


def liczby():
    wynik = []
    for i in range(31):
        wynik.append(i)

    return wynik


print(liczby())


def genliczby():
    for i in range(31):
        yield i


print(genliczby())  # <generator object genliczby at 0x000001AC35548FB0>
print(list(genliczby()))

for p in genliczby():
    print(p)
    # time.sleep(1)

gen = genliczby()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# StopIterations

def wznowienie(n, k):
    print("wstrzymanie działania")
    yield 3005

    print("wstrzymanie działania 1")

    print("wznowienie działania 1")
    yield n + k

    print("wznowienie działanie 2")

    print("wstrzymanie działanie 2")
    n = 8 * k - 4
    yield n - k

    print("wznowienie działanie 3")

    print("wstrzymanie działanie 3")
    yield n * k

    print("wznowienie działanie 4")

    print("wstrzymanie działanie 4")

    yield n / k
    print("wznowienie działanie 5")


print(wznowienie(8, 4))
print(list(wznowienie(8, 4)))


# wstrzymanie działania
# wstrzymanie działania 1
# wznowienie działania 1
# wznowienie działanie 2
# wstrzymanie działanie 2
# wznowienie działanie 3
# wstrzymanie działanie 3
# wznowienie działanie 4
# wstrzymanie działanie 4
# wznowienie działanie 5
# [3005, 12, 24, 112, 7.0]

def gene2():
    n = 1
    while True:
        result = yield n
        print(result)
        if result == "stop":
            break
        n += 1
        print(n)
        print(50 * "-")


g2 = gene2()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
g2.send("OK")

print(next(g2))
try:
    g2.send("stop")
except StopIteration:
    print('Koniec danych')


# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\PythonProjectZaawansowane-9-03-2026\day2\generatory.py", line 99, in <module>
#     g2.send("stop")
#     ~~~~~~~^^^^^^^^
# StopIteration
# Koniec danych

def sengen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x + 1
        else:
            x = 3 * y


g = sengen()
print("_" * 60)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(122))
print(next(g))
print(next(g))
print(g.send(15))
print(next(g))
print(g.send("a"))
# 3 367
# 368
# 45
# 46
# aaa
print(next(g))
# TypeError: can only concatenate str (not "int") to str
