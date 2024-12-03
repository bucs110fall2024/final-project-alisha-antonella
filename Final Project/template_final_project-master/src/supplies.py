import pygame

class Supplies:
    BUTTON_WIDTH=200
    BUTTON_HEIGHT=50
    BUTTON_COLOR=(200,200,200)
    FONT_COLOR=(0,0,0)
    def __init__(self, button,screen, initial_resources=None):
         """
         Initializes the button object
         Args:
         - button(): The buy more toppings button 
         - screen(pygame.Surface): Where the button is drawn 
         """
         self.button=button
         self.screen=screen
         self.font=pygame.font.Font(None,36)
         self.resources=initial_resources or {
             "Cheese": 0,
             "Pineapple": 0,
             "Pepperoni": 0,
         }
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
       
       
    def update_game_state(self):
        """
        Update the game state by displaying available resources
        """
        font = pygame.font.SysFont('comic sans', 24)
        resource_text = font.render(f"Cheese: {self.resources['Cheese']} | Pineapple: {self.resources['Pineapple']} | Pepperoni: {self.resources['Pepperoni']}", True, (0, 0, 0))
        self.screen.blit(resource_text, (10, 10))

       
    def button_click(self, event):
        """
        Event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(event.pos):
                    self.buy_topping(topping)
    
    
    def buy_topping(self, topping):
        """
        Handles the purchase of a topping
        """
        if topping == "Buy Cheese":
            self.resources["Cheese"] += 1
            print("Bought Cheese!")
        elif topping == "Buy Pineapple":
            self.resources["Pineapple"] += 1
            print("Bought Pineapple!")
        elif topping == "Buy Pepperoni":
            self.resources["Pepperoni"] += 1
            print("Bought Pepperoni!")


    def draw(self):
        """
        Draws the supplies buttons and updates the game state
        """
        self.draw_supplies_buttons()
        self.update_game_state()