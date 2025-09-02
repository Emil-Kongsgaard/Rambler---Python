import pygame
from src.Mode.GameEventManager import EventManager
from src.constants import Constants


class Screen(EventManager):

    def __init__(self,screen:pygame.Surface):
        super().__init__()
        self.screen = screen
        self._load_images()

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
        self._render()
        self._processInput()
        self._update()

    def _checkForQuit(self,event:pygame.event.Event):
        if event.type == pygame.QUIT:
            self.notifyQuitRequested()
