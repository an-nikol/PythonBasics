price_tax_yearly = int(input())

price_basketball_shoes = price_tax_yearly - (price_tax_yearly * 0.40)
price_basketball_clothes = price_basketball_shoes - (price_basketball_shoes * 0.20)
price_basketball = 1/4 * price_basketball_clothes
price_basketball_accessoaries = 1/5 * price_basketball

result = price_basketball_shoes + price_basketball_clothes + price_basketball + price_basketball_accessoaries + price_tax_yearly
print(result)
