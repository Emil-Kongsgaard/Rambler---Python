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
from src.constants import Constants as C
from src.State.Gamestate import StateofGame


class MainGameLoop(GamePlayer):
    def __init__(self) -> None:
        self.init_ui()
        self.gamestate = StateofGame()

    def init_ui(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(C.Window_size.value)
        pygame.display.set_caption(C.Caption.value)
        self.clock = pygame.time.Clock()
        self.running = True

        # initialize menu
        self.current_screen = "MainMenu"
        self.mainmenu = MainMenu(self.screen)
        self.mainmenu.addObserver(self)


    def run(self):
        while self.running:
            match self.current_screen:
                case C.MainMenu.value:
                    self.mainmenu.run()
                case C.CharacterSel.value:
                    self.CharSelect.run()
                case C.Figth.value:
                    self.Figth.run()   
                case _:
                    pygame.quit()

            pygame.display.update()
            self.clock.tick(C.Clock.value)
            pass
        pygame.quit()

    def quitRequested(self):
        self.running = False
        return None
    
    def loadScreenRequested(self,screen_name:str):
        match screen_name:
            case C.MainMenu.value:
                pass 
                #The mainmenu screen is created and observer is added during init
            case C.CharacterSel.value:
                self.CharSelect = CharSelect(self.screen)
                self.CharSelect.addObserver(self)
            case C.Figth.value:
                self.Figth = Figth_screen(self.screen)
                self.Figth.addObserver(self)
            case C.TextEventScreen.value:
                    TEdata = self.gamestate.pulltexteventfromqueue(self.current_screen)
                    if TEdata is not None:
                        self.TEScreen = TextEventScreen(self.screen, TEdata)
                        self.TEScreen.addObserver(self)
                    else:
                        pass   
            case _:
                pass
        
        self.current_screen = screen_name

    

if __name__ == '__main__':
    game = MainGameLoop()
    game.run()
        
        

