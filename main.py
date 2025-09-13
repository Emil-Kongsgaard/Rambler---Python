#inherit from gameobserver
# this will handle the main game loop,
# the switch between screens.
# the actual endgame, gamewon, "save?game?" implementations. 
import os
from src.Screens.Figth import Figth_screen
from src.Screens.CharSelect import CharSelect
import pygame
from src.Screens.MainMenu import MainMenu
from src.Mode.GamePlayer import GamePlayer
from src.constants import Constants


class UserInterface(GamePlayer):
    def __init__(self) -> None:
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(Constants.Window_size.value)
        pygame.display.set_caption(Constants.Caption.value)
        self.clock = pygame.time.Clock()
        self.running = True

        # initialize menu
        self.current_screen = "MainMenu"
        self.mainmenu = MainMenu(self.screen)
        self.mainmenu.addObserver(self)

        Text_events = []
        
    
    def run(self):


        while self.running:
            match self.current_screen:
                case Constants.MainMenu.value:
                    self.mainmenu.run()
                case Constants.CharacterSel.value:
                    self.CharSelect.run()
                case Constants.Figth.value:
                    self.Figth.run()   
                case _:
                    pygame.quit()

            pygame.display.update()
            self.clock.tick(Constants.Clock.value)
            pass
        pygame.quit()

    def quitRequested(self):
        self.running = False
        return None
    
    def loadScreenRequested(self,screen_name:str):
        match screen_name:
            case Constants.MainMenu.value:
                pass 
                #The mainmenu screen is created and observer is added during init
            case Constants.CharacterSel.value:
                self.CharSelect = CharSelect(self.screen)
                self.CharSelect.addObserver(self)
            case Constants.Figth.value:
                    self.Figth = Figth_screen(self.screen)
                    self.Figth.addObserver(self)   
            case _:
                pass
        
        self.current_screen = screen_name

    

if __name__ == '__main__':
    UI = UserInterface()
    UI.run()
        
        

