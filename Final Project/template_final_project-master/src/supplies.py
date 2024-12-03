import pygame

class Supplies:
    BUTTON_WIDTH=200
    BUTTON_HEIGHT=50
    BUTTON_COLOR=(200,200,200)
    FONT_COLOR=(0,0,0)
    def __init__(self, button,screen):
         """
         Initializes the button object
         Args:
         - button(): The buy more toppings button 
         - screen(pygame.Surface): Where the button is drawn 
         """
         self.button=button
         self.screen=screen
         self.font=pygame.font.Font(None,36)
         self.dough_button = pygame.Rect(50, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
         self.toppings_buttons = {
            "Buy Cheese": pygame.Rect(50, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Buy Pineapple": pygame.Rect(50, 300, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Buy Pepperoni": pygame.Rect(50, 400, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
        }

    def draw_supplies_button(self, rect, text):
        """
        Draws a button with text
        Args:
        - rect (pygame.Rect): The rectangle for the button
        - text (str): The text displayed on the button
        """
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        text_surface = self.font.render(text, True, self.FONT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_supplies_buttons(self):
        """
        Draws buttons on screen
        """
        for topping, rect in self.toppings_buttons.items():
            self.draw_supplies_button(rect, topping)
       
    def button_click(self, event):
        """
        Event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(event.pos):
                    print(f"{topping} bought!")
           