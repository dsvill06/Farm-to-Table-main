"""Module to represent a chess set, and individual pieces."""
import pygame
import constants
class Sprite(pygame.sprite.Sprite):
    def __init__(self, img, center_position, action=None):
        
  
        self.image = pygame.image.load(img)
        
    
        self.rect = self.image.get_rect(center=center_position)
        self.action = action
 
    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)
    def update_direction(self):
        self.rect.x += 3
        if self.rect.x > 100:
            return
        