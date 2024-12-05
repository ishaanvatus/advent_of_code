# part 1
with open("input", "r") as f:
    lines = [line.strip().split() for line in f]
n = len(lines)
left = [int(lines[i][0]) for i in range(0, n)]
right = [int(lines[i][1]) for i in range(0, n)]
left.sort()
right.sort()
distance = 0
for i in range(0, n):
    distance += abs(left[i] - right[i])
print(distance)

# part 2
similarity = 0
for target in left:
    weight = 0
    for duplicate in right:
        if (target == duplicate):
            weight += 1
    similarity += target*weight
print(similarity)

