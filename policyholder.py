class Policyholder:
    # Constructor method to initialize a Policyholder object with name, id_number, and default status and lists for products and payments
    def __init__(self, name, id_number):
        self.name = name          # Assigning the name of the policyholder
        self.id_number = id_number  # Assigning the unique ID number of the policyholder
        self.status = "Active"     # Default status is "Active"
        self.products = []         # List to store the products associated with the policyholder
        self.payments = []         # List to store the payments made by the policyholder

    # Method to register the policyholder, printing a message confirming their registration
    def register(self):
        print(f"{self.name} (ID: {self.id_number}) has been registered.")

    # Method to suspend the policyholder, changing their status to "Suspended"
    def suspend(self):
        self.status = "Suspended"

    # Method to reactivate the policyholder, changing their status back to "Active"
    def reactivate(self):
        self.status = "Active"

    # Method to add a product to the policyholder's list of products
    def add_product(self, product):
        self.products.append(product)

    # Method to add a payment to the policyholder's list of payments
    def add_payment(self, payment):
        self.payments.append(payment)

    # Method to display the policyholder's information including name, ID, status, products, and payments
    def display_info(self):
        # Print the basic info of the policyholder
        print(f"\nPolicyholder: {self.name} (ID: {self.id_number})")
        print(f"Status: {self.status}")
        
        # Print details of the products associated with the policyholder
        print("Products:")
        for product in self.products:
            print(f" : {product.name} (${product.price}) | Active: {product.active}")
        
        # Print details of the payments made by the policyholder
        print("Payments:")
        for payment in self.payments:
            print(f" : ${payment.amount} on {payment.date}")
