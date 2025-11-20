import os
import json
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
                       "function":{ "1":   lambda: self.notifyFetchPlayer("Farmer"),
                                    "2":   lambda: self.notifyLoadScreenRequested(Constants.Figth.value)
                                }, 
                       "state": Constants.ENABLED.value},
                       "Character_2": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Young soldier", 
                       "function": { "1":   lambda: self.notifyFetchPlayer("Young soldier"),
                                    "2":   lambda: self.notifyLoadScreenRequested(Constants.Figth.value)
                                }, 
                       "state": Constants.ENABLED.value},
                        "Character_3": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Veteran Officer", 
                       "function": { "1":   lambda: self.notifyFetchPlayer("Veteran Officer"),
                                    "2":   lambda: self.notifyLoadScreenRequested(Constants.Figth.value)
                                }, 
                       "state": Constants.ENABLED.value},
                        "Character_4": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Yx. Bounty Hunter", 
                       "function": { "1":   lambda: self.notifyFetchPlayer("Yx. Bounty Hunter"),
                                    "2":   lambda: self.notifyLoadScreenRequested(Constants.Figth.value)
                                }, 
                       "state": Constants.ENABLED.value},
                       "Back": 
                      {"surface": self.screen, 
                       "rect": "rect", 
                       "title": "Go Back", 
                       "function": { "1":   lambda: print("somefunction"),
                                     "2": lambda: self.notifyLoadScreenRequested(Constants.MainMenu.value)
                                }, 
                       "state": Constants.ENABLED.value},
                       }
        # apply install / profile specific availability rules
        self._apply_install_logic()

    def _load_images(self) -> None:
        self.background_image = pygame.image.load(
            Constants.Placeholder_img.value)
        return None

    def _apply_install_logic(self) -> None:
        """
        Read a small player profile at data/player_profile.json (if present)
        and modify button availability.

        Supported profile keys (both optional):
          - unlocked: list of titles that should be enabled (if present, only these enabled)
          - dead: list of titles that should be disabled

        If neither key exists, leave default button states unchanged.
        """
        try:
            profile_path = os.path.join(os.getcwd(), "data", "player_profile.json")
            if not os.path.isfile(profile_path):
                return
            with open(profile_path, "r", encoding="utf-8") as fh:
                profile = json.load(fh)
        except Exception:
            # on error, leave defaults unchanged
            return

        unlocked = profile.get("unlocked")
        dead = profile.get("dead")

        # If unlocked list present: enable only those titles
        if isinstance(unlocked, list):
            unlocked_set = set(unlocked)
            for btn in self.Buttons.values():
                title = btn.get("title")
                if title and title in unlocked_set:
                    btn["state"] = Constants.ENABLED.value
                else:
                    btn["state"] = Constants.DISABLED.value
            return

        # Otherwise, if dead list present: disable those titles
        if isinstance(dead, list):
            dead_set = set(dead)
            for btn in self.Buttons.values():
                title = btn.get("title")
                if title and title in dead_set:
                    btn["state"] = Constants.DISABLED.value
    
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
            self.Buttons[key]["rect"] = pygame.Rect(0,0,(screen_rect.w * Constants.Button_width_multp.value),Constants.Buttons_y.value)
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