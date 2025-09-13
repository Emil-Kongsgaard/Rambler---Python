import os
from pydoc import text
from src.constants import Constants
import pygame

#os.environ['SDL_VIDEO_CENTERED'] = '1'


WIDTH = 1024
HEIGTH = 640

lorem_ipsum = "Labore dolore aliquip ipsum consequat quis consectetur nisi labore dolor sed enim tempor ullamco sed tempor ex sit et do ut minim enim lorem incididunt dolore do aliqua nostrud nisi exercitation ut ex aliqua magna quis labore ex incididunt ullamco nisi enim sit nostrud dolor ex ut incididunt nostrud ullamco eiusmod veniam ea amet do ipsum ipsum ipsum ullamco enim ut consequat ad ex ut aliqua amet ipsum consequat aliquip ut ex ea incididunt consectetur magna consectetur ut ut adipiscing consectetur ipsum commodo magna consectetur dolor sit sed ullamco adipiscing dolore laboris dolor dolore dolore ut consequat consectetur incididunt ullamco ull."
class UserInterface():
    button_state = Constants.ENABLED.value
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(Constants.Window_size.value)
        self.placeholder = pygame.image.load(Constants.Placeholder_img.value)
        pygame.display.set_caption(Constants.Caption.value)
        #pygame.display.set_icon(pygame.image.load("icon.png"))
        self.clock = pygame.time.Clock()
        self.running = True

    def render(self):
        self.window.fill((0,0,0))
        self.window.blit(self.placeholder,(40,20))
        screen_rect = self.window.get_rect()
        lv_h= self.window.get_height()# 720
        lv_w= self.window.get_width()# 1280
        #------------------- Cut HERE ----------------#

   

        #------------------- Cut HERE ----------------#       
        pygame.display.update()   

    def processInput(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break


    def run(self):
        while self.running:
            self.render()
            self.processInput()
            self.clock.tick(60)

userInterface = UserInterface()
userInterface.run()
pygame.quit()