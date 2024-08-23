class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.file_name = 'products.txt'

    def get_products(self):
        file = open(self.file_name, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        existing_products = set()

        file = open(self.file_name, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()

        for line in lines:
            existing_products.add(line.strip().split(',')[0])

        file = open(self.file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
                existing_products.add(product.name)

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())