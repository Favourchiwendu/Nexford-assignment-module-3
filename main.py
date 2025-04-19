from policyholder import Policyholder
from product import Product
from payment import Payment

# Create a product
life_insurance = Product("Life Insurance", 50000)

# Update product price and suspend it
life_insurance.update_price(72000)
life_insurance.suspend_product()

# Reactivate it later
life_insurance.activate_product()

# Create policyholders and register them
favour = Policyholder("Nnamani Favour", "FHD123")
favour.register()

ernest = Policyholder("Udeh Ernest", "PHD124")
ernest.register()

# Create payments and demonstrate penalty + reminder
payment1 = Payment(65000)
payment1.send_reminder()
payment1.apply_penalty(10000)

payment2 = Payment(12000)

# Link products and payments
favour.add_product(life_insurance)
favour.add_payment(payment1)

ernest.add_product(life_insurance)
ernest.add_payment(payment2)

# Suspend and reactivate a policyholder
favour.suspend()
favour.reactivate()

# Display policyholder details
favour.display_info()
ernest.display_info()
