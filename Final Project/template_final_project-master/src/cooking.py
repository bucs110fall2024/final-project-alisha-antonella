import pygame

class Cooking:
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
         self.dough_button = pygame.Rect(50, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
         self.toppings_buttons = {
            "Cheese": pygame.Rect(50, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Pineapple": pygame.Rect(50, 300, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Pepperoni": pygame.Rect(50, 400, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
        }
         self.bake_button = pygame.Rect(300, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
         self.package_button = pygame.Rect(300, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

    def draw_button(self, rect, text):
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

    def draw_buttons(self):
        """
        draws buttons on screen
        """
        self.draw_button(self.dough_button, "Dough")
        for topping, rect in self.toppings_buttons.items():
            self.draw_button(rect, topping)
        self.draw_button(self.bake_button, "Bake")
        self.draw_button(self.package_button, "Package")

    def button_click(self, event):
        """
        event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            if self.dough_button.collidepoint(event.pos):
                print("Dough button clicked!")
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(event.pos):
                    print(f"{topping} button clicked!")
            if self.bake_button.collidepoint(event.pos):
                print("Bake button clicked!")
            if self.package_button.collidepoint(event.pos):
                print("Package button clicked!")
    