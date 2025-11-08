import pygame
from src.Screens.Utils import Screen
from src.constants import Constants
from src.Screens.Utils import Buttons


class Figth_screen (Screen):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.Buttons = {"Throw": 
                        {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Throw", 
                       "function":{ "1":   lambda: print("somefunction")
                                }, 
                       "state": Constants.ENABLED.value},
                       "Heal": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Heal", 
                       "function": { "1":   lambda: print("somefunction")
                                }, 
                       "state": Constants.ENABLED.value},
                        "Hit_Fast": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Hit Fast", 
                       "function": { "1":   lambda: print("somefunction")
                                }, 
                       "state": Constants.ENABLED.value},
                        "Hit_Slow": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Hit Slow", 
                       "function": { "1":   lambda: print("somefunction")
                                }, 
                       "state": Constants.ENABLED.value},
                        }
        # TODO: implement logic that asks Gamestate if buttons should be enabled or disabled based on players inventory

    def _load_images(self) -> None:
        self.background_image = pygame.image.load(
            Constants.Placeholder_img.value)
        self.EnemyCenter = pygame.image.load(
            Constants.main_enemy_plach.value)
        self.side_enemy_1 = pygame.image.load(
            Constants.side_enemy_plach.value)
        self.side_enemy_2 = pygame.image.load(
            Constants.side_enemy_plach.value)
        
        return None

    
    def _render_images(self) -> None:
        super()._render_images()
        return None
    
    def _render(self):
        super()._render()
        # build rects 
        screen_rect = self.background_image.get_rect()
        gamefont = pygame.font.Font(Constants.FONT.value, 32)
        title_surface = gamefont.render(
            "Figth for your life!", True, Constants.F_COLOR.value)
        title_rect = title_surface.get_rect()
        title_rect.center = (screen_rect.centerx, (screen_rect.y + 90))

        for key in self.Buttons.keys():
            self.Buttons[key]["rect"] = pygame.Rect(0,0,(screen_rect.w * Constants.Button_width_multp.value),Constants.Buttons_y.value)

        self.Buttons['Throw']['rect'].center = (int(screen_rect.w * 0.14),(screen_rect.h * 0.98))
        self.Buttons['Heal']['rect'].center = (int(screen_rect.w * 0.35 ),(screen_rect.h * 0.98))

        self.Buttons['Hit_Fast']['rect'].center = (int(screen_rect.w * 0.71),(screen_rect.h * 0.98))
        self.Buttons['Hit_Slow']['rect'].center = (int(screen_rect.w * 0.92),(screen_rect.h * 0.98))

        self.screen.fill(Constants.background_color.value)
        self._render_images()
        self.screen.blit(title_surface, title_rect)

        throw_but = Buttons(self.Buttons["Throw"])
        heal_but = Buttons(self.Buttons["Heal"])
        hitf_but = Buttons(self.Buttons["Hit_Fast"])
        hits_but= Buttons(self.Buttons["Hit_Slow"])
    
        throw_but.render()
        heal_but.render()
        hitf_but.render()
        hits_but.render()
       