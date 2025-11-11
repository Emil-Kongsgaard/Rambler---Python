import pygame
from src.Screens.Utils import Screen, TextBox
from src.constants import Constants as C

# here is sample text event
{"0000":  # idnumber
 {
     C.NAME.value: "template",
     C.REL_EVENTS.value: [],
     C.VERSION.value: "00",
     C.V_ORDER.value: "00",
     C.B_TEXT.value: "lorem ipsum....",
     C.POS_TITLE.value: 'Positive_option_title',
     C.POS_FUNCS.value: {   "1":   f"{C.ACTION_NEW_SCREEN.value}{C.Figth.value}_someparam",
                            "2":   f"{C.ACTION_NEW_SCREEN.value}{C.Figth.value}_someparam"
                        },
     C.POS_BUT_ST.value: 'Postive_button_state',
     C.NEG_TITLE.value: 'Negative_option_title',
     C.NEG_FUNCS.value: {   "1":   f"{C.ACTION_NEW_SCREEN.value}{C.Figth.value}_someparam",
                            "2":   f"{C.ACTION_NEW_SCREEN.value}{C.Figth.value}_someparam"
                        },
     C.NEG_BUT_ST.value: 'Negative_button_state'
 }} # pyright: ignore[reportUnusedExpression]

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

if __name__ == "__main__":
    pass
