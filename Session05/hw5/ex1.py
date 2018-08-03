inventory = {
    'gold': 500,
    'pouch': ['flint','twine','gemstone'],
    'backpack': ['xylophone','dagger','bedroll','bread loaf']
}

#add key pocket 
inventory['pocket'] = ['seashell','strange berry','lint']
#remove "dagger"
inventory['backpack'].remove('dagger')
#add 50
inventory['gold'] += 50
#print
print(inventory)
