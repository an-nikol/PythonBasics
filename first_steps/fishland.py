price_skum = float(input())
price_caca = float(input())
price_palam = (price_skum * 1.6)
price_safrid = (price_caca * 1.8)
price_midi = 7.50

palam_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

money = (palam_kg * price_palam + safrid_kg * price_safrid + midi_kg * price_midi)
print('%.2f'% money)
