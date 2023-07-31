lines = []

for i in range(1, 6):
    inp = input()
    if "HAFEZ" in inp or "MOLANA" in inp:
        lines.append(str(i))

print(" ".join(lines) if len(lines) > 0 else "NOT FOUND!")