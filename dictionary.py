""" pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
} """

""" print(pizza['name'])

pizza['name'] = input()

print(pizza['name'])

print(pizza.get('toppings', []))

print(pizza.keys())

print(pizza.values()) """

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70
}

for price in products.values():
    print(price)

for product in products.keys():
    print(product)

for item in products.items():
    print(item)

for product, price in products.items():
    products[product] = round(price * 0.8)
    
print(products)

for product in enumerate(products):
    print(product)

for index, product in enumerate(products):
    print(index, product)

for index, product in enumerate(products.items(), 1):
    print(index, product)