import pygame
from src.Screens.Utils import Screen, Buttons
from src.constants import Constants


class CharSelect(Screen):

    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.Buttons = {"Character_1": 
                        {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Farmer", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.ENABLED.value},
                       "Character_2": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Young soldier", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.ENABLED.value},
                        "Character_3": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Veteran Officer", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.ENABLED.value},
                        "Character_4": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Yx. Bounty Hunter", 
                       "function": lambda: print("somefunction"), 
                       "state": Constants.ENABLED.value},
                       "Back": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Go Back", 
                       "function": lambda: self.notifyLoadScreenRequested(Constants.MainMenu.value), 
                       "state": Constants.ENABLED.value},
                       }
        # TODO: Implement some install-spefic logic that determines
        # if the buttons should be disabled. 
        # Eg, you have died as a farmer, now you can play as young soldier

        #local constants for placement of buttons
        self.rect_x_multiplier = 0.2
        self.rect_y = 60

    def _load_images(self) -> None:
        self.background_image = pygame.image.load(
            Constants.Placeholder_img.value)
        return None
    
    def _render(self) -> None:
        # build title rect 
        screen_rect = self.background_image.get_rect()
        gamefont = pygame.font.Font(Constants.FONT.value, 32)
        title_surface = gamefont.render(
            "Tell me, who are you traveller?", True, Constants.F_COLOR.value)
        title_rect = title_surface.get_rect()
        title_rect.center = (screen_rect.centerx, (screen_rect.y + 90))
        # The rects should be positioned in a scattered way
        for key in self.Buttons.keys():
            self.Buttons[key]["rect"] = pygame.Rect(0,0,(screen_rect.w * self.rect_x_multiplier),self.rect_y)
        self.Buttons["Character_1"]["rect"].center = (int(screen_rect.w * 0.33),int(screen_rect.h * 0.25))
        self.Buttons["Character_2"]["rect"].center = (int(screen_rect.w * 0.48),int(screen_rect.h * 0.35))
        self.Buttons["Character_3"]["rect"].center = (int(screen_rect.w * 0.67),int(screen_rect.h * 0.22))
        self.Buttons["Character_4"]["rect"].center = (int(screen_rect.w * 0.64),int(screen_rect.h * 0.45))
        self.Buttons["Back"]["rect"].center = (int(screen_rect.w * 0.93),(screen_rect.h * 0.98))

        # render
        self.screen.fill(Constants.background_color.value)
        self._render_images()
        self.screen.blit(title_surface, title_rect)

        char1_button = Buttons(self.Buttons["Character_1"])
        char2_button = Buttons(self.Buttons["Character_2"])
        char3_button = Buttons(self.Buttons["Character_3"])
        char4_button = Buttons(self.Buttons["Character_4"])
        back_button = Buttons(self.Buttons["Back"])

        char1_button.render()
        char2_button.render()
        char3_button.render()
        char4_button.render()
        back_button.render()
    
    def _update(self):
        pass