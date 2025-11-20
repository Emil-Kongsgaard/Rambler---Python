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
    REL_EVENT = "RelatedEvents"
    VERSION = "Version"
    CHARACTER = "Character"
    DAY = "Day"
    B_TEXT = "BodyText"
    POS_TITLE = 'Positive_option_title'
    POS_FUNCS = 'Postive_functions'
    POS_BUT_ST = 'Postive_button_state'
    NEG_TITLE = 'Negative_option_title'
    NEG_FUNCS = 'Negative_functions'
    NEG_BUT_ST = 'Negative_button_state'

    #TE Validations
    NAMELENGTH = 20
    IDNUMBERLENGTH = 4
    VERSIONLENGTH = 2
    VORDERLENGTH = 2
    BODYTEXTLENGTH = 600

    #TE actions
    ACTION_NEW_SCREEN = "NEW_SCREEN"
    ACTION_CHANGE_VALUE = "CHANGE_VAL"

    #Text
    FONT = os.path.join("Assets","DuBellay-4B1Y.ttf")
    F_SIZE = 24 # there can be 17 characters in a button with this font
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

    #Screens
    Button_width_multp = 0.2
    Buttons_y = 60
    MainMenu = "MainMenu"
    CharacterSel = "CharacterSelection"
    Figth = "Figth"
    TextEventScreen = "TextEventScreen"



    # Images:
    main_enemy_plach = os.path.join("Assets","Main_enemy_300x400.png")
    side_enemy_plach =  os.path.join("Assets","side_enemy_250x300.png")
