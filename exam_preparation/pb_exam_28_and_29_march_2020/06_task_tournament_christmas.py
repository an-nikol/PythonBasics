number_of_days = int(input())

total_profit = 0

total_won_games = 0
total_lost_games = 0


for day in range(1, number_of_days + 1):
    current_profit = 0
    current_won_games = 0
    current_lost_games = 0
    while True:
        name_of_game = input()

        if name_of_game == 'Finish':
            break

        game_output = input()
        if game_output == 'win':
            current_profit += 20
            current_won_games += 1
            total_won_games += 1
        elif game_output == 'lose':
            current_lost_games += 1
            total_lost_games += 1

    if current_won_games > current_lost_games:
        current_profit *= 1.10
        total_profit += current_profit
    else:
        total_profit += current_profit

if total_won_games > total_lost_games:
    total_profit += total_profit * 0.20
    print(f'You won the tournament! Total raised money: {total_profit:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_profit:.2f}')
