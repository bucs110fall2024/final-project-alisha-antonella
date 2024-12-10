import pygame
import pygame_menu
from budgeting import Budgeting
from button import Button
from cooking import Cooking
from customer import Costumer
from music import Music
from player import Player

class Controller:
    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.fill((150, 150, 250))
        
        # setup menu(s) for the loop
        width, height = pygame.display.get_window_size()
        self.menu = pygame_menu.Menu("My Pizza Restaurant", width-20, height/2, position=(10,10), theme=pygame_menu.themes.THEME_BLUE)

        # a label allows you to add text on the page
        self.menu.add.label("Press to Start", max_char=-1, font_size=14)
        
        # a button creates a button you can link to a method
        self.menu.add.button('Start', self.start_game, align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        self.customer = None
        self.cooking = None
        self.supplies = None
        self.upgrades = None
        self.button = Button(x=50, y=self.menu.get_rect().bottom + 10)
        self.player = None 
        self.state = "menu"
        self.background = pygame.image.load("backgroundpic.jpg")
        self.background = pygame.transform.scale(self.background, pygame.display.get_window_size())
        self.music = Music("backgroundmusic.mp3")
        
    def start_game(self):
        """
        Initialize the game state when the start button is pressed
        """
        
        self.state = "game"
        self.customer = Costumer(100, 100, "paper_order.jpg", self.screen)
        self.cooking = Cooking(self.button, self.screen)
        self.player = Player(400, 300, "player_image2.jpg", budget=100, scale=(150,150))  
        
        

    def menuloop(self):
        while self.state == "menu":
            # you draw the menu on the screen like this
            self.screen.blit(self.background, (0, 0))
            if self.menu.is_enabled():
                # saved list of events from the event loop above
                self.menu.update(pygame.event.get())
                # You can draw the menu onto any surface
                self.menu.draw(self.screen)
                pygame.display.update()
        
    def gameloop(self):
        """
        menu elements must be defined before the mainloop
        """
        clock = pygame.time.Clock()  
        while self.state == "game":  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "menu"
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.cooking.cooking_button_click(event, self.screen)
                    self.cooking.button_click(event)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.x -= 5
            if keys[pygame.K_RIGHT]:
                self.player.x += 5
            if keys[pygame.K_UP]:
                self.player.y -= 5
            if keys[pygame.K_DOWN]:
                self.player.y += 5
            
            self.player.rect.topleft = (self.player.x, self.player.y)
            
            self.screen.fill((150, 150, 250))
            self.customer.display_order_image()  
            self.cooking.draw()  
            self.cooking.draw()
            self.screen.blit(self.player.image, self.player.rect)  
            self.cooking.update_game_state() 
            pygame.display.flip()
            
            clock.tick(60)

    def mainloop(self):
        while True:
            if self.state == "menu":
                self.menuloop()
            elif self.state == "game":
                self.gameloop()

    def gameoverloop(self):
        # Event loop, update data, and redraw
        pass