#x1 + x2 + x3 = n

n = int(input())
combination_count = 0
flag = False

for a in range(0, n + 1):
    for b in range(0, n + 1):
        for c in range(0, n + 1):
            if a + b + c == n:
                combination_count += 1

print(combination_count)
