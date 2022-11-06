import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import constants



def create_surface_with_text(text, font_size, text_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # assign button action
        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

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
        
class UIElementImage(Sprite):
    """ An user interface element that can be added to a surface """
    
    def __init__(self,center_position, img, action=None):
        """
        Args:
            center_position - tuple (x, y)
            img-str location of image file
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = pygame.image.load(img)
        default_image = pygame.transform.scale(default_image, (default_image.get_width(), default_image.get_height()))

        highlighted_image = pygame.transform.scale(default_image, (default_image.get_width()*1.25, default_image.get_height()*1.25))

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        
        self.action = action

        super().__init__()
    
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

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
        """Creates a moving simulation horizontally"""
        self.rect.x += 2
        if self.rect.x > 100:
            return self.action
 
    
        
  
        
        
class GameState(Enum):
    QUIT = -1
    TITLE = 0
    KORN = 1
    MILK = 2
    QUESTION = 3
    TRACTOR = 4
    SEED = 5
    PLANT = 6
    GROW_1 = 7
    GROW_2 = 8
    FINISH = 9
    
    