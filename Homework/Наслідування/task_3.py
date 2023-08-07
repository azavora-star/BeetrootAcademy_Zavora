# Product Store

# Write a class Product that has three attributes:

#     type
#     name
#     price

# Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

# Also, the ProductStore class must have the following methods:

#     add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
#     set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). 
#     The discount must be specified in percentage
#     sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. 
#     It also increments income if the sell_product method succeeds.
#     get_income() - returns amount of many earned by ProductStore instance.
#     get_all_products() - returns information about all available products in the store.
#     get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self,product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        # if this product is not in the store yet
        if product.name not in self.products:
            self.products[product.name] = {"product_type": product.product_type, "price": product.price * 1.3, "amount": amount}

        # if this product is already in the store
        else:
            self.products[product.name]["amount"] += amount

    def set_discount(self, identifier, percent, identifier_type):
        if identifier_type == 'name':
            self.products[identifier]["price"] =  self.products[identifier]["price"] * (1 - percent / 100)
        
        if identifier_type == 'type':
            for product in self.products:
                if self.products[product]["product_type"] == identifier:
                    self.products[product]["price"] =  self.products[product]["price"] * (1 - percent / 100)    




p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Running Shoes', 100)

s = ProductStore()
s.add(p1, 20)
s.add(p2, 500)
s.add(p3, 150)

s.set_discount('Sport', 15 , 'type')

#s.add(product1, 25)
print(s.products)

# s.add(p2, 300)

# s.sell('Ramen', 10)

# assert s.get_product_info('Ramen') == ('Ramen', 290)