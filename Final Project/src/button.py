import pygame

class Button:
    def __init__(self, x, y, width=100, height=50, color=(0, 255, 0), text="Button"):
        """
       Initializes the button 
        Args:
        - x (int): The x-coordinate of the button's top-left corner
        - y (int): The y-coordinate of the button's top-left corner
        - width (int): The width of the button
        - height (int): The height of the button
        - color (tuple): RGB color tuple for the button 
        - text (str): The text displayed on the button
        """
        self.rect=pygame.Rect(x, y, width, height)
        self.color=color
        self.text=text
        self.font=pygame.font.Font(None, 30)

    def draw(self, screen):
        """
       Creates the button on the screen
       Args:
        - screen (pygame.Rect): The rectangle for the button
        """
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        """
        Handles the event if the button is clicked  
        Args:
        - event (pygame.event): when button is clicked 
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.rect.collidepoint(event.pos):
                return True
        return False