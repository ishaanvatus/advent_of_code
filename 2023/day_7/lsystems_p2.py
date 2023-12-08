from math import lcm
lines = ""
with open("input", "r") as fp:
    lines = fp.readlines()
rule = lines[0]
rule = rule.strip()
rule_len = len(rule)
raws = lines[2::]
rule = rule.replace('L', '0')
rule = rule.replace('R', '1')
print("rule")

instructions = dict()

for raw in raws:
    raw = raw.replace('=', '')
    raw = raw.replace(', ', ',')
    key, val = raw.split()
    val = val.replace('(', '')
    val = val.replace(')', '')
    val = val.split(',')
    instructions[key] = val

nodes = [key for key, val in instructions.items() if key[2] == 'A']
print(nodes)

steps = 0
all_steps = []
for node in nodes:
    steps = 0
    current_instruction = node
    while (current_instruction[2] != 'Z'):
        current_instruction = instructions[current_instruction][int(rule[steps%rule_len])]
        steps = (steps + 1)
    all_steps.append(steps)
print(lcm(*all_steps))
