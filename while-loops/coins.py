change = float(input())
coins = 0
rest = 0
# Coins: 2 BGB, 1 BGN, 0.5 BGN, 0.2 BGN, 0.1 BGN, 0.05 BGN, 0.02 BGN, 0.01 BGN
rest = change // 2
if rest > 0:
    coins += rest
    change -= rest * 2
    change = round(change, 2)
rest = change // 1
if rest > 0:
    coins += rest
    change -= rest
    change = round(change, 2)
rest = change // 0.5
if rest > 0:
    coins += rest
    change -= rest * 0.5
    change = round(change, 2)
rest = change // 0.2
if rest > 0:
    coins += rest
    change -= rest * 0.2
    change = round(change, 2)
rest = change // 0.1
if rest > 0:
    coins += rest
    change -= rest * 0.1
    change = round(change, 2)
rest = change // 0.05
if rest > 0:
    coins += rest
    change -= rest * 0.05
    change = round(change, 2)
rest = change // 0.02
if rest > 0:
    coins += rest
    change -= rest * 0.02
    change = round(change, 2)
rest = change // 0.01
if rest > 0:
    coins += rest
    change -= rest * 0.01
    change = round(change, 2)
print(int(coins))
