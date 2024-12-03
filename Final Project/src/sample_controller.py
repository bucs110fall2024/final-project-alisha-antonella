# from src.player import Player


#class Controller: (backup of old code)
 # WIDTH = 800
  #HEIGHT = 600
  
  #def __init__(self, WIDTH, HEIGHT):
     #pygame.init()
     #screen = pygame.display.set_mode((WIDTH, HEIGHT))
     
class Controller:
  
  #Light BG = ?
  
  def __init__(self):
    #pygame.init()
    #pygame.event.pump()
    
    #self.screen = pygame.display.set_mode()
    #setup pygame data
    #self.p1 = Player()
    #self.clouds = []
    #self.enemires = []
    
   def mainloop(self):
    #select state loop
    
      #while True:
        
        #1. Event loop
        #2. Updates
        #3. Redraw
        #completely overlay the screen
        #self.screen.fill("Red") OR self.background.fill
        #4. Display
  
  ### below are some sample loop states ###

    def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
     def gameloop(self):
      #event loop

      #update data

      #redraw
    
      def gameoverloop(self):
      #event loop

      #update data

      #redraw