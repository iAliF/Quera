l = {1, 2, 3, 4}


def find(num1, num2, num3):
    return list(l - {num1, num2, num3})[0]
