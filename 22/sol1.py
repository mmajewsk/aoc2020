
data = open("input.txt", "r").read().splitlines()
p1 = []
p2 = []
breakline = False
for d in data:
    if d == '':
        breakline = True
        continue
    if 'Player' in d:
        continue
    if not breakline:
        p1.append(d)
    else:
        p2.append(d)

def play_game(p1,p2):
    a = p1.pop(0)
    b = p2.pop(0)
    a = int(a)
    b = int(b)
    assert a!=b
    print("Player 1 plays: {}".format(a))
    print("Player 2 plays: {}".format(b))
    if a>b:
        print("P1 wins", str(a), " > ", str(b))
        p1.append(a)
        p1.append(b)
    if b>a:
        print("P2 wins", str(a), " < ", str(b))
        p2.append(b)
        p2.append(a)
    return p1, p2

print(p1)
print(p2)
print()
print()
for i in range(3000):
    print("Round ", i)
    print("Player 1's deck: ", ','.join(str(x) for x in p1))
    print("Player 2's deck: ", ','.join(str(x) for x in p2))
    p1, p2 = play_game(p1,p2)
    if p1 and not p2:
        print("p1 wins")
        win = p1
        break

    if p2 and not p1:
        print("p2 wins")
        win = p2
        break

together = list(zip(win, reversed(range(1,len(win)+1))))
slist = [k*l for k,l in together]
print(sum(slist))

print()
print(p1)
print(p2)
