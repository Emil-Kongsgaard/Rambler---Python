
from src.State.Character import Character

character = {
    'hp' : 150,
    'morale' : 20,
    'att_dice': [1,20],
    'def_score': 5,
    'level': 0,
    'class': None,
    'exp':0,
    'Attributes':{
        'Strength': 2,
        'Agility': 2,
        'Intelligence':1,
    },
    'Skills': ['skill_1', 'skill_2'],
    'Gear':{
            'head':None,
            'body':None,
            'legs':None,
            'boots':None,
            'Rhand':None,
            'Lhand':None,
                },
    'Bag':{'1':None,
    },
    'Quests': ['Main quest'],
    


}




class Player(Character):
    def __init__(self,character:dict) -> None:
        #Set basic character values
        super().__init__(character)
        self.morale = character['morale']
        self.level = character['level']
        self.rgp_class = character['class']
        self.experiece = character['exp']

        self.strength = character['Attributes']['Strength']
        self.agility = character['Attributes']['Agility']
        self.intelligence = character['Attributes']['Intelligence']
        
        self.equipped_gear = character['Gear']
        self.bag = character['Bag']

        self.quest = character['Quests']

        self.skills = character['Skills']