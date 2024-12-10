import pygame
import random

class Customer:
    PIZZA_COST=4
    TIP=3
    
    def __init__(self, x, y, paper_order, screen):
         """
         Initializes the costumer object
         Args:
        - x (int): The x-coordinate of the customer.
        - y (int): The y-coordinate of the customer.
        - order_paper (str): path to paper_order.jpg file
         """
         self.x = x
         self.y = y
         self.screen=screen
         self.image=pygame.image.load("paper_order.jpg")
         self.image = pygame.transform.scale(self.image, (266, 300))
         self.order_text=""
         self.revenue=0
         self.order_fulfilled=False
         self.font = pygame.font.SysFont('comic sans', 24)
         self.order_list = ["Cheese", "Pepperoni", "Pineapple"]
         self.selected_topping = random.choice(self.order_list)
         
    def display_order_image(self):
         """
         Displays the customer's order image
         """
         if not self.order_fulfilled:
            self.screen.blit(self.image, (0, 0))
            if self.order_text:
                self.render_order_text()
     
    def update_order(self):
        """
        Updates the customer's topping order to a new random topping.
        """
        self.selected_topping = random.choice(self.order_list)
        print(f"New order: {self.selected_topping}")
             
    def display_order_text(self):
        """
        Renders the order text on top of the paper_order image
        """
        order_text = self.font.render(f"Toppings: {self.selected_topping}", True, (0, 0, 0))
        self.screen.blit(order_text, (10, 90))
    
    
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