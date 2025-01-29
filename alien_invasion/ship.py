import pygame 

class Ship: 
    """A class to manage the ship"""

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at the bottom centre of the screen .
        self.rect.midbottom = self.screen_rect.midbottom
    
    def biltme(self) :
        """draw the ship at its cureent location."""
        self.screen.blit(self.image,self.rect)