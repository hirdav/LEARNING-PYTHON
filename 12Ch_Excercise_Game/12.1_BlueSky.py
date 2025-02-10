##12-1. Blue Sky: Make a Pygame window with a blue background

import sys 
import pygame
class Bluesky : 
    """making a blue background pygame"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption ("Alien_Capture")
        #set the bg color
        self.bg_color = (230,250,230)
    def run_game(self):
    
        """start the loop for input action """
        while True :
            for event in pygame.event.get():
                  if event.type==pygame.QUIT:
                       pygame.quit()
                       sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
game = Bluesky()  # Creates an instance
game.run_game()
