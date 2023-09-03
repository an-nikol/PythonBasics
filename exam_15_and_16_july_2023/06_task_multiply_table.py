number = int(input())

num_to_str = str(number)

n1 = int(num_to_str[0])
n2 = int(num_to_str[1])
n3 = int(num_to_str[2])

for i in range(1, n3 + 1):
    for j in range(1, n2 + 1):
        for k in range(1, n1 + 1):
            summ = i * j * k
            print(f"{i} * {j} * {k} = {summ}")
