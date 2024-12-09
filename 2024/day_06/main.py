import os
import time
start = time.time()
def save_map(map, name):
    width = len(map[0])
    height = len(map)
    palette = {'.': "255 255 255\n", '#': "0 0 0\n", '^': "0 255 0\n", '*': "138 43 226\n"}
    image = open(f"{name}.ppm", "w")
    image.write(f"P3\n{width} {height}\n255\n")
    for row, level in enumerate(map):
        for col, tile in enumerate(level):
            image.write(palette[tile])
    image.close()
    os.system(f"magick {name}.ppm -interpolate Nearest -filter point -resize 1920x1920 {name}.bmp")
    os.system(f"rm {name}.ppm")
def right_turn(vector):
    vector = vector[1], -vector[0]
    return vector
with open("input", "r") as f:
    lab = [[ch for ch in line.strip()] for line in f.readlines()]
save_map(lab, "before")
for row, level in enumerate(lab):
    for col, tile in enumerate(level):
        if (tile == '^'):
            lab[row][col] = '*'
            guard_pos = [row, col]
cover = 1
direction = (-1, 0)
width = len(lab[0])
height = len(lab)
frame_number = 0
while (True):
    save_map(lab, f"./frames/{frame_number:03}")
    frame_number += 1
    x = guard_pos[0] + direction[0]
    y = guard_pos[1] + direction[1]
    #exit if out of bounds
    if not ((0 <= x < width) and (0 <= y < height)):
        break
    if lab[x][y] == '#':
        x -= direction[0]
        y -= direction[1]
        direction = right_turn(direction)
    if lab[x][y] == '*':
        cover -= 1
    cover += 1
    lab[x][y] = '*'
    guard_pos = [x, y]
save_map(lab, "after")
print(cover)
end = time.time()
print(end - start)
