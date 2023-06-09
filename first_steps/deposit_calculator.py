deposit_sum = float(input())
deposit_date = int(input())
deposit_year_interest = float(input())

total_interest = deposit_sum * deposit_year_interest / 100
interest_month = total_interest / 12
total_sum = deposit_sum + deposit_date * interest_month
print(total_sum)
