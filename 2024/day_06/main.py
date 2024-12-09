import os
def save_map(map, name):
    width = len(map[0])
    height = len(map)
    palette = {'.': "255 255 255\n", '#': "0 0 0\n", '^': "0 255 0\n", '*': "64 64 128\n"}
    image = open(f"{name}.ppm", "w")
    image.write(f"P3\n{width} {height}\n255\n")
    for row, level in enumerate(map):
        for col, tile in enumerate(level):
            image.write(palette[tile[0]])
    image.close()
    os.system(f"magick {name}.ppm -interpolate Nearest -filter point -resize 1920x1920 {name}.png")
    os.system(f"rm {name}.ppm")
with open("input", "r") as f:
    lab = [[ch for ch in line.strip()] for line in f.readlines()]
save_map(lab, "before")
