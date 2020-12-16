food = ["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


for i in food:
	if bakery_stock.get(i) != None:
		print(f"{bakery_stock[i]} left")
	else:
		print("We don't make that")
		
	