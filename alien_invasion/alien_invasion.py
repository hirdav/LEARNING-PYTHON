import sys 
import pygame
from settings import Settings 
from ship import Ship 
class AlienInvasion :
    """ Overall Class to manage game assests and behavior"""

    def __init__(self) :
        """Initialize the game , and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("alien Invasion")
        self.ship=Ship(self)

        #setting bg color
        self.bg_color  = (230,230,230)
    def run_game(self) :
        """Start the main loop for the game."""
        while True : 
            #watch for keyboard and mouse events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()
            #Redraw the screen during each pass through the loop 
            self.screen.fill (self.settings.bg_color)
            self.ship.biltme()
            #make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)
if __name__== '__main__':
    #make a game instances , and run the game
    ai = AlienInvasion()
    ai.run_game()