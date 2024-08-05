from pprint import pprint


class Product:
    name = str
    weight = float
    category = str
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self, name, weight, category):
        return print(f'{name},{weight},{category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        file = open(__file_name, 'a')
        file.write(products)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
