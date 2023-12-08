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

current_instruction = 'AAA'

steps = 0
while (current_instruction != 'ZZZ'):
    current_instruction = instructions[current_instruction][int(rule[steps%rule_len])]
    steps = (steps + 1)
print(steps)
