#################################
#
#Author: Jordi Garcia Altadill
#Date: 07-02-2020
#
#Script that obtain the total cost for Lamps & Wallets
#
#################################
import json

#Function that returns the prices for a single variant
def sum_cost(variant):
	variant_price = variant["price"]
	return variant_price


#Function that returns an array with all the prices for every products
def calculate_cost(feed):

	product_cost = 0

	#Obtain the evet type from each element.
	product = feed["product_type"]
	
	if (product == "Wallet") or (product == "Lamp"):
		product_cost = sum(map(sum_cost,feed["variants"]))
	
	return product_cost




#Load the JSON. Now is hardoceded but can come from an HTTP call.
json_feed = json.loads('{"products": [{"title": "Small Rubber Wallet", "product_type": "Wallet","variants": [{ "title": "Blue", "price": 29.33 },{ "title": "Turquoise", "price": 18.50 }]}, {"title": "Sleek Cotton Shoes","product_type": "Shoes","variants": [{ "title": "Sky Blue", "price": 20.00 }]},{"title": "Lamp1", "product_type": "Lamp","variants": [{ "title": "Blue", "price": 100.33 },{ "title": "Turquoise", "price": 8.50 },{ "title": "Orange", "price": 21.50 }]}]}')



cost = sum(map(calculate_cost,json_feed["products"]))

print "The total cost is: "+ str(cost)







