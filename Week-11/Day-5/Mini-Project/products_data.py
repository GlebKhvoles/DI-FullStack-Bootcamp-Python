import json
def retrieve_all_products():
	with open('products.json', 'r') as p:
		return json.load(p)


def retrieve_requested_product(product_id):
	requested_products = retrieve_all_products()
	for product in requested_products:
		if product['ProductId'] == product_id:
			return product

