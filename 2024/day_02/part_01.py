with open("input", "r") as f:
    data = [list(map(int, line.strip().split())) for line in f]
diffs = []
for report in data:
    n = len(report)
    sub_diff = []
    for i in range(1, n):
        sub_diff.append(report[i] - report[i - 1])
    diffs.append(sub_diff)
## remove different signs
sign = 0
strict = []
for diff in diffs:
    if (diff[0] < 0):
        sign = 1
    else:
        sign = 0
    flag = True
    for num in diff:
        if sign:
            if (num > 0):
                flag = False
                break
        else:
            if (num < 0):
                flag = False
                break
    if flag:
        strict.append(diff)
safe = []
diffs = [list(map(abs, candy)) for candy in strict]
for diff in diffs:
    flag = True
    for num in diff:
        if ((num < 1) or (num > 3)):
            flag = False
            break
    if flag:
        safe.append(diff)
print(len(safe))
