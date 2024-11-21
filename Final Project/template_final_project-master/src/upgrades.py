import pygame

class Upgrades:
     BUTTON_WIDTH=200
     BUTTON_HEIGHT=50
     BUTTON_COLOR=(200,200,200)
     FONT_COLOR=(0,0,0)
     def __init__(self, button,screen):
         """
         initializes the button object
         args:
        - 
         """
         self.button=button
         self.screen=screen
         self.font=pygame.font.Font(None,36)
         self.better_toppings = pygame.Rect(50, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
         self.faster_cooking = pygame.Rect(300, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
       

     def draw_upgrade_button(self, rect, text):
        """
        draws a button with text
        Args:
        - rect (pygame.Rect): The rectangle for the button
        - text (str): The text displayed on the button
        """
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        text_surface = self.font.render(text, True, self.FONT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

     def draw_upgrade_buttons(self):
        """
        draws buttons on screen
        """
        self.draw_upgrade_button(self.better_toppings, "Buy Better Toppings")
        self.draw_upgrade_button(self.faster_cooking, "Buy Faster Cooking")

     def cooking_button_click(self, event):
        """
        event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if self.better_toppings.collidepoint(event.pos):
                print("More Toppings Bought!")
            if self.faster_cooking.collidepoint(event.pos):
                print("Faster Cooking Bought!")
    
   