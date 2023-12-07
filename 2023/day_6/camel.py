def set_length(string):
    chars = set(string)
    char_arr = [ch for ch in string]
    max = -1;
    for char in chars:
        occurences = char_arr.count(char)
        if occurences > max:
            max = occurences;
    return max
def best_char(string):
    chars = set(string)
    shitking = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
    ranking = [str(elem) for elem in shitking]
    ranking = ranking[::-1]
    char = set(string)
    rank = -1
    for char in chars:
        tachiba = ranking.index(char)
        if tachiba > rank:
            rank = tachiba
    return rank
filename = input("input file? ")
lines = []
hands = []
with open(filename, "r") as fp:
    lines = fp.readlines()

for line in lines:
    val = line.split()
    hands.append([val[0], int(val[1])])

hands = sorted(hands, key=lambda x: set_length(x[0]))

bins = [[] for i in range(0, 6)]

for hand in hands:
    bins[set_length(hand[0])].append(hand)

for bin in bins:
    bin = sorted(bin, key = lambda x: best_char(x[0][0]))
    bin = sorted(bin, key = lambda x: best_char(x[0][1]))
    bin = sorted(bin, key = lambda x: best_char(x[0][2]))
    bin = sorted(bin, key = lambda x: best_char(x[0][3]))
    bin = sorted(bin, key = lambda x: best_char(x[0][4]))
for i, bin in enumerate(bins):
    print(f"bin {i}")
    for item in bin:
        print(item, end = " ")
    print()










