from random import choice

class Robot:
    def __init__(self, name, active_weapon):
        self.name = name
        self.health = 100
        self.active_weapon = active_weapon
    
    def attack(self, dinosaur):
        print(f"{self.name} used {weapon.name} on {dinosaur.name} for {weapon.attack_power} damage!")
        dinosaur.health -= weapon.attack_power

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 25

    def attack(self, robot):
        print(f"{self.name} used Eyebeam on {robot.name} for {self.attack_power} damage!")
        robot.health -= self.attack_power

class Weapon:
    def __init__(self, name):
        self.name = name
        self.attack_power = 25
    
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
        has_no_health = False
        dino_hit_or_miss_list = ["robot", "robot", "Missed", "robot", "robot", "robot", "robot", "Missed"]
        bot_hit_or_miss_list = ["dinosaur", "dinosaur", "Missed", "dinosaur", "dinosaur", "dinosaur", "dinosaur", "Missed"]
        while has_no_health == False:
            if first_attack == self.dinosaur:
                dino_attack_succeed_or_fail = choice(dino_hit_or_miss_list)
                if dino_attack_succeed_or_fail == "robot":
                    self.dinosaur.attack(self.robot)
                else:
                    print(f"{self.dinosaur.name} {dino_attack_succeed_or_fail}")
                if self.robot.health == 0:
                    has_no_health = True
                    continue
                bot_attack_succeed_or_fail = choice(bot_hit_or_miss_list)
                if bot_attack_succeed_or_fail == "dinosaur":
                    self.robot.attack(self.dinosaur)
                else:
                    print(f"{self.robot.name} {bot_attack_succeed_or_fail}")
                if self.dinosaur.health == 0:
                    has_no_health = True
                    continue
            elif first_attack == self.robot:
                bot_attack_succeed_or_fail = choice(bot_hit_or_miss_list)
                if bot_attack_succeed_or_fail == "dinosaur":
                    self.robot.attack(self.dinosaur)
                else:
                    print(f"{self.robot.name} {bot_attack_succeed_or_fail}")
                if self.dinosaur.health == 0:
                    has_no_health = True
                    continue
                dino_attack_succeed_or_fail = choice(dino_hit_or_miss_list)
                if dino_attack_succeed_or_fail == "robot":
                    self.dinosaur.attack(self.robot)
                else:
                    print(f"{self.dinosaur.name} {dino_attack_succeed_or_fail}")
                if self.robot.health == 0:
                    has_no_health = True
                    continue

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
