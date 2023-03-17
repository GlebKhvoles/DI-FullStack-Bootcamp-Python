from products_data import retrieve_all_products, retrieve_requested_product
from flask import Flask, render_template

app = Flask(__name__)
cart_items = []

@app.route("/")
def homepage():
	return render_template("homepage.html")

@app.route("/products")
def products():
	products = retrieve_all_products()
	return render_template("products.html", products=products)

@app.route("/products/<product_id>")
def product_info(product_id):
	product = retrieve_requested_product(product_id)
	return render_template("details.html", product=product)


@app.route("/cart")
def cart():
	return render_template("cart.html", cart_items=cart_items)

@app.route("/add_product_to_cart/<product_id>")
def add_product(product_id):
	cart_item = retrieve_requested_product(product_id)
	cart_items.append(cart_item)
	return render_template("cart.html", cart_items=cart_items)

@app.route("/delete_product_from_cart/<product_id>")
def del_product(product_id):
	for item in cart_items:
		if item["ProductId"] == product_id:
			cart_items.remove(item)
			break
	return render_template("cart.html", cart_items=cart_items)

app.run()