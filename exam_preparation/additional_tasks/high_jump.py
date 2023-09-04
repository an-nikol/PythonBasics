target_high_jump = int(input())

current_high_jump = target_high_jump - 30
unsuccessful_jumps = 0
jumps_counter = 0

while unsuccessful_jumps < 3:
    jump = int(input())

    jumps_counter += 1

    if jump > current_high_jump:
        unsuccessful_jumps = 0
        current_high_jump += 5

        if current_high_jump > target_high_jump:
            print(f"Tihomir succeeded, he jumped over {target_high_jump}cm after {jumps_counter} jumps.")
            break

    else:
        unsuccessful_jumps += 1

else:
    print(f"Tihomir failed at {current_high_jump}cm after {jumps_counter} jumps.")

