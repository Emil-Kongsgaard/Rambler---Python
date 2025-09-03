class GamePlayer():
    """
    This is a abstract player class.
    The subclasses of this class can functions as observers/ listeners,
    to specific event publishers. 
    """
    def __init__(self) -> None:
        raise NotImplementedError
    def loadScreenRequested(self,screen_name:str):
        pass
    def gameWon(self):
        pass
    def gameLost(self):
        pass
    def quitRequested(self):
        pass