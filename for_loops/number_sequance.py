n = int(input())

min_value = int(input())
max_value = min_value

for i in range(n-1):
    num = int(input())
    if num < min_value:
        min_value = num
    elif num > max_value:
        max_value = num

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')
