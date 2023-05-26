from random import choice

class Robot:
    def __init__(self, name, active_weapon):
        self.name = name
        self.health = 100
        self.active_weapon = active_weapon
    
    def attack(self, dinosaur):
        print(f"{self.name} used {weapon.name} for {weapon.attack_power} damage!")
        dinosaur.health -= 100

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 100

    def attack(self, robot):
        print(f"{self.name} used Eyebeam on the robot for {self.attack_power} damage!")
        robot.health -= 100

class Weapon:
    def __init__(self, name):
        self.name = name
        self.attack_power = 100
    
class Battlefield:
    def __init__(self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur

    def display_welcome(self):
        weapon
        print('''
        Welcome to Bots Vs Dinos!
        ''')

    def battle_phase(self):
        combatants = [self.dinosaur, self.robot]
        first_attack = choice(combatants)
        if first_attack == self.dinosaur:
            self.dinosaur.attack(self.robot)
        elif first_attack == self.robot:
            self.robot.attack(self.dinosaur)
            

    def display_winner(self):
        if self.robot.health == 0:
            print(f"{self.dinosaur.name} is the Winner!")
        elif self.dinosaur.health == 0:
            print(f"{self.robot.name} is the Winner!")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

weapon = Weapon("gatling gun")
tyranozill = Dinosaur("Tyranozill")
megabronze = Robot("Megabronze", weapon)
battlefield = Battlefield(megabronze, tyranozill)
battlefield.run_game()
