import os
from enum import Enum

class Constants(Enum):
    #Exceptions:
    SYS_ERR = "SYSTEM ERROR"
    INP_ERR = "INPUT ERROR"
    
    #JSON file handling:
    JSON_INDENT = 4
    JSON_FILEPATH = os.getcwd() + "/data/eventdata.json"

    #TextEvent:
    NAME = "Name"
    REL_EVENTS = "RelatedEvents" 
    VERSION = "Version"
    V_ORDER ="ViewOrder"
    B_TEXT = "BodyText"

    #Text
    FONT = os.path.join("Assets","DuBellay-4B1Y.ttf")
    F_SIZE = 24
    F_COLOR = (100,100,100)

    #Buttons
    DISABLED = "D"
    ENABLED = "E"
    HIGHLIGHTED = "H"
    DISABLED_COLOR = (0.92,0.98,0.85)
    ENABLED_COLOR = (27,27,27)
    HIGHLIGHTED_COLOR = (141,141,141)
    INNER_COLOR = (0,0,0)
    INNER_MARGIN = 10

    #UI init
    background_color = (0,0,0)
    background_xy = (40,20)
    Placeholder_img = os.path.join("Assets","1200x680.png")
    Window_size = (1280, 720)
    Caption = "Rambler"
    Clock = 60
