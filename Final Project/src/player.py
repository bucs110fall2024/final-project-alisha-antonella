import pygame

class Player:
    def __init__(self, x, y, img_file, budget, speed=5):
        """
        Initializes the player object with an image and a starting budget.
        
        args:
        - x (int): starting x coordinate
        - y (int): starting y coordinate
        - img_file (str): path to the image file for the player (e.g., "player_image.jpeg")
        - budget (Budgeting object): the player's budgeting system
        - speed (int): movement speed (default is 5)
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.budget = budget
        self.order = None
        self.state = 'idle'  # Could be 'idle', 'moving', 'working', etc.
        self.velocity = pygame.Vector2(0, 0)  # For more advanced movement later

    def takeorder(self, order):
        """
        The player receives an order and goes to each station based on the order.
        """
        self.order = order
        self.state = 'working'  # Transition state to 'working' when taking an order
        print(f"Order received: {order.description}")
        
    def move(self, direction):
        """
        Move the player in a specific direction (e.g., 'up', 'down', 'left', 'right').
        """
        if direction == 'up':
            self.velocity.y = -self.speed
        elif direction == 'down':
            self.velocity.y = self.speed
        elif direction == 'left':
            self.velocity.x = -self.speed
        elif direction == 'right':
            self.velocity.x = self.speed
        self.state = 'moving'

    def stop_movement(self):
        """
        Stops the player's movement by resetting velocity to 0.
        """
        self.velocity = pygame.Vector2(0, 0)
        self.state = 'idle'

    def update_position(self):
        """
        Update the player's position based on the current velocity.
        """
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def move_to_station(self, station_rect):
        """
        Move the player to a specific station (e.g., oven, counter).
        """
        # Simple example of moving directly to the station
        self.rect.topleft = station_rect.topleft

    def use_budget(self, item, cost):
        """
        Use the player's budget to buy a specific item or service.
        """
        if self.budget.money >= cost:
            self.budget.countMoney(-cost)
            print(f"Bought {item} for {cost} units.")
        else:
            print(f"Not enough money to buy {item}.")

    def draw(self, screen):
        """
        Draw the player on the screen at the current position.
        """
        screen.blit(self.image, self.rect.topleft)
        
    def get_state(self):
        """
        Return the current state of the player.
        """
        return self.state