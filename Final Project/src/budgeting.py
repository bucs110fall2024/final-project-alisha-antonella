import pygame
import datetime

class Budgeting:
    MAX_MONEY = 1000  # Cap on the maximum money the player can have

    def __init__(self, x, y):
        """
        Initializes the budgeting object/item on screen
        args: 
        - x (int): starting x coordinate
        - y (int): starting y coordinate
        """
        self.x = x
        self.y = y
        self.money = 0.0  # Using a float for money to allow decimal places
        self.font = pygame.font.SysFont("Arial", 24)
        self.color = (0, 255, 0)
        self.transaction_history = []  # List to store transaction history
        self.recent_earnings = []  # Store recent earnings for dynamic prediction

    def format_money(self):
        """
        Formats the money to include commas and two decimal places (e.g., $1,000.00).
        """
        return f"${self.money:,.2f}"

    def countMoney(self, amount):
        """
        Calculates and keeps track of the money earned by user, with input validation.
        Ensures that amount is a valid number and checks for enough balance when subtracting.
        
        args:
        - amount (float): The amount of money to add or subtract
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be an integer or float.")
        
        if amount < 0 and abs(amount) > self.money:
            print("Not enough money to subtract.")
            return  # Don't allow spending more money than the player has
        
        old_balance = self.money
        self.money += amount
        
        # Record the transaction history
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"[{timestamp}] Changed: ${old_balance} -> ${self.money:.2f}. Amount: ${amount:.2f}")

        # Apply money cap
        if self.money > self.MAX_MONEY:
            self.money = self.MAX_MONEY
            print(f"Money cap reached: ${self.MAX_MONEY}")
        
        print(f"Current balance: {self.format_money()}")

        # Track recent earnings for dynamic prediction
        if amount > 0:
            self.recent_earnings.append(amount)
            if len(self.recent_earnings) > 5:  # Keep only the last 5 earnings for averaging
                self.recent_earnings.pop(0)

    def displaysMoney(self, screen):
        """
        Displays the current budget which the user has, in order to buy supplies etc.
        """
        money_text = f"Money: {self.format_money()}"
        text_surface = self.font.render(money_text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))

    def budgetPrediction(self, time_played):
        """
        Dynamically predicts how much money the user will have based on recent earnings.
        
        args:
        - time_played (float): The time in hours that the player has been playing

        Returns:
        - predicted_money (float): Predicted money based on average earnings and time played
        """
        # Calculate average earnings from recent game events
        if not self.recent_earnings:
            average_earnings = 0
        else:
            average_earnings = sum(self.recent_earnings) / len(self.recent_earnings)
        
        predicted_money = self.money + (average_earnings * time_played)
        # Allow for a high or low range prediction based on recent performance
        high_earnings = self.money + (1.5 * average_earnings * time_played)
        low_earnings = self.money + (0.5 * average_earnings * time_played)

        # Print out different prediction scenarios
        print(f"Predicted Money: {self.format_money()}")
        print(f"High Earnings Prediction: {self.format_money()}")
        print(f"Low Earnings Prediction: {self.format_money()}")
        
        return predicted_money, high_earnings, low_earnings