class EventGenerator():
    """
    Abstract Event Manager class. Used in all game screens to notify listeners of
    user actions.
    """


    def __init__(self):
        self.__observers = []
    def addObserver(self, observer):
        self.__observers.append(observer)
    def notifyLoadScreenRequested(self,screen_name:str, TextEventID:str|None=None):
        for observer in self.__observers:
            observer.loadScreenRequested(screen_name, TextEventID)
    def notifyGameWon(self):
        for observer in self.__observers:
            observer.gameWon()
    def notifyGameLost(self):
        for observer in self.__observers:
            observer.gameLost()
    def notifyQuitRequested(self):
        for observer in self.__observers:
            observer.quitRequested()
    def notifyChangeValueRequested(self, key:str, value:int):
        for observer in self.__observers:
            observer.changeValueRequested(key, value)
    def notifyDayPassed(self):
        for observer in self.__observers:
            observer.dayPassed()
        pass
    def notifyFetchPlayer(self,player_type:str):
        for observer in self.__observers:
            observer.fetchPlayer(player_type)

    def processInput(self):
        raise NotImplementedError()
    def update(self):
        raise NotImplementedError()
    def render(self):
        pass