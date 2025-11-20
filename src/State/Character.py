# Define basic character templates
# might as well be hardcoded here for now. 
# In future, could be loaded from external file.
Farmer = {
    'Hp' : 100,
    'Morale' : 10,
    'Strength': 2,
    'Agility': 2,
    'Intelligence':1,
    }

Young_soldier = {
    'Hp' : 120,
    'Morale' : 10,
    'Strength': 4,
    'Agility': 3,
    'Intelligence':2,
}

Veteran_Officer = {
    'Hp' : 150, 
    'Morale' :13,
    'Strength': 4,
    'Agility': 2,
    'Intelligence':4, 
}
Yx_Bounty_Hunter = {
    'Hp' : 150,
    'Morale': 18,
    'Strength': 5,
    'Agility': 4,
    'Intelligence':3,
}

class Character():
    def __init__(self, basic_character:dict) -> None:
        self.health:int = basic_character['Hp']
        self.morale:int = basic_character['Morale']
        self.strength:int = basic_character['Strength']
        self.agility:int = basic_character['Agility']
        self.intelligence:int = basic_character['Intelligence']

    def IsDead (self):
        if self.health > 0:
            return False
        else:
            return True

class Player(Character):
    def __init__(self,character:dict) -> None:
        #Set basic character values
        super().__init__(character)
        pass
    def changevalue(self, attribute:str, change_number:int) -> None:
        """
        Changes a value of a player attribute by the given value. 
        value-signs (+ / -) are respected.
        Nothing is done on errors. Since it is internal function, errors should not occur.
        Valid attributes: "Hp", "Morale", "Strength", "Agility", "Intelligence"
        """
        match attribute:
            case "Hp":
                self.health += change_number
            case "Morale":
                self.morale += change_number
            case "Strength":
                self.strength += change_number
            case "Agility":
                self.agility += change_number
            case "Intelligence":
                self.intelligence += change_number
            case _:
                pass
        return None

                                                                                        
def GetPlayer(character_type:str) -> Player:
    """ Factory function to create a player of given character type. 
    Valid character types: "Farmer", "Young soldier", "Veteran Officer", "Yx. Bounty Hunter"
    Returns the created Player object.
    """
    match character_type:
        case "Farmer":
            player = Player(Farmer)
        case "Young soldier":
            player = Player(Young_soldier)
        case "Veteran Officer":
            player = Player(Veteran_Officer)
        case "Yx. Bounty Hunter":
            player = Player(Yx_Bounty_Hunter)
        case _:
            raise ValueError(f"Unknown character type requested: {character_type}")
    return player

def DiceRoll(player:Player, attribute:str) -> int:
    """
    Simulates a dice roll based on the given player's attribute.
    Returns an integer value representing the roll result.
    Valid attributes: "Strength", "Agility", "Intelligence"
    """
    import random
    base_roll = random.randint(1, 20)  # Simulate a d20 roll
    if base_roll == 20:
        return 100  # Critical success
    modifier = 0
    match attribute:
        case "Strength":
            modifier = player.strength
        case "Agility":
            modifier = player.agility
        case "Intelligence":
            modifier = player.intelligence
        case _:
            raise ValueError(f"Unknown attribute for dice roll: {attribute}")
    total_roll = base_roll + modifier
    return total_roll

    