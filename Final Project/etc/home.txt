import pygame

class Home:
    def __init__(self, screen, font):
         """
         Initializes home object
         """
         self.screen = screen
        
         self.font = font
        
         self.button_rect = pygame.Rect(150, 250, 200, 50) 
        
         self.button_color = (0, 255, 0)  
        
         self.button_hover_color = (0, 200, 0)
        
         self.button_text = "Start Game"

    def initial_text(self):
        """
        args: none
        Displays homescreen text including name of game, etc.
        """
        self.screen.fill((0, 0, 0))  
        
        # Title text
        title_text = self.font.render("Welcome to Our Game", True, (255, 255, 255)) 
        
        self.screen.blit(title_text, (self.screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Instructions text
        instructions_text = self.font.render("Press the button to start!!", True, (255, 255, 255))
        
        self.screen.blit(instructions_text, (self.screen.get_width() // 2 - instructions_text.get_width() // 2, 200))

        # Draw the start button
        self.start_button()
        
        
        
    def start_button(self):
        """
        Creates a button object which if pressed starts the
        game and goes to a new screen 
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Check if the mouse is hovering over the button
        if self.button_rect.collidepoint(mouse_x, mouse_y):
            
            pygame.draw.rect(self.screen, self.button_hover_color, self.button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        
        # Draw the text on the button
        button_text = self.font.render(self.button_text, True, (255, 255, 255)) 
        self.screen.blit(button_text, (self.button_rect.centerx - button_text.get_width() // 2, 
                                       
                                      self.button_rect.centery - button_text.get_height() // 2))

