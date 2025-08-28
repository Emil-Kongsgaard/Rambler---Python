import os
from src.constants import Constants
from src.Screens.Buttons import Buttons
import pygame

#os.environ['SDL_VIDEO_CENTERED'] = '1'


WIDTH = 1024
HEIGTH = 640


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
        lv_h= self.window.get_height()# 720
        lv_w= self.window.get_width()# 1280
        #lower rigth
        margin = 60
        #upper rigt
        y1 = (lv_h-lv_h)+margin
        x1 = (lv_w-lv_w)+margin
        #upper rigth
        y2 = (lv_h-lv_h)+margin
        x2 = (lv_w-margin-60)
        #lower left 
        y3 = (lv_h-margin-60)
        x3 = (lv_w-lv_w)+margin
        #
        y4 = (lv_h-margin-60)
        x4 = (lv_w-margin-60)
        rect1 = pygame.Rect(x1,y1,240,90)

        self.test_button = Buttons(
            surface=self.window,
            rect= rect1,
            text= "Inventory",
            function= lambda: print("this is an action"),
            state= self.button_state
        )
        self.test_button.render()


        self.button_1 = self.test_button.getButton()
        #text_01 = self.test_button.getText()
        #print(self.button_1.contains(text_01))
        
        """
        #rect coordinates 
        rect_x =  int((lv_h*0.2))
        rect_y= int((lv_w*0.2))
        #print(lv_h)#x
        #print(lv_w)#y

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
        """
        pygame.display.update()   

    def processInput(self):     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.MOUSEMOTION:
                if self.button_1.collidepoint(pygame.mouse.get_pos()):
                    print("highligt button")
                    self.button_state = Constants.HIGHLIGHTED.value
                else:
                    self.button_state = Constants.ENABLED.value
                #if self.window.get_rect().collidepoint(pygame.mouse.get_pos()):
                    #print("i am touching the surface")
            if event.type == pygame.MOUSEBUTTONDOWN:
                print ("mousebottom down")
                if self.button_1.collidepoint(pygame.mouse.get_pos()):
                    try:  
                        self.test_button.clicked['action']()
                    except Exception as e:
                        pass


                    


    def run(self):
        while self.running:
            self.render()
            self.processInput()
            self.clock.tick(1)

userInterface = UserInterface()

print(pygame.font.get_fonts())