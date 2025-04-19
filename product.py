class Product:
    # Constructor method to initialize a Product object with a name, price, and default status (active)
    def __init__(self, name, price):
        self.name = name          # Assigning the name of the product
        self.price = price        # Assigning the price of the product
        self.active = True        # By default, the product is active

    # Method to update the product's price
    def update_price(self, new_price):
        self.price = new_price    # Updating the price with the new value
        print(f"Price for {self.name} updated to ${self.price}")

    # Method to suspend the product, making it inactive
    def suspend_product(self):
        self.active = False       # Marking the product as inactive
        print(f"{self.name} has been suspended.")

    # Method to reactivate the product, making it active again
    def activate_product(self):
        self.active = True        # Marking the product as active
        print(f"{self.name} has been reactivated.")