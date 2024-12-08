import pygame
from controller import Controller

def main():
    """
    Initialize the game and run the main loop.
    """
    pygame.init()  # Initialize Pygame once here
    game = Controller()  # Create a controller instance
    game.mainloop()  # Start the main game loop

    # Optionally, you could add a cleanup here if needed (e.g., shutting down pygame)
    pygame.quit()  # Properly shut down Pygame when the game ends

# Ensures the script runs only when executed directly, not when imported as a module
if __name__ == '__main__':
    main()