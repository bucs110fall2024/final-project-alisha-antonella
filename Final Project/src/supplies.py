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
             "Cheese": 20,
             "Pineapple": 20,
             "Pepperoni": 20,
         }
         # Calculate position for buttons in top-right corner
         screen_width, screen_height = self.screen.get_size()

        # Set a fixed x-coordinate for the right edge
         self.toppings_buttons = {
            "Buy Cheese": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,  # 20 pixels padding from right edge
                30,  # Start positioning buttons from 100px down
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
            "Buy Pineapple": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,
                90,  # 70 pixels below the "Buy Cheese" button
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
            "Buy Pepperoni": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,
                150,  # 70 pixels below the "Buy Pineapple" button
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
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
        y_offset = 30  # starting Y position
        for topping, quantity in self.resources.items():
            resource_text = font.render(f"{topping}: {quantity}", True, (0, 0, 0))
            self.screen.blit(resource_text, (10, y_offset))
            y_offset += 30
       
    
    def button_click(self, event):
        """
        Event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if self.button.is_clicked(event):
            if self.toppings_buttons["Buy Cheese"].collidepoint(event.pos):
                self.resources["Cheese"] += 5
                print("Bought 5 Cheese.")
            elif self.toppings_buttons["Buy Pineapple"].collidepoint(event.pos):
                self.resources["Pineapple"] += 5
                print("Bought 5 Pineapple.")
            elif self.toppings_buttons["Buy Pepperoni"].collidepoint(event.pos):
                self.resources["Pepperoni"] += 5
                print("Bought 5 Pepperoni.")

    def draw(self):
        """
        Draw the button for buying supplies and display supply counts
        """
        self.draw_supplies_buttons()
        self.update_game_state()