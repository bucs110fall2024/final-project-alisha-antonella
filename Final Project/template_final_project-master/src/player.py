import pygame

<<<<<<< HEAD
class Player:
    
    def __init__(self, x, y, img_file):
         """
         Initializes the player object
         args:
        - x (int) - starting x coordinate
        - y (int) - starting y coordinate
        - img_file : str - path to ____ file
         """
    
    def takeorder(self)
        """
        The player takes an order based on what
        the customer wants
        """
        
    def movestations(self)
        """
        The player moves from each station to 
        make the order 
        """
    
    def usebudget(self)
        """
        Player uses bduget to calculate how much
        they can spend on supplies/upgrades
        """
    
=======
class Player(pyagem.sprite.Sprite):
    
    def __init__(self, name):
        super().__init__()
        
        self.name
        self.size = "small"
        self.image = pygame.image.load("assets/(name).png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0  
>>>>>>> b9499dfed023231edcd5c019245f8adf87772dd0
