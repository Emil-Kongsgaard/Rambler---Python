
import pygame
from src.Screens.Buttons import Buttons
from src.Screens.Screens import Screen
from src.constants import Constants


class MainMenu(Screen):

    def __init__(self,screen):
        super().__init__(screen)
        self._menuitems = {"Play": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Play", 
                       "function": lambda: print("somefunction"), 
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

    def _load_images(self):
        self.background_image = pygame.image.load(
            Constants.Placeholder_img.value)
        return None

    def _render_images(self) -> None:
        self.screen.blit(self.background_image, Constants.background_xy.value)

    def _render(self):
        # build Rects for all the buttons defined in __init__
        # plus Rect for title. 
        # self.menu_y_dist is the constant distance between all rects
        screen_rect = self.background_image.get_rect()
        gamefont = pygame.font.Font(Constants.FONT.value, 32)
        title_surface = gamefont.render(
            "Welcome, weary traveller", True, Constants.F_COLOR.value)
        title_rect = title_surface.get_rect()
        title_rect.center = (screen_rect.centerx, (screen_rect.y + self.menu_y_dist))
        i = 2
        for key in self._menuitems.keys():
            self._menuitems[key]["rect"] = pygame.Rect(0,0,(screen_rect.w * self.rect_x_multiplier),self.rect_y)
            self._menuitems[key]["rect"].center = (screen_rect.centerx, (screen_rect.y + (self.menu_y_dist * i )))
            i += 1

        # render
        self.screen.fill(Constants.background_color.value)
        self._render_images()
        self.screen.blit(title_surface, title_rect)

        play_button = Buttons(self._menuitems["Play"])
        load_button = Buttons(self._menuitems["Load"])
        quit_button = Buttons(self._menuitems["Quit"])

        self.play_but_rect = play_button.render()
        self.load_but_rect = load_button.render()
        self.quit_byt_rect = quit_button.render()

        return None

    def _processInput(self):
        for event in pygame.event.get():
            self._checkForQuit(event)
            self._highligt_buttons(event)
            self._handle_button_click(event)

    def _handle_button_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in self._menuitems.keys():
                if self._menuitems[key]["state"] == Constants.DISABLED.value:
                    continue
                if self._menuitems[key]["rect"].collidepoint(pygame.mouse.get_pos()):
                    try:  
                        self._menuitems[key]["function"]()
                    except Exception as e:
                        pass

    def _highligt_buttons(self, event):
        if event.type == pygame.MOUSEMOTION:
            for key in self._menuitems.keys():
                if self._menuitems[key]["state"] == Constants.DISABLED.value:
                    continue
                if self._menuitems[key]["rect"].collidepoint(pygame.mouse.get_pos()):
                    self._menuitems[key]["state"] = Constants.HIGHLIGHTED.value
                else: 
                    self._menuitems[key]["state"] = Constants.ENABLED.value


    def _update(self):
        pass


if __name__ == '__main__':
    pass