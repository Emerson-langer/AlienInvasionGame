import pygame
from pygame.sprite import Sprite

# This class manages the ship

class Ship(Sprite):
    # Initialize the ship and set its starting position
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads ship image and gets its rect
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False


    # Updates ship's position based on movement flag
    def update(self):
        # Updates ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x


    # Draws ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)


    # Center ship on screen
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)