# read user input
user_name = input()
password = input()

# logic
current_password = input()
while current_password != password:
    current_password = input()

# print output
print(f'Welcome {user_name}!')



# scond  version
# while True:
    #current_password = input()
    #if current_password == password:
    #break
#print
