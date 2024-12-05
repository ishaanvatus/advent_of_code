import re
with open("input", "r") as f:
    memory = f.read()
pattern = re.compile(r'(mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\))')
matches = pattern.finditer(memory)
sum_p1 = 0
sum_p2 = 0
disabled = False
for match in matches:
    #print(match)
    start = match.start()
    end = match.end()
    ins = memory[start:end]
    if (ins == 'don\'t()'):
        disabled = True
        break;
    elif (ins == 'do()'):
        disabled = False
        continue
    p1 = re.compile(r'[0-9]+\,')
    num1_match = p1.finditer(ins)
    p2 = re.compile(r'\,[0-9]+')
    num2_match = p2.finditer(ins)
    num1 = 0
    num2 = 0
    for thing in num1_match:
        num1 = int(ins[thing.start():(thing.end() - 1)])
    for thing in num2_match:
        num2 = int(ins[(thing.start() + 1):thing.end()])
    sum_p1 += num1*num2
    if (not disabled):
        sum_p2 += num1*num2
print(f"Part 1: {sum_p1}")
print(f"Part 2: {sum_p2}")
