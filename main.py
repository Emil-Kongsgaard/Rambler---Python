#inherit from gameobserver
# this will handle the main game loop,
# the switch between screens.
# the actual endgame, gamewon, "save?game?" implementations. 
import os
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
    
    def run(self):
        self.current_screen = "MainMenu"
        mainmenu = MainMenu(self.screen)
        mainmenu.addObserver(self)

        while self.running:
            match self.current_screen:
                case "MainMenu":
                    mainmenu.run()
                case _:
                    pygame.quit()

            pygame.display.update()
            self.clock.tick(Constants.Clock.value)
            pass
        pygame.quit()

    def quitRequested(self):
        self.running = False
        return None
    

if __name__ == '__main__':
    UI = UserInterface()
    UI.run()
        
        

