import pygame

class Cooking:
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_COLOR = (200, 200, 200)
    FONT_COLOR = (0, 0, 0)

    def __init__(self, button, screen):
        """
        Initializes the cooking system.
        """
        self.button = button
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        screen_width, screen_height = self.screen.get_size()

        self.bake_button = pygame.Rect(
            screen_width - self.BUTTON_WIDTH - 20,
            screen_height - 150,
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        self.package_button = pygame.Rect(
            screen_width - self.BUTTON_WIDTH - 20,
            screen_height - 80,
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        topping_button_y = screen_height - 250  

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

        self.dough_button = pygame.Rect(
            (screen_width - self.BUTTON_WIDTH * 3) // 2 - 70, screen_height - self.BUTTON_HEIGHT - 80,
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
        self.dough_message_printed = False
        self.dough_added_message_printed = False  
        self.baking_message_printed = False
        self.packaged_message_printed = False

    def draw_button(self, rect, text):
        """
        Draws a button with text.
        """
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        text_surface = self.font.render(text, True, self.FONT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_cooking_buttons(self):
        """
        Draws all the buttons on the screen.
        """
        self.draw_button(self.dough_button, "Dough")
        for topping, rect in self.toppings_buttons.items():
            self.draw_button(rect, topping)
        self.draw_button(self.bake_button, "Bake")
        self.draw_button(self.package_button, "Package")
        
    def update_game_state(self):
        """
        Updates the game state with feedback for each pizza state.
        """
        if self.pizza_state == 'No Dough':
            if not self.dough_message_printed:
                print("Please add dough to start.")
                self.dough_message_printed = True
        elif self.pizza_state == 'Dough Added':
            if not self.dough_added_message_printed:
                print("Dough added. Add toppings next.")
                self.dough_added_message_printed = True  
        elif self.pizza_state == 'Toppings Added':
            print("Toppings added. Bake the pizza next.")
            
            
    def cooking_button_click(self, event):
        """
        Handles the button clicks and updates pizza state accordingly.
        """
    # Check if the event is a mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
         Get the position of the mouse click
            mouse_pos = event.pos
        
        # Check if the dough button is clicked and the pizza state is 'No Dough'
            if self.dough_button.collidepoint(mouse_pos) and self.pizza_state == 'No Dough':
                 self.pizza_state = 'Dough Added'
                 print("Dough added to the pizza.")
        
            # Handle topping button clicks
            for topping, rect in self.toppings_buttons.items():
                if rect.collidepoint(mouse_pos) and self.pizza_state == 'Dough Added' and topping not in self.toppings:
                    if self.topping_quantities[topping] > 0:
                        self.toppings.append(topping)
                        elf.topping_quantities[topping] -= 1
                        print(f"{topping} added to the pizza.")
                    else:
                        print(f"No more {topping} available.")
        
        # Check if the bake button is clicked
        if self.bake_button.collidepoint(mouse_pos):
            self.pizza_state = 'Baked'
            print("Pizza is baking...")
        
        # Check if the package button is clicked and the pizza state is 'Baked'
        if self.package_button.collidepoint(mouse_pos) and self.pizza_state == 'Baked':
            self.pizza_state = 'Packaged'
            self.toppings = []  # Clear toppings list as the pizza is packaged
            print("Pizza is packaged!")
        else:
            print(f"Unexpected event type: {event.type}")
            
    def draw(self):
        """
        Draws the cooking state and buttons.
        """
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