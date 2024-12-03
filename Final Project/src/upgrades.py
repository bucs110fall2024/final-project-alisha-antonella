import pygame

class Upgrades:
     BUTTON_WIDTH=200
     BUTTON_HEIGHT=50
     BUTTON_COLOR=(200,200,200)
     FONT_COLOR=(0,0,0)
     def __init__(self,screen, player):
         """
         Initializes the button object
         Args:
         - screen(pygame.Surface): Where the button is drawn 
         """
         self.screen=screen
         self.font=pygame.font.Font(None,36)
         self.player=player
         self.upgrades = {
            "Better Toppings": pygame.Rect(50, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Faster Cooking": pygame.Rect(50, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
        }
         self.purchased_upgrades = {
            "Better Toppings": False,
            "Faster Cooking": False
        }
       
       
     def draw_button(self, rect, text):
        """
        Draws a button with the given text on the screen
        """
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, rect)
        text_surface = self.font.render(text, True, self.FONT_COLOR)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

     def draw_upgrade_buttons(self):
        """
        Draws the buttons for available upgrades
        """
        y_offset = 100  
        for upgrade, rect in self.upgrades.items():
            rect.y = y_offset  
            self.draw_button(rect, upgrade) 
            y_offset += self.BUTTON_HEIGHT + 10  

     def update_game_state(self):
        """
        Update the game state by displaying purchased upgrades
        """
        font = pygame.font.SysFont('comic sans', 24)
        upgrade_text = font.render(
            f"Better Toppings: {'Yes' if self.purchased_upgrades['Better Toppings'] else 'No'} | "
            f"Faster Cooking: {'Yes' if self.purchased_upgrades['Faster Cooking'] else 'No'}", 
            True, (0, 0, 0))
        self.screen.blit(upgrade_text, (10, 10))


     def button_click(self, event):
        """
        Handles the event when a button is clicked to buy upgrades
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
            for upgrade, rect in self.upgrades.items():
                if rect.collidepoint(event.pos):
                    self.buy_upgrade(upgrade)

     def buy_upgrade(self, upgrade):
        """
        Handles the purchase of an upgrade
        """
        if upgrade == "Better Toppings" and not self.purchased_upgrades["Better Toppings"]:
            self.purchased_upgrades["Better Toppings"] = True
            print("Bought Better Toppings!")
            self.player.increase_topping_effectiveness()  
        elif upgrade == "Faster Cooking" and not self.purchased_upgrades["Faster Cooking"]:
            self.purchased_upgrades["Faster Cooking"] = True
            print("Bought Faster Cooking!")
            self.player.increase_cooking_speed()  
            
            
     def draw(self):
        """
        Draws the upgrade buttons and updates the game state
        """
        self.draw_upgrade_buttons()
        self.update_game_state()