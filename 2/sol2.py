data = open("input.txt", "r").read().splitlines()
correct = 0
for l in data:
    r, letter, pwd = l.split()[:3]
    letter = letter[:1]
    low, high = r.split("-")
    low, high = int(low), int(high)
    s = ""
    s += pwd[low - 1]
    s += pwd[high - 1]
    if s.count(letter) == 1:
        correct += 1

print(correct)
