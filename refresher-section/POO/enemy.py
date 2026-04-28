class Enemy:
    type_of_enemy: str 
    health_points: int = 10 
    attack_damage: int = 1 

    #PARAMETER CONSTRUCTOR
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy #double underscore means the attribute is not public
        self.health_points = health_points
        self.attack_damage = attack_damage

    # getter of the private attribute
    def get_type_of_enemy(self):
        return self.__type_of_enemy    

    def talk(self):
        print(f" I am an enemy. Be prepared to fight!")
            
    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage.')
    
    def special_atack(self):
        print("Enemy has no special attack.")


#NOTES

    # default/ Empty constructor - it is automatically created if not written in the code
    #def __init__(self): # SELF: refers to the current class/object
    #    pass

    # NO ARGUMENT CONSTRUCTOR 
    # def __init__(self):
    #     print("New enemy created with no starting value")