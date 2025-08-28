
import pygame
from src.Screens.Screens import Screen
from src.constants import Constants


class MainMenu(Screen):
    _menuitems = {}
    def _load_images(self):
        self.background_image = pygame.image.load(Constants.Placeholder_img.value)
        return None
    
    def _render_images(self) -> None:
        self.screen.blit(self.background_image,Constants.background_xy.value)
        
    def _render(self):
        # prepare
        screen_rect = self.background_image.get_rect() 
        ##Screen title:
        gamefont = pygame.font.Font(r"C:\Users\Lenovo\Desktop\kode projekter\Rambler python Github clone\Rambler---Python\Assets\DuBellay-4B1Y.ttf",32)
        title_surface = gamefont.render("Welcome, weary traveller",True,Constants.F_COLOR.value) 
        title_rect = title_surface.get_rect()
        title_rect.center = (screen_rect.centerx,(screen_rect.y + 30))
        

        # render
        self.screen.fill(Constants.background_color.value)
        self._render_images()
        self.screen.blit(title_surface,title_rect)
        pygame.display.update()
        return None

    def _processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    def _update(self):
        pass


if __name__ == '__main__':
    menu = MainMenu()
    menu.run()