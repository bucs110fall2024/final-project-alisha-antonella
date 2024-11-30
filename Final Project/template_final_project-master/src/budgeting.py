import pygame

class Budgeting:
    def __init__(self, x, y):
         """
         Initializes the budgeting object/item on screen
         args: x (int) - starting x coordinate
         y (int) - starting y coordinate
         """
        self.x = x
        
        self.y = y
        
        self.money = 0 
        
        self.font = pygame.font.SysFont("Arial", 24) 
        
        self.color = (0, 255, 0) 
         
         
    def countMoney(self, amount)
        """
        Calculates and keeps track of the money earned by user
        """
        
        self.money += amount
         
    def displaysMoney(self, screen)
        """
        Displays the current budget which the user 
        has, in order to buy supplies etc. 
        """
        money_text = f"Money: ${self.money}"
        
        text_surface = self.font.render(money_text, True, self.color)
        
        screen.blit(text_surface, (self.x, self.y))  
    
    
    def budgetPrediction(self, average_earnings, time_played)
        """
        Incorporate a feature in which based on the 
        users usual earnings it can predict how much
        user will have after a certain amount of time 
        played.  
        """
        predicted_money = self.money + (average_earnings * time_played)
        
        return predicted_money