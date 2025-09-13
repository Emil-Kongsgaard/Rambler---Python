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
        pass

    def _render(self) -> None:
        pass

    def _processInput(self):
        for event in pygame.event.get():
            self._checkForQuit(event)
            self._highligt_buttons(event)
            self._handle_button_click(event)

    def _update(self) -> None:
        pass
    
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
                        for func_key in  self.Buttons[key]["function"].keys():
                            #The "function" holds a dict of lambda functions 
                            try:
                                self.Buttons[key]["function"][func_key]()
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
    def __init__(self,screen:pygame.Surface,Textevent) -> None:
        self.screen = screen
        self.Buttons = {"Positive_option": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Positive", 
                       "function": lambda: print("positive"), 
                       "state": Constants.ENABLED.value},
                       "Go_to_Next_text": 
                       {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "More...", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.ENABLED.value},
                       "Negative_option": 
                       {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "negative", 
                       "function": lambda: print("negative"), 
                       "state": Constants.ENABLED.value}
                      }
        self.screen_rect = self.screen.get_rect()
        self.menu_y_dist = 90
        self.rect_x_multiplier = 0.2
        self.rect_y = 60
        self.body_text = "aaaa"

    def render(self):
        textbox_outer = pygame.Rect(0,0,500,600)
        textbox_outer.center = self.screen_rect.center
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
        pygame.draw.rect(self.screen,Constants.HIGHLIGHTED_COLOR.value,(textbox_outer),width=15)
        pygame.draw.rect(self.screen,Constants.INNER_COLOR.value,inner_rect)
        self.screen.blit(title_surface,(title_rect))

        tb_text_font = pygame.font.Font(Constants.FONT.value, 18)
        y_diff = (textbox_outer.h - (title_rect.h + 30))
        new_line_start = 0
        line_no = 0
        for i in range(len(self.body_text)):
            text_str = self.body_text[new_line_start:i]
            (w,h) = tb_text_font.size(text_str)
            if (textbox_outer.w-40) < w < (textbox_outer.w-25):
                if text_str.endswith((" ",".",",","-")):
                    pass
                elif " " == text_str[-2]:
                    text_str = self.body_text[new_line_start:(i-2)]
                    i = i-1
                else: 
                    text_str = self.body_text[new_line_start:(i-1)] + "-"
                    i = i-1
                new_line_start = i
                text_surface = tb_text_font.render(
                text_str, True, Constants.F_COLOR.value)
                text_rect = text_surface.get_rect()
                text_rect.left = (textbox_outer.x+15)
                text_rect.top = textbox_outer.y+50 + ( 30 * line_no) 
                self.screen.blit(text_surface,(text_rect))
                line_no = line_no +1
            elif i == (len(self.body_text)-1): 
                #to handle last line of text 
                text_str = self.body_text[new_line_start:]
                text_surface = tb_text_font.render(
                text_str, True, Constants.F_COLOR.value)
                text_rect = text_surface.get_rect()
                text_rect.left = (textbox_outer.x+15)
                text_rect.top = textbox_outer.y+50 + ( 30 * line_no) 
                self.screen.blit(text_surface,(text_rect))
                line_no = line_no +1
            else:
                pass   
        
if __name__ == "__main":
    pass