from random import randint, randrange

class Character():
    def __init__(self, basic_character:dict) -> None:
        self.Health:int = basic_character['hp']
        self.attack_dice:list = basic_character['att_dice'] #dice with 20 sides
        self.defense_score:int =  basic_character['def_score'] 

    @property
    def health(self):
        return self.Health
    @health.setter
    def Sethealth (self,health):
        self.Health = health

    @property
    def  attackdice (self):
        return self.attack_dice
    @attackdice.setter
    def SetAttDiceSmallest(self,number):
        self.attack_dice[0] = self.attack_dice[0] + number
    @attackdice.setter
    def SetAttDiceLargest(self,number):
        self.attack_dice[1] = self.attack_dice[1] + number
    @property
    def defenceScore (self):
        return self.defense_score
    
    @defenceScore.setter
    def SetDefenceScore (self,number):
        self.defense_score = self.defense_score + number


    @property
    def IsDead (self):
        if self.health > 0:
            return False
        else:
            return True