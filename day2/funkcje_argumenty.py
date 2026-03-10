from os import name


def all_params(a, b, /, c=10, *args, d=90, **kwargs):
    print(f"{a=}, {b=}, {c=}, {d=}")
    print(args)
    print(kwargs)


# all_params()
all_params(1, 2, 3, 4, 5, 6)
all_params(1, 2, 3, 4, 5, 6, a=10)

# ()
# {}
# (1, 2, 3, 4, 5, 6)
# {}
# (1, 2, 3, 4, 5, 6)
# {'a': 10}

# (3, 4, 5, 6)
# {'a': 10}
all_params(1, 2, 3)
all_params(1, 2, c=3)
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9)
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, d=12)
# a=1, b=2, c=3, d=12
# (4, 5, 6, 7, 8, 9)
# {}
all_params(1, 2, 3, 4, 5, 6, 7, 8, 9, d=12, e=99, name='Radek')
# a=1, b=2, c=3, d=12
# (4, 5, 6, 7, 8, 9)
# {'e': 99, 'name': 'Radek'}

age = 90
print("Radek:", age)  # Radek: 90
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
