from src.Exceptions import UIError
import pygame
from src.constants import Constants

class Buttons():

    def __init__(self, iv_button:dict ):
        self.surface = iv_button["surface"]
        self._outer_rect = iv_button["rect"]
        self.text = iv_button["title"]
        self.state = iv_button["state"]
        self.font = Constants.FONT.value
        self.font_size = Constants.F_SIZE.value
        self.font_color = Constants.F_COLOR.value
        self.ENA_color = Constants.ENABLED_COLOR.value
        self.DIS_color = Constants.DISABLED_COLOR.value
        self.HIG_color = Constants.HIGHLIGHTED_COLOR.value
        return None
             
    def render(self):
        match self.state:
            case Constants.DISABLED.value:
                color = self.DIS_color
            case Constants.ENABLED.value:
                color = self.ENA_color
            case Constants.HIGHLIGHTED.value:
                color = self.HIG_color
            case _:
                raise UIError(errors=Constants.SYS_ERR,message="Attempted to set unkown state to button")
        #draw rect
        self.button = self._draw_button(color)


    def _draw_button(self,button_color):
        #prep:
        inner_margin = Constants.INNER_MARGIN.value
        inner_x = self._outer_rect.x + inner_margin
        inner_y = self._outer_rect.y + inner_margin
        inner_w = self._outer_rect.w - (2 * inner_margin)
        inner_h = self._outer_rect.h - (2 * inner_margin)
        #inner_rect:
        inner_rect = pygame.Rect(inner_x,inner_y,inner_w,inner_h)

        # text_rect:
        gamefont = pygame.font.Font(self.font,self.font_size)
        text_surface = gamefont.render(self.text,True,self.font_color) 
        text_rect = text_surface.get_rect()
        text_rect.center = inner_rect.center

        #draw
        outer_rect = pygame.draw.rect(self.surface,button_color,(self._outer_rect),width=inner_margin)
        inner_rect = pygame.draw.rect(self.surface,Constants.INNER_COLOR.value,inner_rect)
        self.text_rect = self.surface.blit(text_surface,(text_rect))
        return outer_rect
    
    def getButton(self):
        return self.button
    
    def getText(self):
        return self.text_rect
        


                
                


if __name__ == "__main":
    pass