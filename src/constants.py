from enum import Enum

class Constants(Enum):
    #Exceptions:
    SYS_ERR = "SYSTEM ERROR"
    INP_ERR = "INPUT ERROR"
    
    #JSON file handling:
    JSON_INDENT = 4

    #TextEvent:
    NAME = "Name"
    REL_EVENTS = "RelatedEvents" 
    VERSION = "Version"
    V_ORDER ="ViewOrder"
    B_TEXT = "BodyText"