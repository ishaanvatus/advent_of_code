import re
with open("input", "r") as f:
    word_arr = [
            [ch for ch in line.strip()]
            for line in f.readlines()
            ]
pattern = 'XMAS'
width = len(word_arr[0])
height = len(word_arr)
n = len(pattern)
word_count = 0
directions = [
        [0, 1], #horizontal forwards
        [0, -1], #horizontal backwards
        [1, 0], #vertical downwards
        [-1, 0], #vertical upwards
        [1, 1], #diagonally right downwards
        [1, -1], #diagonally right upwards
        [-1, 1], #diagonally left downwards
        [-1, -1] #diagonally left upwards
        ]
for row, line in enumerate(word_arr):
    for col, ch in enumerate(line):
        for direction in directions:
            candy = ""
            for index in range(0, n):
                x = row + index*direction[0]
                y = col + index*direction[1]
                if not ((0 <= x < width) and (0 <= y < height)):
                    break
                candy += word_arr[x][y]
            if (candy == pattern):
                word_count += 1
print(word_count)
