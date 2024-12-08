import pygame
import random

class Costumer:
    PIZZA_COST=4
    TIP=3
    
    def __init__(self, x, y, paper_order, screen):
         """
         Initializes the costumer object
         Args:
        - x (int): starting x coordinate
        - y (int): starting y coordinate
        - order_paper (str): path to paper_order.jpg file
         """
         self.x=x
         self.y=y
         self.screen=screen
         self.image=pygame.image.load("paper_order.jpg")
         self.image = pygame.transform.scale(self.image, (200, 300))
         self.order_text=""
         self.revenue=0
         self.order_time=pygame.time.get_ticks()
         self.order_fulfilled=False
         
    def display_order_image(self):
         """
         Displays the customer's order image
         """
         if not self.order_fulfilled:
            self.screen.blit(self.image, (0, 0))
            if self.order_text:
                self.render_order_text()
          

    def order(self):
        """
        The costumer orders based off a randomly selected
        order from the menu list
        """
        if not self.order_fulfilled:
            order_list = ["Cheese", "Pepperoni", "Pineapple"]
            self.order_text = f"Toppings: {random.choice(order_list)}" 
            self.display_order_image()
    
    
    def render_order_text(self):
        """
        Renders the order text on top of the paper_order image
        """
        pygame.font.init()
        my_font = pygame.font.SysFont('comic sans', 24)  

        
        order_lines = self.order_text.split(", ")  

        y_offset = self.y + 120  
        for line in order_lines:
            text_surface = my_font.render(line, True, (0, 0, 0)) 
            text_rect = text_surface.get_rect(center=(self.x + 100, y_offset))  

            self.screen.blit(text_surface, text_rect)
            y_offset += 30
    
    def pay(self, pizza):
        """
        The costumer pays and gives a tip if the order was correct
        Args:
        - pizza (str): The toppings 
        Returns: 
        -revenue (int): The revenue from the customer 
        """
        if pizza == self.order_text and not self.order_fulfilled:
             self.revenue += self.PIZZA_COST + self.TIP
             self.order_fulfilled = True
        elif not self.order_fulfilled:
             self.revenue += self.PIZZA_COST
             self.order_fulfilled = True
        return self.revenue