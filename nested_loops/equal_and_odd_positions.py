first_num = int(input())
second_num = int(input())


for number in range(first_num, second_num + 1):
    even_sum = 0
    odd_sum = 0
    number_to_str = str(number)

    for index in range(len(number_to_str)):
        if index % 2 == 0:
            even_sum += int(number_to_str[index])
        else:
            odd_sum += int(number_to_str[index])

    if even_sum == odd_sum:
        print(number, end=' ')
