data = open("input.txt", "r").read().splitlines()
correct = 0
for l in data:
    r, letter, pwd = l.split()[:3]
    letter = letter[:1]
    low, high = r.split("-")
    if int(low) <= pwd.count(letter) <= int(high):
        correct += 1

print(correct)
