from operator import ne
import pygame
from src.Mode.GameEventManager import EventManager
from src.constants import Constants as C
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
                if self.Buttons[key]["state"] == C.DISABLED.value:
                    continue
                if self.Buttons[key]["rect"].collidepoint(pygame.mouse.get_pos()): 
                        for func_key in  self.Buttons[key]["function"].keys():
                            #The "function" holds a dict of lambda functions 
                            try:
                                self.Buttons[key]["function"][func_key]()
                            except Exception as e:
                                pass
    def _render_images(self) -> None:
        self.screen.blit(self.background_image, C.background_xy.value)

    def _highligt_buttons(self, event):
        if event.type == pygame.MOUSEMOTION:
            for key in self.Buttons.keys():
                if self.Buttons[key]["state"] == C.DISABLED.value:
                    continue
                if self.Buttons[key]["rect"].collidepoint(pygame.mouse.get_pos()):
                    self.Buttons[key]["state"] = C.HIGHLIGHTED.value
                else: 
                    self.Buttons[key]["state"] = C.ENABLED.value

class Buttons():
    """
    Class that handles the currect rendering of buttons. 
    """
    def __init__(self, iv_button:dict ):
        self.surface = iv_button["surface"]
        self._outer_rect = iv_button["rect"]
        self.text = iv_button["title"]
        self.state = iv_button["state"]
        self.font = C.FONT.value
        self.font_size = C.F_SIZE.value
        self.font_color = C.F_COLOR.value
        self.ENA_color = C.ENABLED_COLOR.value
        self.DIS_color = C.DISABLED_COLOR.value
        self.HIG_color = C.HIGHLIGHTED_COLOR.value
        return None
             
    def render(self):
        match self.state:
            case C.DISABLED.value:
                color = self.DIS_color
            case C.ENABLED.value:
                color = self.ENA_color
            case C.HIGHLIGHTED.value:
                color = self.HIG_color
            case _:
                raise UIError(errors=C.SYS_ERR,message="Attempted to set unkown state to button")
        #draw rect
        self.button = self._draw_button(color)


    def _draw_button(self,button_color):
        #prep:
        inner_margin = C.INNER_MARGIN.value
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
        inner_rect = pygame.draw.rect(self.surface,C.INNER_COLOR.value,inner_rect)
        self.text_rect = self.surface.blit(text_surface,(text_rect))
        return outer_rect
    
    def getButton(self):
        return self.button
    
    def getText(self):
        return self.text_rect

class TextBox():
    def __init__(self,screen:pygame.Surface,Textevent:dict) -> None:
        self.screen = screen
        # extract the inner dict from the Textevent dict
        for key in Textevent.keys():
            Textevent = Textevent[key]
            break
        self.Buttons = {"Positive_option": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": Textevent[C.POS_TITLE.value], 
                       "function": Textevent[C.POS_FUNCS.value], 
                       "state": Textevent[C.POS_BUT_ST.value]
                       },
                       "Negative_option": 
                       {"surface": self.screen, 
                       "rect": "rect", 
                       "title": Textevent[C.NEG_TITLE.value], 
                       "function": Textevent[C.NEG_FUNCS.value], 
                       "state": Textevent[C.NEG_BUT_ST.value]}
                      }
        self.screen_rect = self.screen.get_rect()
        self.menu_y_dist = 90
        self.rect_x_multiplier = 0.2
        self.rect_y = 60
        self.body_text = Textevent[C.B_TEXT.value]

        # cache for rendered line surfaces keyed by (body_text, font_path, font_size, max_width)
        self._line_cache: dict = {}

    def render(self):
        textbox_outer = pygame.Rect(0,0,500,600)
        textbox_outer.center = self.screen_rect.center
        inner_margin = C.INNER_MARGIN.value
        inner_x = textbox_outer.x + inner_margin
        inner_y = textbox_outer.y + inner_margin
        inner_w = textbox_outer.w - (2 * inner_margin)
        inner_h = textbox_outer.h - (2 * inner_margin)
        #inner_rect:
        inner_rect = pygame.Rect(inner_x,inner_y,inner_w,inner_h)

        tb_title_font = pygame.font.Font(C.FONT.value, 28)
        title_surface = tb_title_font.render(
            "Title for textbox", True, C.F_COLOR.value)
        title_rect = title_surface.get_rect()
        title_rect.center = (textbox_outer.centerx, (textbox_outer.y + 30))

        # draw
        pygame.draw.rect(self.screen,C.HIGHLIGHTED_COLOR.value,(textbox_outer),width=15)
        pygame.draw.rect(self.screen,C.INNER_COLOR.value,inner_rect)
        self.screen.blit(title_surface,(title_rect))

        tb_text_font = pygame.font.Font(C.FONT.value, 18)
        max_text_width = textbox_outer.w - 40

        # get cached line surfaces (build and cache on first use)
        line_surfaces = self._get_line_surfaces(tb_text_font, max_text_width)

        # blit the pre-rendered line surfaces
        line_no = 0
        for surf in line_surfaces:
            text_rect = surf.get_rect()
            text_rect.left = (textbox_outer.x+15)
            text_rect.top = textbox_outer.y+50 + ( 30 * line_no)
            self.screen.blit(surf, text_rect)
            line_no += 1

    def _get_line_surfaces(self, font: pygame.font.Font, max_text_width: int):
        """
        Return a list of rendered surfaces for each line of self.body_text.
        Results are cached per (body_text, font path, font size, max_width).
        """
        cache_key = (self.body_text, C.FONT.value, font.get_linesize(), max_text_width)
        cached = self._line_cache.get(cache_key)
        if cached is not None:
            return cached

        # simple word-wrapping that will hyphenate long words
        words = self.body_text.split(' ')
        lines = []
        current = ""
        for w in words:
            test = (current + " " + w) if current else w
            test_w, _ = font.size(test)
            if test_w <= max_text_width:
                current = test
            else:
                if current:
                    lines.append(current)
                # if single word too long, break it by characters with hyphenation
                if font.size(w)[0] > max_text_width:
                    part = ""
                    for ch in w:
                        testp = part + ch
                        if font.size(testp)[0] <= max_text_width:
                            part = testp
                        else:
                            lines.append(part + "-")
                            part = ch
                    if part:
                        current = part
                    else:
                        current = ""
                else:
                    current = w
        if current:
            lines.append(current)

        # render surfaces for each line and cache them
        surfaces = [font.render(line, True, C.F_COLOR.value) for line in lines]
        self._line_cache[cache_key] = surfaces
        return surfaces
        
if __name__ == "__main":
    pass