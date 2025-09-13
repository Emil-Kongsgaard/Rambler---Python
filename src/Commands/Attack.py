from src.State.Character import Character
from src.Commands.Command import Command

class Attack(Command):
        
        def attack(self,Attacking_char:Character, Defending_characters:list):
                # prepare
                
                
                        
                Attacking_char.attackdice


        #diceroll
        attack_value = randint(self.attack_dice[0],self.attack_dice[1])
        attack_value = attack_value - target.defense_score
        target.health = target.health - attack_value
        _class:str = "" #[Figther,Rouge,Wizard]
        _level:int = 1 # top level 10