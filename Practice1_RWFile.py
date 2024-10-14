class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        string = file.read()
        file.close()
        return string

    def add(self, *products):
        product_existing = self.get_products()
        for product in products:
            if product.__str__() in product_existing:
                print(f'Product {product.name} does already exist')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product.__str__}\n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())