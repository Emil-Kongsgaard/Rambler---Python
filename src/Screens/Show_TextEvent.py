import pygame
from src.Screens.Utils import Screen, TextBox
from src.constants import Constants as C
import src.TextEvents.ActionHandler as ActionHandler


class TextEventScreen(Screen):
    def __init__(self, screen: pygame.Surface, text_event: dict):
        super().__init__(screen)
        self.text_event = text_event
        self.textbox = TextBox(self.screen, self.text_event)


    def _load_images(self) -> None:
        self.background_image = pygame.image.load(
            C.Placeholder_img.value)
        return None

    def _render(self) -> None:
 
        # render
        self.screen.fill(C.background_color.value)
        self._render_images()
        self.textbox.render()

    def _handle_button_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in self.Buttons.keys():
                if self.Buttons[key]["state"] == C.DISABLED.value:
                    continue
                if self.Buttons[key]["rect"].collidepoint(pygame.mouse.get_pos()): 
                        for func_key in  self.Buttons[key]["function"].keys():
                            #when dealing with textevents the function dict contains a string that needs to be parsed with internal logic in action handler. 
                            ActionHandler.Handle(
                            self.Buttons[key]["function"][func_key],#action string
                            self #screen for executing the action
                            )

    
if __name__ == "__main__":
    pass
