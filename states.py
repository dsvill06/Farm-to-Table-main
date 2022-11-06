"""Define functions for different states"""


from ui_element import UIElement, GameState, UIElementImage
import pygame
import constants
import images
from  sprite_set import Sprite


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def title_screen(screen):

    font = pygame.font.Font('../pygame_test/learning_curve_alt_G_bold_ot_tt.ttf', 64)
 
    # create a text surface object,
    text = font.render('Farm-to-Table', True, constants.BLACK)
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (constants.X // 2 +2, constants.Y // 3)
    
    # create ui elements
    korn = UIElementImage(
        center_position=(constants.X/2, 500),
        img='../pygame_test/images/Corn_A.png',
        action=GameState.KORN
    )
    quit_btn = UIElement(
        center_position=(50, 25),
        font_size=30,
        text_rgb=constants.BLACK,
        text="Quit",
        action=GameState.QUIT,
    )
    question_mark = UIElementImage(
        center_position = (750, 25),
        img = '../pygame_test/images/icons8-question-mark-48.png',
        action=GameState.QUESTION
    )
    
    buttons = [korn, quit_btn, question_mark]
 
    while True:
        mouse_up = False
        bg_1 = pygame.image.load("../pygame_test/images/Farm-to-Table StartScreen.png")
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
       

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
    
    
    
def korn(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    tractor = UIElementImage(
        center_position=(50,450),
        img="../pygame_test/images/John Deere Tractor.png",
        action=GameState.TRACTOR
    )
    buttons = [return_btn, tractor]
    text= f"The first step is to use the tractor on the land!\nClick on the tractor to go through the land!"
    font = pygame.font.SysFont("Courier",20)
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        blit_text(screen,text,(400,300),font)
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        

        pygame.display.flip()
        
def question_mark(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    #open text file in read mode
    text_file = open("../pygame_test/welcome.txt", "r")
    
    #read whole file to a string
    data = text_file.read()
    
    
    
    # set the center of the rectangular object.
   
    while True:
        mouse_up = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))

        font = pygame.font.SysFont('Courier', 25)

        blit_text(screen, data,(20,300),font)
        


        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)
        #close file
        text_file.close()
        pygame.display.flip()
    
        
        
def tractor(screen):
    tractor = Sprite(
        img="../pygame_test/images/John Deere Tractor.png",
        center_position=(0,450),

    )
    arrow = UIElementImage(
        center_position=(750,50),
        img="../pygame_test/images/output-onlinepngtools.png",
        action=GameState.SEED
    )
    
    font = pygame.font.SysFont('Courier', 25)
    # create a text surface object,
    text = ('The tractor moves along the field and plows it in order to make an area suitable for the seeds to grow!')
   
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/pixel-art-game-background-grass-sky-clouds_210544-60(14)(15)(16)(17)(18)(19)(20)(21)(22)(23)(24)(25)(26).png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        
        tractor.update_direction()
        tractor.draw(screen)

        
        ui_action = arrow.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        arrow.draw(screen)

        blit_text(screen, text,(400,300),font)
            
        pygame.display.flip()
        
    
    
def seed(screen):
    seed = UIElementImage(
        center_position=(725,70),
        img="../pygame_test/images/seed.png",
        action=GameState.PLANT
    )
    
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        text_rgb=constants.BLACK,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    text= "Now to plant the seeds!"
    font = pygame.font.SysFont("Courier",20)
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/addseeds.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 650)), (0, 0))
        blit_text(screen,text,(400,500),font)
        ui_action = seed.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        seed.draw(screen)
        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)
            
        pygame.display.flip()
        
        
def plant(screen):
    water_bucket = UIElementImage(
        center_position=(750, 70),
        img="../pygame_test/images/WateringCan3.png",
        action=GameState.GROW_1
    )
    font = pygame.font.SysFont("Courier", 25)
    text = "Time to give the seeds some water!"
    
    while True:
        mouse_up = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/seeds_added.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 650)), (0, 0))

        font = pygame.font.SysFont('Courier', 25)

        blit_text(screen, text,(20,150),font)


        ui_action = water_bucket.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        water_bucket.draw(screen)
        pygame.display.flip()
        
    
def grow_1(screen):
    arrow = UIElementImage(
        center_position=(750,50),
        img="../pygame_test/images/output-onlinepngtools.png",
        action=GameState.GROW_2
    )
    while True:
        mouse_up = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/Step_2_Farm.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))
        
        ui_action = arrow.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        arrow.draw(screen)
        
        pygame.display.flip()
      
    
    
def grow_2(screen):
    
    scythe = UIElementImage(
        center_position=(725,70),
        img="../pygame_test/images/Scythe2.png",
        action=GameState.FINISH
    )
    
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        bg_1 = pygame.image.load('../pygame_test/images/Step_3_Farm.png')
        screen.blit(pygame.transform.scale(bg_1, (800, 650)), (0, 0))
        ui_action = scythe.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        scythe.draw(screen)
        pygame.display.flip()
                      
        
def finish(screen):
    quit_btn = UIElement(
        center_position=(50, 25),
        font_size=30,
        text_rgb=constants.BLACK,
        text="Quit",
        action=GameState.QUIT,
    )

    while True:
        mouse_up = False
        bg_1 = pygame.image.load("../pygame_test/images/EndScreen.png")
        screen.blit(pygame.transform.scale(bg_1, (800, 600)), (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
  
        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        quit_btn.draw(screen)
        
        pygame.display.flip()
        
    