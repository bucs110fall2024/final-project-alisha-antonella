import pygame
import pygame_menu
from button import Button
from cooking import Cooking
from customer import Costumer
from music import Music
from player import Player
from supplies import Supplies
from budgeting import Budgeting

class Controller:
    def __init__(self):
        # Setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.fill((150, 150, 250))
        
        # Setup menu(s)
        width, height = pygame.display.get_window_size()
        self.menu = pygame_menu.Menu("My Pizza Restaurant", width-20, height/2, position=(10, 10))
        self.menu.add.label("Press to Start", max_char=-1, font_size=14)
        self.menu.add.button('Press Me', self.start_game, align=pygame_menu.locals.ALIGN_CENTER)



        # Game state
        self.state = "menu"
    
        # Initialize game objects
        self.customer = None
        self.cooking = None
        self.supplies = None
        self.player = None
        self.budget = Budgeting(10, 10)
        self.music = Music("background_music.mp3")  # Replace with your actual music file
        self.button = Button(x=50, y=self.menu.get_rect().bottom + 10)
        
        self.item_costs = {
                "cheese": 10,
                "tomato": 5,
                "pepperoni": 15
        }
        self.current_item = None  # Track the current item player interacts with
        self.current_cost = 0

    def start_game(self):
        """
        Initialize the game state when the start button is pressed.
        """
        self.state = "game"
        self.customer = Costumer(100, 100, "paper_order.jpg", self.screen)
        self.cooking = Cooking(self.button, self.screen)
        self.supplies = Supplies(self.button, self.screen)
        self.player = Player(100, 100, "player_image.jpg", self.budget)

    def menu_state(self):
        """
        Handles the menu state.
        """
        while self.state == "menu":
            if self.menu.is_enabled():
                # Handle menu events and update
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
                pygame.display.flip()
            else:
                break  # Exit loop when menu is no longer enabled

    def game_state(self):
        """
        Handles the game state.
        """
        while self.state == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "menu"
                self.handle_events(event)

        if self.current_item:
            success = self.player.use_budget(self.current_item, self.current_cost)
            if success:
                # Perform the action (e.g., update the game state, deliver item)
                print(f"Action completed for {self.current_item}")
            else:
                # Reset or handle failure to complete action
                print(f"Could not complete action for {self.current_item}")
            self.current_item = None  # Reset after attempting action

            # Update game elements
            self.screen.fill((150, 150, 250))  # Background color
            self.customer.display_order_image()
            self.budget.displaysMoney(self.screen)
            self.player.move_to_station(self.cooking.dough_button)
            self.cooking.draw()
            self.supplies.draw()
            self.supplies.update_game_state()

            pygame.display.flip()
            self.clock.tick(60)

    def gameover_state(self):
        """
        Handles the game over state. Can be expanded for restart or exit.
        """
        pass  # Implement game over logic here

    def handle_events(self, event):
        """
            Handles events from the game loop.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.cooking.cooking_button_click(event)
            self.supplies.button_click(event)
        
        # Handle dough button click
            if self.cooking.dough_button.collidepoint(event.pos):
                self.current_item = "Dough"
                self.current_cost = 5  # Example cost for dough
                return

        # Handle topping buttons dynamically
            for topping, rect in self.cooking.toppings_buttons.items():
                if rect.collidepoint(event.pos):
                    self.current_item = topping
                    self.current_cost = self.item_costs.get(topping, 0)  # Get cost from the dictionary
                    return

        # Handle bake and package buttons
            if self.cooking.bake_button.collidepoint(event.pos):
                print("Bake button clicked!")
            elif self.cooking.package_button.collidepoint(event.pos):
                print("Package button clicked!")
    
    # Check if the menu is enabled and handle the start button click
        if self.menu.is_enabled():
            mouse_pos = pygame.mouse.get_pos()
            if self.menu.get_rect().collidepoint(mouse_pos):
                self.start_game()
                print("Start button clicked!")
            else:
            # If not over the menu, check other interactions
                self.cooking.cooking_button_click(event)
                self.supplies.button_click(event)
       
    def reset_game(self):
        """
        Resets the game state to start a new game.
        """
        self.player = Player(100, 100, "player_image.jpg", self.budget)
        self.customer = Costumer(100, 100, "paper_order.jpg", self.screen)
        self.cooking = Cooking(self.button, self.screen)
        self.supplies = Supplies(self.button, self.screen)
        self.state = "game"

    def mainloop(self):
        """
        Main game loop that determines the current game state and calls the appropriate function.
        """
        while True:
            if self.state == "menu":
                self.menu_state()
            elif self.state == "game":
                self.game_state()
            elif self.state == "gameover":
                self.gameover_state()