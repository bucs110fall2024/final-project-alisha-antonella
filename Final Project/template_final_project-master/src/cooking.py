import pygame

class Cooking:
    BUTTON_WIDTH=200
    BUTTON_HEIGHT=50
    BUTTON_COLOR=(200,200,200)
    FONT_COLOR=(0,0,0)
    
    def __init__(self, button,screen):
         """
         initializes the button object
         Args:
         - button(): The pizza button 
         - screen(pygame.Surface): Where the button is drawn 
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
         self.pizza_state = 'No Dough' 
         self.toppings = ["Cheese", "Pineapple", "Pepperoni"] 
         self.is_baking = False
         
         
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


    def draw_cooking_buttons(self):
        """
        draws buttons on screen
        """
        self.draw_button(self.dough_button, "Dough")
        for topping, rect in self.toppings_buttons.items():
            self.draw_button(rect, topping)
        self.draw_button(self.bake_button, "Bake")
        self.draw_button(self.package_button, "Package")


    def update_game_state(self):
        """
        Updates the game based on the current pizza state
        """
        if self.pizza_state == 'Dough Added':
            print("Dough added, now add toppings.")
        elif self.pizza_state == 'Toppings Added':
            print("Toppings added, now bake the pizza.")
        elif self.pizza_state == 'Baked':
            print("Pizza is baked, now package it.")
        elif self.pizza_state == 'Packaged':
            print("Pizza is packaged, ready to serve.")


    def cooking_button_click(self, event):
        """
        Handles the cooking actions
        """
        if self.button.is_clicked(event):
            if self.dough_button.collidepoint(event.pos) and self.pizza_state == 'No Dough':
                self.pizza_state = 'Dough Added'
                print("Dough added to the pizza.")
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(event.pos) and self.pizza_state == 'Dough Added':
                    if topping not in self.toppings:  # Add topping if it's not already added
                        self.toppings.append(topping)
                        print(f"{topping} added to the pizza.")
            if self.bake_button.collidepoint(event.pos) and self.pizza_state == 'Toppings Added':
                self.pizza_state = 'Baked'
                self.is_baking = True
                print("Pizza is baking...")
            if self.package_button.collidepoint(event.pos) and self.pizza_state == 'Baked':
                self.pizza_state = 'Packaged'
                print("Pizza is packaged.")
                self.is_baking = False


    def draw(self):
        """
        Draw the current state of the cooking process and buttons
        """
        self.draw_cooking_buttons()
        self.update_game_state()
        font = pygame.font.SysFont('comic sans', 24)
        state_text = font.render(f"Pizza State: {self.pizza_state}", True, (0, 0, 0))
        self.screen.blit(state_text, (10, 10))