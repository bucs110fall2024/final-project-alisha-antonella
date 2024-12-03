import pygame
import pygame_menu
from budgeting import Budgeting
from button import Button 
from cooking import Cooking
from costumer import Costumer
from home import Home
from music import Music
from player import Player
from supplies import Supplies
from upgrades import Upgrades 


class Controller:
    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background.fill((150, 150, 250))
        
        # setup menu(s) for the loop
        width, height=pygame.display.get_window_size()
        
        self.menu = pygame_menu.Menu("My Pizza Restaurant", width-20, height/2, position=(10,10))

        # a label allows you to add text on the page
        self.menu.add.label("Press to Start", max_char=-1, font_size=14)
        #a button creates a button you can link to a method
        self.menu.add.button('Press Me', self.start_game, align=pygame_menu.locals.ALIGN_CENTER)
        self.button = Button(x=50, y=self.menu.get_rect().bottom + 10)
        self.state = "menu"


    def menuloop(self):
        while self.state == "menu":
            # you draw the menu on the screen like this
            if self.menu.is_enabled():
                # saved list of events from the event loop above
                self.menu.update(pygame.event.get())
                # You can draw the menu onto any surface
                # so if you want the menu in a specific place, 
                # create a surface in the location to draw the menu on
                self.menu.draw(self.screen)
                if(False): self.state = "game"
            pygame.display.update()
      
        
    def gameloop(self):
        """
        menu elements must be defined before the mainloop
        """
        while self.state == "game":  # one time through the loop is one frame (picture)
            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "menu"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.menuloop()
                elif event.type == pygame.MOUSEMOTION:
                    if self.button.rect.collidepoint(event.pos):
                        self.button.highlight()
                    else:
                        self.button.color_default()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        self.reveal_hero()
        
            self.screen.blit(self.background, (0,0))
            self.background.blit(self.button.image, self.button.rect)

            # update the screen
            pygame.display.update()
       
            
    def mainloop(self):
        while True:
            if self.state == "menu":
                self.menuloop()
                #print(self.state)
            elif self.state == "game":
                self.gameloop()
    
    
    def gameoverloop(self):
      #event loop

      #update data

      #redraw
