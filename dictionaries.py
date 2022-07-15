from itertools import product


product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "First_name": "ryan",
    "last_name": "ray"
}

print(type(product))
#print(dir(person))

print(person.keys())#obtiene las llaves
print(person.values())#obtiene los valores

print(person.items())#obtiene los items

person.clear()
print(person)

products = [
    {"name": 'book', "price":  10.99},
    {"name": 'book', "price": 100.00},
]