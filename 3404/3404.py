messages = {
    "Obese": lambda x: x >= 30,
    "Underweight": lambda x: x < 18.5,
    "Normal": lambda x: x < 25,
    "Overweight": lambda x: x < 30,
}

weight = int(input())
height = float(input())
bmi = weight / (height * height)

print(round(bmi, 2))
for msg, func in messages.items():
    if func(bmi):
        print(msg)
        break

# Todo: FIX
