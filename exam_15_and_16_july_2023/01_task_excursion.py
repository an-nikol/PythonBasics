number_of_people = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_cards = int(input())

price_per_night = 20
card_for_transport = 1.60
card_for_museum = 6

price_nights = number_of_nights * price_per_night
cards_transport_price = card_for_transport * number_of_transport_cards
card_for_museum_price = card_for_museum * number_of_museum_cards

total_for_one_person = price_nights + cards_transport_price + card_for_museum_price

total_for_everyone = number_of_people * total_for_one_person

sum_after_discount = total_for_everyone + (total_for_everyone * 0.25)

print(f'{sum_after_discount:.2f}')
