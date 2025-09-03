
import pygame
from src.Screens.Utils import Buttons, Screen
from src.constants import Constants


class MainMenu(Screen):

    def __init__(self,screen):
        super().__init__(screen)
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

    def _load_images(self):
        self.background_image = pygame.image.load(
            Constants.Placeholder_img.value)
        return None

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
        for key in self.Buttons.keys():
            self.Buttons[key]["rect"] = pygame.Rect(0,0,(screen_rect.w * self.rect_x_multiplier),self.rect_y)
            self.Buttons[key]["rect"].center = (screen_rect.centerx, (screen_rect.y + (self.menu_y_dist * i )))
            i += 1

        # render
        self.screen.fill(Constants.background_color.value)
        self._render_images()
        self.screen.blit(title_surface, title_rect)

        play_button = Buttons(self.Buttons["Play"])
        load_button = Buttons(self.Buttons["Load"])
        quit_button = Buttons(self.Buttons["Quit"])

        play_button.render()
        load_button.render()
        quit_button.render()

        return None

    def _update(self):
        pass


if __name__ == '__main__':
    pass