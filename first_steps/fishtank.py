distance = int(input())
width = int(input())
height = int(input())
percent = float(input())

v_aquarium = distance * width * height
v_litters = v_aquarium * 0.001
busy = v_litters * 0.17

total = v_litters - busy
print(total)
