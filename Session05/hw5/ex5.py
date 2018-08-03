prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}

total = 0
for key in prices:
    value = prices[key] * stock[key]
    print(key,"\nprices:",prices[key], "\nstock:",stock[key],"\nvalue:",value )
    total += value
print("Total = {}".format(total))
