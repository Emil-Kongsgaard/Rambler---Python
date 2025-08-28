import os
from src.constants import Constants
from src.Screens.Buttons import Buttons
import pygame

class Screen():

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(Constants.Window_size.value)
        self._load_images()
        pygame.display.set_caption(Constants.Caption.value)
        self.clock = pygame.time.Clock()
        self.running = True

    def _load_images(self) -> None:
        raise NotImplemented
    
    def _render_images(self) -> None:
        raise NotImplemented

    def _render(self) -> None:
        raise NotImplemented
        

    def _processInput(self) -> None:
        raise NotImplemented     

    def _update(self) -> None:
        raise NotImplemented                    
         
    def run(self):
        while self.running:
            self._render()
            self._processInput()
            self._update()
            self.clock.tick(Constants.Clock.value)
        pygame.quit()
    
    def _checkForQuit(self):
        if event.type == pygame.QUIT: # pyright: ignore[reportUndefinedVariable]
            self.running = False
            
