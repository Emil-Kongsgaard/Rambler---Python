class EventManager():
    """
    Abstract Event Manager class. Used in all game screens to notify listeners of
    user actions.
    """


    def __init__(self):
        self.__observers = []
    def addObserver(self, observer):
        self.__observers.append(observer)
    def notifyLoadScreenRequested(self):
        for observer in self.__observers:
            observer.loadScreenRequested()
    def notifyGameWon(self):
        for observer in self.__observers:
            observer.gameWon()
    def notifyGameLost(self):
        for observer in self.__observers:
            observer.gameLost()
    def notifyQuitRequested(self):
        for observer in self.__observers:
            observer.quitRequested()
        
    def processInput(self):
        raise NotImplementedError()
    def update(self):
        raise NotImplementedError()
    def render(self):
        raise NotImplementedError()