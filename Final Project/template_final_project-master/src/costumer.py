import pygame
import random


class Costumer:
    PIZZA_COST=4
    TIP=3
    
    def __init__(self, x, y, order_paper.jpg, screen):
         """
         Initializes the costumer object
         args:
        - x (int) - starting x coordinate
        - y (int) - starting y coordinate
        - img_file : str - path to order_paper.jpg file
         """
         self.x=x
         self.y=y
         self.screen=screen
         self.image=pygame.image.load(order_paper)
         self.order_text=""
         self.revenue=0
         self.order_time=pygame.time.get_ticks()
         self.order_fulfilled=False
         
    def display_order_image(self):
         """
         Displays the customer's order image
         """
         if not self.order_fulfilled:
            self.screen.blit(self.image, (self.x, self.y))
            pygame.display.flip()
         
    
    def order(self):
        """
        The costumer orders based off a randomly selected
        order from the menu list
        """
        if not self.order_fulfilled:
            order_list=["Toppings: Cheese", "Toppings: Pepperoni","Toppings: Pineapple"]
            self.order_text=random.choice(order_list)
            pygame.font.init()
            my_font=pygame.font.SysFont('comic sans',24)
            text_surface=my_font.render(order_list, False, (0, 0, 0))
            self.screen.blit(text_surface, (self.x + 50, self.y + 50))
            pygame.display.flip()
    
    def pay(self):
        """
        The costumer pays and gives a tip if the order was correct
        """
        if pizza == self.order_text and not self.order_fulfilled:
            self.revenue+=self.PIZZA_COST+self.TIP
            self.order_fulfilled=True
        elif not self.order_fulfilled:
            self.revenue+=self.PIZZA_COST
            self.order_fulfilled=True
        return self.revenue