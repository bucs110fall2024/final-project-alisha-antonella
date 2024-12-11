import pygame

class Cooking:
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_COLOR = (255, 182,193)
    FONT_COLOR = (0, 0, 0)

    def __init__(self, button, screen, customer, initial_resources=None):
        """
        Initializes the cooking system.
        """
        self.button = button
        self.screen = screen
        self.customer=customer
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
         
        self.supply_buttons={
             "Buy Cheese": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,  
                30,  
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
            "Buy Pineapple": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,
                90,  
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
            "Buy Pepperoni": pygame.Rect(
                screen_width - self.BUTTON_WIDTH - 20,
                150, 
                self.BUTTON_WIDTH,
                self.BUTTON_HEIGHT
            ),
        }

        self.dough_button = pygame.Rect(
            (screen_width - self.BUTTON_WIDTH * 3) // 2 - 70, screen_height - self.BUTTON_HEIGHT - 80,
            self.BUTTON_WIDTH,
            self.BUTTON_HEIGHT
        )

        self.topping_quantities = {
            "Cheese": 20,
            "Pineapple": 20,
            "Pepperoni": 20
        }
        
             
        self.pizza_state = 'No Dough'
        self.toppings = []
        self.is_baking = False
        self.dough_message_printed = False
        self.dough_added_message_printed = False  
        self.baking_message_printed = False
        self.packaged_message_printed = False
           
        self.dough=pygame.image.load("dough.png")
        self.dough = pygame.transform.scale(self.dough, (300, 300))
        
        self.cheese_pizza_raw=pygame.image.load("cheese_pizza raw.png")
        self.cheese_pizza_raw = pygame.transform.scale(self.cheese_pizza_raw, (300, 300))
       
        self.pineapple_pizza_raw=pygame.image.load("pineapple_pizza_raw.png")
        self.pineapple_pizza_raw = pygame.transform.scale(self.pineapple_pizza_raw, (300, 300))
       
        self.pepperoni_pizza_raw=pygame.image.load("pepperoni_pizza_raw.png")
        self.pepperoni_pizza_raw = pygame.transform.scale(self.pepperoni_pizza_raw, (300, 300))
        
        self.cheese_pizza_cooked=pygame.image.load("cheese_pizza_cooked.png")
        self.cheese_pizza_cooked = pygame.transform.scale(self.cheese_pizza_cooked, (300, 300))
        
        self.pineapple_pizza_cooked=pygame.image.load("pineapple_pizza_cooked.png")
        self.pineapple_pizza_cooked= pygame.transform.scale(self.pineapple_pizza_cooked, (300, 300))
        
        self.pepperoni_pizza_cooked=pygame.image.load("pepperoni_pizza_cooked.png")
        self.pepperoni_pizza_cooked= pygame.transform.scale(self.pepperoni_pizza_cooked, (300, 300))
        
        self.pizza_box=pygame.image.load("pizza_box.png")
        self.pizza_box = pygame.transform.scale(self.pizza_box, (240, 240))


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
            if 'Buy' not in topping:
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
            if not self.dough_added_message_printed:
                print("Toppings added. Bake the pizza next.")
                self.dough_added_message_printed = True

    def reset(self):
        """
        Resets the pizza state 
        """
        self.pizza_state='No Dough'
        self.toppings=[]
        print("Ready for a new pizza!")

    def cooking_button_click(self, event, screen):
        """
        Handles the button clicks and updates pizza state accordingly.
        """
        if self.dough_button.collidepoint(event.pos) and self.pizza_state == 'No Dough':
            self.pizza_state = 'Dough Added'
            print("Dough added to the pizza.")
    
        for topping, rect in self.toppings_buttons.items():
            if rect.collidepoint(event.pos) and self.pizza_state in ['Dough Added', 'Toppings Added'] and topping not in self.toppings:
                if self.topping_quantities[topping] > 0:
                    self.pizza_state = 'Toppings Added'
                    self.toppings.append(topping)
                    self.topping_quantities[topping] -= 1 
                    print(f"{topping} added to the pizza. Remaining: {self.topping_quantities[topping]}")
                else:
                    print(f"No more {topping} available.")
    
        if self.bake_button.collidepoint(event.pos):
            self.pizza_state = 'Baked'
            print("Pizza is baking...")
            
        if self.package_button.collidepoint(event.pos) and self.pizza_state == 'Baked':
            self.pizza_state = 'Packaged'
            self.toppings = [] 
            print("Pizza is packaged!")
            self.customer.update_order()
            self.reset()  
        
#/////////
    def draw_supplies_button(self):
        """
        Draws a button with text
        Args:
        - rect (pygame.Rect): The rectangle for the button
        - text (str): The text displayed on the button
        """
        for topping, rect in self.supply_buttons.items():
            self.draw_button(rect, topping)
       
    def update_game_state(self):
        """
        Update the game state by displaying available resources
        """
        font = pygame.font.SysFont('comic sans', 24)
        resource_text = font.render(f"Cheese: {self.topping_quantities['Cheese']} | Pineapple: {self.topping_quantities['Pineapple']} | Pepperoni: {self.topping_quantities['Pepperoni']}", True, (0, 0, 0))
        self.screen.blit(resource_text, (310, 250))

    def button_click(self, event):
        """
        Event when button is clicked
        Args:
        - event (pygame.event.Event): The event to handle
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            for topping, rect in self.supply_buttons.items():
                if rect.collidepoint(event.pos):
                    self.buy_topping(topping)
    
    def buy_topping(self, topping):
        """
        Handles the purchase of a topping
        """
        if topping == "Buy Cheese":
            if self.customer.budget.money >= 5:
                self.customer.budget.countMoney(-5)
                self.topping_quantities["Cheese"] += 5
                print("Bought 5 Cheese!")
            else:
                print("Insufficient budget to buy Cheese.")
        elif topping == "Buy Pineapple":
            if self.customer.budget.money >= 5:
                self.customer.budget.countMoney(-5)
                self.topping_quantities["Pineapple"] += 5
                print("Bought 5 Pineapple!")
            else:
                print("Insufficient budget to buy Pineapple.")
        elif topping == "Buy Pepperoni":
            if self.customer.budget.money >= 5:
                self.customer.budget.countMoney(-5)
                self.topping_quantities["Pepperoni"] += 5
                print("Bought 5 Pepperoni!")
            else:
                print("Insufficient budget to buy Pepperoni.")
            
    def draw(self):
        """
        Draws the cooking state and buttons.
        """     
        self.draw_cooking_buttons() 
        self.draw_supplies_button() 
        self.update_game_state() 
        
        font = pygame.font.SysFont('comic sans', 24)
        state_text = font.render(f"Pizza State: {self.pizza_state}", True, (0, 0, 0))
        self.screen.blit(state_text, (10, 30))
        
        if self.pizza_state == 'Dough Added':
            self.screen.blit(self.dough, (250, 4))
            
        elif self.pizza_state == 'Toppings Added':
            if 'Cheese' in self.toppings:
                self.screen.blit(self.cheese_pizza_raw, (250, 4))
            elif 'Pineapple' in self.toppings:
                self.screen.blit(self.pineapple_pizza_raw, (250, 4))
            elif 'Pepperoni' in self.toppings:
                self.screen.blit(self.pepperoni_pizza_raw, (250, 4))
        elif self.pizza_state == 'Baked':
            if 'Cheese' in self.toppings:
                self.screen.blit(self.cheese_pizza_cooked, (250, 4))
            elif 'Pineapple' in self.toppings:
                self.screen.blit(self.pineapple_pizza_cooked, (250, 4))
            elif 'Pepperoni' in self.toppings:
                self.screen.blit(self.pepperoni_pizza_cooked, (250, 4))

        if self.pizza_state =="No Dough":
            pass