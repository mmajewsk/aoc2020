
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
        p1.append(int(d))
    else:
        p2.append(int(d))
from functools import lru_cache

@lru_cache(maxsize=None)
def play_game(p1,p2, subgame=0):
    played_games=[]
    while p1 and p2:
        a = p1[0]
        b = p2[0]
        a = int(a)
        b = int(b)
        p1 = p1[1:]
        p2 = p2[1:]
        assert a!=b
        if False:
            if subgame != 0:
                print("SUBGAME ", str(subgame))
            print("Player 1's deck: ", ','.join(str(x) for x in p1))
            print("Player 2's deck: ", ','.join(str(x) for x in p2))
            print("Player 1 plays: {}".format(a))
            print("Player 2 plays: {}".format(b))
        if str((p1,p2)) in played_games:
            # print("win by repetition")
            # print( str((p1,p2)), "in", str(played_games ))
            return "p1", tuple(p1) ,tuple(p2)
        else:
            played_games.append(str((p1,p2)))
            if a <=len(p1) and b<=len(p2):
                px = p1[:a]
                py = p2[:b]
                winner, _, _ = play_game(px, py, subgame=subgame-1)
            elif a>b:
                winner = "p1"
            elif b>a:
                winner = "p2"
            if winner == 'p1':
                # print("P1 wins", str(a), " vs ", str(b))
                p1 += (a, b)
            elif winner == 'p2':
                p2 += (b, a)
                # print("P2 wins", str(a), " vs ", str(b))
            else:
                print("Error")
                print(winner, a,b, p1, p2)
                raise ValueError
    # print("win otherwise")
    if p1 and not p2:
        return 'p1', tuple(p1) , tuple(p2)

    if p2 and not p1:
        return 'p2', tuple(p1) , tuple(p2)

print()
print()

winner, p1, p2 = play_game(tuple(p1), tuple(p2))
if winner == 'p1':
    win = p1

if winner == 'p2':
    win = p2
together = list(zip(win, reversed(range(1,len(win)+1))))
slist = [k*l for k,l in together]
print(sum(slist))

print()
print(p1)
print(p2)
