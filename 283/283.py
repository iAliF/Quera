a, b = (int(input()) for _ in range(2))  # Inputs

if a <= b:
    print("Wrong order!")
    exit()

if (diff := (a - b)) % 2 != 0:
    print("Wrong difference!")
    exit()

x = diff // 2
star_line = ("* " * a)[:-1]
sq_line = ("* " * x) + (" " * 2 * b) + ("* " * x)[:-1]

for i in range(1, a + 1):
    if i <= x or x + b < i <= a:
        print(star_line)
    else:
        print(sq_line)
