from logging import PlaceHolder
import os
import pygame

#os.environ['SDL_VIDEO_CENTERED'] = '1'


WIDTH = 1024
HEIGTH = 640


class UserInterface():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.placeholder = pygame.image.load("1200x680.png")
        pygame.display.set_caption("Discover Python & Patterns - https://www.patternsgameprog.com")
        #pygame.display.set_icon(pygame.image.load("icon.png"))
        self.clock = pygame.time.Clock()
        self.running = True
    def processInput(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
    def render(self):
        self.window.fill((0,0,0))
        self.window.blit(self.placeholder,(40,20))
        lv_h= self.window.get_height()# 720
        lv_w= self.window.get_width()# 1280
        #rect coordinates 
        rect_x =  int((lv_h*0.2))
        rect_y= int((lv_w*0.2))
        #print(lv_h)#x
        #print(lv_w)#y
        margin = 20
        #upper rigt
        y1 = (lv_h-lv_h)+margin
        x1 = (lv_w-lv_w)+margin
        #lower left
        y2 = (lv_h-lv_h)+margin
        x2 = (lv_w-margin-60)
        #upper rigth
        y3 = (lv_h-margin-60)
        x3 = (lv_w-lv_w)+margin
        #lower rigth
        y4 = (lv_h-margin-60)
        x4 = (lv_w-margin-60)
        #pygame.draw.rect(surface =self.window,color=(0,0,255),rect=(rect_x,rect_y,120,120))

        pygame.draw.rect(surface=self.window,color=(0,0,255),rect=(x1,y1,60,60))
        pygame.draw.rect(surface=self.window,color=(0,255,0),rect=(x2,y2,60,60))
        pygame.draw.rect(surface=self.window,color=(0,0,255),rect=(x3,y3,60,60))
        pygame.draw.rect(surface=self.window,color=(0,0,255),rect=(x4,y4,60,60))
        #upper left
        pygame.draw.rect(surface=self.window,color=(0,255,0),rect=(0,0,30,30))
        #upper rigth
        pygame.draw.rect(surface=self.window,color=(0,0,255),rect=(1250,0,30,30))
        #Lower left
        pygame.draw.rect(surface=self.window,color=(0,255,0),rect=(0,690,30,30))
        #lower rigth
        pygame.draw.rect(surface=self.window,color=(0,0,255),rect=(1250,690,30,30))

        pygame.draw.rect(surface=self.window,color=(255,0,0),rect=(x1,y1,60,60))
        pygame.draw.rect(surface=self.window,color=(255,0,0),rect=(x2,y2,60,60))
        pygame.draw.rect(surface=self.window,color=(255,0,0),rect=(x3,y3,60,60))
        pygame.draw.rect(surface=self.window,color=(255,0,0),rect=(x4,y4,60,60))
        pygame.display.update()    

    def run(self):
        while self.running:
            self.processInput()
            self.render()
            self.clock.tick(1)

userInterface = UserInterface()

userInterface.run()

pygame.quit()