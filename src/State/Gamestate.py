from typing import Text
from src.constants import Constants as C
from src.TextEvents.TextEvent import TextEvent
{"0000":  # idnumber
 {
     C.NAME.value: "template",
     C.REL_EVENT.value: '0000',
     C.VERSION.value: "00",
     C.CHARACTER.value: "Farmer",
     C.DAY.value: "0",
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


class StateofGame ():
    def __init__(self) -> None:
        self.Texteventobj = TextEvent()
        self.player_char_type = ""
        self.no_days_passed = 0
        self.TextEventsdict = self.Texteventobj.get()
        pass
    def pulltextevent(self, last_screen:str, ID:str|None=None) -> dict|None:
        # if we come from character selection screen, we need to load the first text event for that character
        # in normal scenario, we need pull based on day and character
        # if ID is not none, we pull based on ID
        #step 1
        if ID is not None:
            for id, data in self.TextEventsdict.items():
                if id == ID:
                    return data        
        #step 2    
        ids = []
        if last_screen == C.CharacterSel.value:
            for id, data in self.TextEventsdict.items():
                if data[C.CHARACTER.value] == self.player_char_type and data[C.DAY.value] == "0":
                    ids.append(id)  
            ids.sort()
            if len(ids) > 0:
                for id, data in self.TextEventsdict.items():
                    if id == ids[0]:
                        return data
        ids.clear()

        #step 3
        for id, data in self.TextEventsdict.items():
            if data[C.CHARACTER.value] == self.player_char_type and data[C.DAY.value] == str(self.no_days_passed):
                ids.append(id)  
            ids.sort()
            if len(ids) > 0:
                for id, data in self.TextEventsdict.items():
                    if id == ids[0]:
                        return data
        pass

    def advance_day(self) -> None:
        self.no_days_passed += 1
        return None
    def set_character_type(self, character:str) -> None:
        self.player_char_type = character
        return None
    


