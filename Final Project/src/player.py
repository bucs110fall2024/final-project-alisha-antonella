import pygame

class Player:
    
    def __init__(self, x, y, img_file, budget, scale=(150, 150)):
         """
         Initializes the player object
         args:
        - x (int) - starting x coordinate
        - y (int) - starting y coordinate
        - img_file : str - path to ____ file
         """
         self.x = x
        
         self.y = y
        
         self.image = pygame.image.load(img_file) 
         
         self.image = pygame.transform.scale(self.image, scale) 
        
         self.rect = self.image.get_rect() 
    
         self.rect.topleft = (x, y) 
        
         self.order = None 
        
         self.budget = budget 
        
    def takeorder(self):
        """
        The player receives an order and goes
        to each station based on the order 
        """
        self.order = order
         
        print(f"Order received: {order.description}")
        
    def movestations(self):
        """
        The player moves from each station to 
        make the order 
        """
        print(f"Starting to move between stations to fulfill the order...")
        
        for station in station_list:
          
            self.x, self.y = station.get_position() 
            
            self.rect.topleft = (self.x, self.y) 
            
            print(f"Moved to {station.name} at position {self.x}, {self.y}")
           
    
    def usebudget(self):
        """
        Player uses budget class to calculate how much
        they can spend on supplies/upgrades
        """
        if not self.budget:
             
            print("No budget available.")
            
            return
        
        print("Checking available budget for items:")
        
        for item, cost in item_costs.items():
            
            if self.budget.can_afford(cost):
                
                self.budget.spend(cost)
                
                print(f"Bought {item} for {cost} units.")
                
            else:
                
                print(f"Cannot afford {item} (cost: {cost} units).")