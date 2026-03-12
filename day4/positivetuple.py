class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x >= 0:
                pos_numbers.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls, pos_numbers)
        instance._skipped = skipped
        return instance


pos_n = PositiveTuple(9, 6, 22, 5, 0, -3, -45, 13, 46, 79, -64, -2, 6, -99)
print(type(pos_n))  # <class '__main__.PositiveTuple'>
print(pos_n)  # (9, 6, 22, 5, 0, 13, 46, 79, 6)
print(pos_n._skipped)  # 5
