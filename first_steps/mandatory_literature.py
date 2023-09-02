pages_in_book = int(input())
pages_read_hour = int(input())
days_to_read_book = int(input())

total_time_reading = pages_in_book / pages_read_hour
reading_hours_per_day = total_time_reading / days_to_read_book
print(round(reading_hours_per_day))
