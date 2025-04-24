product = {}

while True:
    user_input = input () . strip()
    if user_input.lower() == "done":
        break
    prod_name, prod_price = user_input. split(",")
    prod_price = float(prod_price.strip())
    product[prod_name] = prod_price
for prod_name, prod_price in product.items ():
    print(f"{prod_name}: {prod_price}")