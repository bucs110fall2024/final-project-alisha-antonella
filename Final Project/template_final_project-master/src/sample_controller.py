import pygame
import random
from budgeting import Budgeting
from cooking import Cooking
from costumer import Costumer
from home import Home
from music import Music
from player import Player
from supplies import Supplies
from upgrades import Upgrades 

class Controller:
  WIDTH = 800
  HEIGHT = 600
  
  def __init__(self, WIDTH, HEIGHT):
     pygame.init()
     screen = pygame.display.set_mode((WIDTH, HEIGHT))

  def mainloop(self):
    #select state loop
    
  
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
