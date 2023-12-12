lines = []
with open("input", "r") as fp:
    lines = fp.readlines()

records = []
for line in lines:
    cleaned = line.replace('\n', '').split()
    size = cleaned[1]
    size = list(map(int, size.split(',')))
    cleaned[0] = cleaned[0].replace('#', '1')
    cleaned[0] = cleaned[0].replace('.', '0')
    record = [cleaned[0], size]
    records.append(record)
max = -1
for record in records:
    count = record[0].count('?')
    if count > max:
        max = count
print(max)
