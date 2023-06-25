
'''Compute the total price of the stock where the total price is the sum of the price of an itemmultiplied by the quantity of this exact item.'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_amount = 0

for qty in stock.keys():
  for price in prices.keys():
    if qty == price:
      total_amount += stock.get(qty) * prices.get(price)
print(total_amount)