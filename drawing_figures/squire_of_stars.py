number = int(input())

for row in range(1, number + 1):
    if row == 1 or number == row:
        print("+ " + (number - 2) * "- " + "+ ")
    else:
        print("| " + (number - 2) * "- " + "| ")


#n = int(input())

#print('+ ' + '- ' * (n - 2) + '+ ')

#for row in range(n - 2):
    #print('| ' + '- ' * (n - 2) + '| ')

#print('+ ' + '- ' * (n - 2) + '+ ')
