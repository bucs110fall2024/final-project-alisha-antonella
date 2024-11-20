import pygame
import random


class Costumer:
    PIZZA_COST=int(4)
    TIP=int(3)
    
    def __init__(self, x, y, order_paper.jpg):
         """
         Initializes the costumer object
         args:
        - x (int) - starting x coordinate
        - y (int) - starting y coordinate
        - img_file : str - path to order_paper.jpg file
         """
         current_time=0
         last_image_time=0
         image=pygame.image.load("templat_final_project-master/assests/order_paper.jpg")
         width, height=image.get_size()
         screen.blit(image, (0,0))
         pygame.display.flip()
         
    
    def order(self):
        """
        The costumer orders based off a randomly selected
        order from the menu list
        """
        order_list=["Toppings: Cheese", "Toppings: Pepperoni","Toppings: Pineapple"]
        random_order=random.choice(order_list)
        pygame.font.init()
        my_font=pygame.font.SysFont('comic sans')
        text_surface=my_font.render(order_list, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
    
    def review(self):
        """
        The costumer gives a review and gives a certain amount 
        of tip based off of how well the player makes their order
        """
        if pizza=order_list:
            revenue=PIZZA_COST+TIP
        else:
            revenue=PIZZA_COST

