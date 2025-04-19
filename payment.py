from datetime import datetime

class Payment:
    # Constructor method to initialize a Payment object with amount and optional date
    def __init__(self, amount, date=None):
        # Assigning the amount of the payment to the object
        self.amount = amount
        
        # If no date is provided, assign the current date in the format "YYYY-MM-DD"
        # Otherwise, use the provided date
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    # Method to send a payment reminder
    def send_reminder(self):
        # Print a message to remind the user about the payment
        print("Reminder: Your payment is due.")
    
    # Method to apply a penalty to the payment amount
    def apply_penalty(self, penalty_amount):
        # Adding the penalty amount to the original payment amount
        self.amount += penalty_amount
        
        # Print the penalty applied and the new total amount after the penalty
        print(f"A penalty of ${penalty_amount} has been applied. New amount: ${self.amount}")
