# models.py
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def get_username(self):
        return self.__username

    def verify_password(self, password):
        return self.__password == password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def verify_password(self, password):
        return password == "admin123" or super().verify_password(password)

class Product:
    def __init__(self, name, price, category, image):
        self.name = name
        self.price = price
        self.category = category
        self.image = image

    def __add__(self, other):
        return self.price + other.price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
# models.py

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if isinstance(item, list):
            self.items.extend(item)
        else:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_cart(self):
        return self.items

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

