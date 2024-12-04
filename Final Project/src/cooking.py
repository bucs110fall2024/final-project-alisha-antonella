import pygame

class Cooking:
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_COLOR = (200, 200, 200)
    FONT_COLOR = (0, 0, 0)

    def __init__(self, button, screen):
        """
        Initializes the button object
        Args:
        - button(): The pizza button 
        - screen(pygame.Surface): Where the button is drawn 
        """
        self.button = button
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        # Screen size for dynamic positioning
        screen_width, screen_height = self.screen.get_size()

        # Position the bake and package buttons at bottom-right
        self.bake_button = pygame.Rect(
            screen_width - self.BUTTON_WIDTH - 20,  # 20 pixels padding from the right edge
            screen_height - 150,                   # 150 pixels from the bottom
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        self.package_button = pygame.Rect(
            screen_width - self.BUTTON_WIDTH - 20,  # Same horizontal position as bake_button
            screen_height - 80,                    # Positioned 10 pixels below the bake button
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        # Topping buttons horizontally aligned in the bottom center
        topping_button_y = screen_height - 250  # Adjust this to align with Bake and Package buttons

        self.toppings_buttons = {
            "Cheese": pygame.Rect(
                (screen_width - self.BUTTON_WIDTH * 3) // 2 + 200, topping_button_y + 60, self.BUTTON_WIDTH, self.BUTTON_HEIGHT
            ),
            "Pineapple": pygame.Rect(
                (screen_width - self.BUTTON_WIDTH * 3) // 2 + 200, topping_button_y + 120, self.BUTTON_WIDTH, self.BUTTON_HEIGHT
            ),
            "Pepperoni": pygame.Rect(
                (screen_width - self.BUTTON_WIDTH * 3) // 2 + 200, topping_button_y + 180, self.BUTTON_WIDTH, self.BUTTON_HEIGHT
            ),
        }

        # Dough button horizontally aligned with Pineapple button
        self.dough_button = pygame.Rect(
            (screen_width - self.BUTTON_WIDTH * 3) // 2 - 70, screen_height - self.BUTTON_HEIGHT - 80,  # Same x-position as Pineapple
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        self.pizza_state = 'No Dough'
        self.toppings = []
        self.is_baking = False

        self.topping_quantities = {
            "Cheese": 20,
            "Pineapple": 20,
            "Pepperoni": 20
        }
        self.baking_duration = 30

        # Flag to track if "Please add dough to start" has been printed
        self.dough_message_printed = False

    def draw_button(self, rect, text):
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

    def draw_cooking_buttons(self):
        self.draw_button(self.dough_button, "Dough")
        for topping, rect in self.toppings_buttons.items():
            self.draw_button(rect, topping)
        self.draw_button(self.bake_button, "Bake")
        self.draw_button(self.package_button, "Package")

    def update_game_state(self):
        """
        Update the game state 
        """
        if self.pizza_state == 'No Dough':
            if not self.dough_message_printed:
                print("Please add dough to start.")
                self.dough_message_printed = True  # Set flag to True after printing
        elif self.pizza_state == 'Dough Added':
            print("Dough added. Add toppings next.")
        elif self.pizza_state == 'Toppings Added':
            print("Toppings added. Bake the pizza next.")
        elif self.pizza_state == 'Baked':
            print("Pizza is baked. Now package it!")
        elif self.pizza_state == 'Packaged':
            print("Pizza is packaged and ready.")

    def cooking_button_click(self, event):
        if self.button.is_clicked(event):
            if self.dough_button.collidepoint(event.pos) and self.pizza_state == 'No Dough':
                self.pizza_state = 'Dough Added'
                print("Dough added to the pizza.")
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(event.pos) and self.pizza_state == 'Dough Added' and topping not in self.toppings:
                    if self.topping_quantities[topping] > 0:
                        self.toppings.append(topping)
                        self.topping_quantities[topping] -= 1
                        print(f"{topping} added to the pizza.")
                    else:
                        print(f"No more {topping} available.")

            if self.bake_button.collidepoint(event.pos) and self.pizza_state == 'Toppings Added':
                self.pizza_state = 'Baked'
                self.is_baking = True
                self.baking_start_time = pygame.time.get_ticks()  # Start the timer
                print("Pizza is baking...")

            if self.package_button.collidepoint(event.pos) and self.pizza_state == 'Baked':
                self.pizza_state = 'Packaged'
                print("Pizza is packaged.")
                self.is_baking = False
                self.toppings = []

    def draw(self):
        if self.is_baking:
            elapsed_time = (pygame.time.get_ticks() - self.baking_start_time) / 1000
            if elapsed_time >= self.baking_duration:
                self.is_baking = False
                print("Pizza is done!")

        self.draw_cooking_buttons()
        self.update_game_state()

        font = pygame.font.SysFont('comic sans', 24)
        state_text = font.render(f"Pizza State: {self.pizza_state}", True, (0, 0, 0))
        self.screen.blit(state_text, (10, 10))

        if self.is_baking:
            remaining_time = max(0, self.baking_duration - (elapsed_time))
            timer_text = font.render(f"Time Remaining: {int(remaining_time)}s", True, (255, 0, 0))
            self.screen.blit(timer_text, (10, 40))
