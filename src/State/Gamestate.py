
class StateofGame ():
    def __init__(self) -> None:
        player_char = None
        no_days_passed = None
        self.TextEvents = []
        pass
    def pulltexteventfromqueue(self, screen_name:str) -> dict|None:
        if len(self.TextEvents) > 0:
            return self.TextEvents.pop(0)
        else:
            return None
    