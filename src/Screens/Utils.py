import pygame
from src.Mode.GameEventManager import EventManager
from src.constants import Constants
from src.Exceptions import UIError

class Screen(EventManager):
    """
    Abstract class that handles all the common functionality between all screens
    """
    Buttons={}

    background_image: pygame.Surface
    def __init__(self,screen:pygame.Surface):
        super().__init__()
        self.screen = screen
        self._load_images()

    def _load_images(self) -> None:
        raise NotImplemented

    def _render(self) -> None:
        raise NotImplemented

    def _processInput(self):
        for event in pygame.event.get():
            self._checkForQuit(event)
            self._highligt_buttons(event)
            self._handle_button_click(event)

    def _update(self) -> None:
        raise NotImplemented
    
    def run(self):
        self._render()
        self._processInput()
        self._update()

    def _checkForQuit(self,event:pygame.event.Event):
        if event.type == pygame.QUIT:
            self.notifyQuitRequested()
    
    def _handle_button_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in self.Buttons.keys():
                if self.Buttons[key]["state"] == Constants.DISABLED.value:
                    continue
                if self.Buttons[key]["rect"].collidepoint(pygame.mouse.get_pos()):
                    try:  
                        self.Buttons[key]["function"]()
                    except Exception as e:
                        pass
    def _render_images(self) -> None:
        self.screen.blit(self.background_image, Constants.background_xy.value)

    def _highligt_buttons(self, event):
        if event.type == pygame.MOUSEMOTION:
            for key in self.Buttons.keys():
                if self.Buttons[key]["state"] == Constants.DISABLED.value:
                    continue
                if self.Buttons[key]["rect"].collidepoint(pygame.mouse.get_pos()):
                    self.Buttons[key]["state"] = Constants.HIGHLIGHTED.value
                else: 
                    self.Buttons[key]["state"] = Constants.ENABLED.value

class Buttons():
    """
    Class that handles the currect rendering of buttons. 
    """
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

class TextBox():
    def __init__(self) -> None:
        self.Buttons = {"Play": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Play", 
                       "function": lambda: self.notifyLoadScreenRequested(Constants.CharacterSel.value), 
                       "state": Constants.ENABLED.value},
                       "Load": 
                       {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Load a save", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.DISABLED.value},
                       "Quit": 
                       {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Quit", 
                       "function": lambda: self.notifyQuitRequested(), 
                       "state": Constants.ENABLED.value}
                      }
        self.menu_y_dist = 90
        self.rect_x_multiplier = 0.2
        self.rect_y = 60

    def render(self):
        textbox_outer = pygame.Rect(0,0,500,600)
        textbox_outer.center = screen_rect.center
        inner_margin = Constants.INNER_MARGIN.value
        inner_x = textbox_outer.x + inner_margin
        inner_y = textbox_outer.y + inner_margin
        inner_w = textbox_outer.w - (2 * inner_margin)
        inner_h = textbox_outer.h - (2 * inner_margin)
        #inner_rect:
        inner_rect = pygame.Rect(inner_x,inner_y,inner_w,inner_h)

        tb_title_font = pygame.font.Font(Constants.FONT.value, 28)
        title_surface = tb_title_font.render(
            "Title for textbox", True, Constants.F_COLOR.value)
        title_rect = title_surface.get_rect()
        title_rect.center = (textbox_outer.centerx, (textbox_outer.y + 30))

        # draw
        pygame.draw.rect(self.window,Constants.HIGHLIGHTED_COLOR.value,(textbox_outer),width=15)
        pygame.draw.rect(self.window,Constants.INNER_COLOR.value,inner_rect)
        self.window.blit(title_surface,(title_rect))

        tb_text_font = pygame.font.Font(Constants.FONT.value, 18)
        y_diff = (textbox_outer.h - (title_rect.h + 30))
        new_line_start = 0
        line_no = 0
        for i in range(len(lorem_ipsum)):
            text_str = lorem_ipsum[new_line_start:i]
            (w,h) = tb_text_font.size(text_str)
            if (textbox_outer.w-40) < w < (textbox_outer.w-25):
                if text_str.endswith((" ",".",",","-")):
                    pass
                elif " " == text_str[-2]:
                    text_str = lorem_ipsum[new_line_start:(i-2)]
                    i = i-1
                else: 
                    text_str = lorem_ipsum[new_line_start:(i-1)] + "-"
                    i = i-1
                new_line_start = i
                text_surface = tb_text_font.render(
                text_str, True, Constants.F_COLOR.value)
                text_rect = text_surface.get_rect()
                text_rect.left = (textbox_outer.x+15)
                text_rect.top = textbox_outer.y+50 + ( 30 * line_no) 
                self.window.blit(text_surface,(text_rect))
                line_no = line_no +1
            elif i == (len(lorem_ipsum)-1): 
                #to handle last line of text 
                text_str = lorem_ipsum[new_line_start:]
                text_surface = tb_text_font.render(
                text_str, True, Constants.F_COLOR.value)
                text_rect = text_surface.get_rect()
                text_rect.left = (textbox_outer.x+15)
                text_rect.top = textbox_outer.y+50 + ( 30 * line_no) 
                self.window.blit(text_surface,(text_rect))
                line_no = line_no +1
            else:
                pass   
        
if __name__ == "__main":
    pass