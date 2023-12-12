# read input
lines = []
with open("input", "r") as fp:
    lines = fp.readlines()
# format image and get dimensions
height = 0
image = []
for line in lines:
    arr = [char for char in line if char != '\n']
    image.append(arr)
    height += 1
width = len(image[0])
# count where the dead space is
empty_cols = []
empty_rows = []
for row in range(0, height):
    alien = False
    for col in range(0, width):
        if image[row][col].__eq__('#'):
            alien = True
            break;
    if not alien:
        empty_rows.append(row)
for col in range(0, width):
    alien = False
    for row in range(0, height):
        if image[row][col].__eq__('#'):
            alien = True
            break;
    if not alien:
        empty_cols.append(col)
for strip in image:
    print(strip)
print(f"height = {height}, width = {width}")
# pad image due to gravity expansion
map = [[ch for ch in row] for row in image]
for region in map:
    print(region)
row_pad = ['.' for row in range(0, height)]
print(row_pad)
for row in range(0, height):
    if (row in empty_rows):
        break;
    for col in range(0, width):
        if (col in empty_cols):
            map[row].insert(col + 1, '.')
for region in map:
    print(region)
