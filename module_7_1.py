class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        with open(self.__file_name, 'r') as file:
            existing_products = file.readlines()
        existing_names = set(line.split(',')[0].strip() for line in existing_products)
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product}\n')
                    existing_names.add(product.name)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
