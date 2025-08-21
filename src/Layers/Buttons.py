import pygame
from src.Layers.UIConstants import UIConst

class Buttons():

    def __init__(self,surface,color,x,y,width,heigth,text,function) -> None:
        self.function = function
        font = UIConst.FONT.value
        font_size = UIConst.F_SIZE.value
        font_color = UIConst.F_COLOR.value
        # build rect
        button = pygame.draw.rect(surface,color,(x,y,width,heigth))
        # insert text in rect
        gamefont = pygame.font.SysFont(font,font_size)
        text = gamefont.render(text,True,font_color)
        text_rect = surface.blit(text,((x-10),(y+5)))
        #button.contains(text_rect)
    
    def SetState(self,State):
        pass



if __name__ == "__main":
    pass