import pygame

class Player(pyagem.sprite.Sprite):
    
    def __init__(self, name):
        super().__init__()
        
        self.name
        self.size = "small"
        self.image = pygame.image.load("assets/(name).png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
        