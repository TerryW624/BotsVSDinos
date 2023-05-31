from random import choice

class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

class Robot:
    def __init__(self, name, weapon_one, weapon_two, weapon_three):
        self.name = name
        self.health = 100
        self.active_weapons = [weapon_one, weapon_two, weapon_three]
    
    def attack(self, dinosaur):
        weapon = input(f'''
{dinosaur.name} stands before you. What weapon do you use?
(1) {self.active_weapons[0].name}
(2) {self.active_weapons[1].name}
(3) {self.active_weapons[2].name}
''')
        if weapon == "1":
            print(f"{self.name} used {self.active_weapons[0].name} on {dinosaur.name} for {self.active_weapons[0].attack_power} damage!")
            dinosaur.health -= self.active_weapons[0].attack_power
        elif weapon == "2":
            print(f"{self.name} used {self.active_weapons[1].name} on {dinosaur.name} for {self.active_weapons[1].attack_power} damage!")
            dinosaur.health -= self.active_weapons[1].attack_power
        elif weapon == "3":
            print(f"{self.name} used {self.active_weapons[2].name} on {dinosaur.name} for {self.active_weapons[2].attack_power} damage!")
            dinosaur.health -= self.active_weapons[2].attack_power

class Fleet:
    def __init__(self, bot_one, bot_two, bot_three):
        self.name = "Bots"
        self.group = [bot_one, bot_two, bot_three]

class Dinosaur:
    def __init__(self, name, ability_one, ability_two, ability_three):
        self.name = name
        self.health = 100
        self.attack_powers = [ability_one, ability_two, ability_three]

    def attack(self, robot):
        ability = input(f'''
{robot.name} stands before you. What ability do you use?
(1) {self.attack_powers[0].name}
(2) {self.attack_powers[1].name}
(3) {self.attack_powers[2].name}
''')
        if ability == "1":
            print(f"{self.name} {self.attack_powers[0].name} on {robot.name} for {self.attack_powers[0].attack_power} damage!")
            robot.health -= self.attack_powers[0].attack_power
        elif ability == "2":
            print(f"{self.name} {self.attack_powers[1].name} on {robot.name} for {self.attack_powers[1].attack_power} damage!")
            robot.health -= self.attack_powers[1].attack_power
        elif ability == "3":
            print(f"{self.name} {self.attack_powers[2].name} on {robot.name} for {self.attack_powers[2].attack_power} damage!")
            robot.health -= self.attack_powers[2].attack_power

class Herd:
    def __init__(self, dino_one, dino_two, dino_three):
        self.name = "Dinos"
        self.group = [dino_one, dino_two, dino_three]
    
class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd
    
    def player_set_up(self):
        self.p1_group = self.choose_team()
        if self.p1_group == self.fleet:
            self.p2_group = self.herd
            print(f"Player 1 you are {self.fleet.name}!")
            print(f"Player 2 you are {self.herd.name}!")
        elif self.p1_group == self.herd:
            self.p2_group = self.fleet
            print(f"Player 1 you are {self.herd.name}!")
            print(f"Player 2 you are {self.fleet.name}!")

    def display_welcome(self):
        print('''
        Welcome to Bots Vs Dinos!
        ''')

    
    def choose_team(self):
        team = input('''
Player 1 choose your side of the battlefield. (1)Bots? OR (2)Dinos?
''')
        if team == "1":
            return self.fleet
        elif team == "2":
            return self.herd
        
    def p1_select_an_attack(self):
        groups = [self.p1_group.group, self.p2_group.group]
        attack_selection = input(f'''
Select your enemy to attack 
(1) {groups[1][0].name} {groups[1][0].health}
(2) {groups[1][1].name} {groups[1][1].health}
(3) {groups[1][2].name} {groups[1][2].health}
''')
        return attack_selection
    
    def p2_select_an_attack(self):
        groups = [self.p1_group.group, self.p2_group.group]
        attack_selection = input(f'''
Select your enemy to attack 
(1) {groups[0][0].name} {groups[0][0].health}
(2) {groups[0][1].name} {groups[0][1].health}
(3) {groups[0][2].name} {groups[0][2].health}
''')
        return attack_selection

    def choose_enemy_hit(self):
        groups = [self.p1_group.group, self.p2_group.group]
        for group in groups:
            for dinobot in group:
                if dinobot.health == 0:
                    print(f"{dinobot.name} is dead")
                    continue
                if dinobot.health > 0:
                    hit_or_miss_list = ["dino or bot", "Missed", "Missed", "dino or bot", "dino or bot", "dino or bot", "dino or bot", "dino or bot"]
                    attack_succeed_or_fail = choice(hit_or_miss_list)
                    attack_attempt = False
                    while attack_attempt == False:
                        if group == groups[0]:
                            if attack_succeed_or_fail == "dino or bot":
                                attack_selection = self.p1_select_an_attack()
                                if attack_selection == "1" and groups[1][0].health > 0:
                                    dinobot.attack(groups[1][0])
                                    attack_attempt = True
                                    if groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0: 
                                        break
                                elif attack_selection == "2" and groups[1][1].health > 0:
                                    dinobot.attack(groups[1][1])
                                    attack_attempt = True
                                    if groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0: 
                                        break
                                elif attack_selection == "3" and groups[1][2].health > 0:
                                    dinobot.attack(groups[1][2])
                                    attack_attempt = True
                                    if groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0: 
                                        break
                                else:
                                    if groups[1][0].health > 0 or groups[1][1].health > 0 or groups[1][2].health > 0: 
                                        print("Target not available")
                                    else:
                                        break
                            else:
                                print(f"{dinobot.name} {attack_succeed_or_fail}")
                                attack_attempt = True
                        elif group == groups[1]:
                            if attack_succeed_or_fail == "dino or bot":
                                attack_selection = self.p2_select_an_attack()
                                if attack_selection == "1" and groups[0][0].health > 0:
                                    dinobot.attack(groups[0][0])
                                    attack_attempt = True
                                    if groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0:
                                        break
                                elif attack_selection == "2" and groups[0][1].health > 0:
                                    dinobot.attack(groups[0][1])
                                    attack_attempt = True
                                    if groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0:
                                        break
                                elif attack_selection == "3" and groups[0][2].health > 0:
                                    dinobot.attack(groups[0][2])
                                    attack_attempt = True
                                    if groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0:
                                        break
                                else:
                                    if groups[0][0].health > 0 or groups[0][1].health > 0 or groups[0][2].health > 0: 
                                        print("Target not available")
                                    else:
                                        break
                            else:
                                print(f"{dinobot.name} {attack_succeed_or_fail}")
                                attack_attempt = True
                    if (groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0) or (groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0):
                        break
                if (groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0) or (groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0):
                    break
            if (groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0) or (groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0):
                break

    def battle_phase(self):
        groups = [self.p1_group.group, self.p2_group.group]
        has_health = True
        while has_health == True:
            if (groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0) or (groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0):
                has_health = False
                break
            else:
                self.choose_enemy_hit()

    def display_winner(self):
        groups = [self.p1_group.group, self.p2_group.group]
        if groups[0][0].health == 0 and groups[0][1].health == 0 and groups[0][2].health == 0:
            print(f"{self.p2_group.name} are the Winners!")
        elif groups[1][0].health == 0 and groups[1][1].health == 0 and groups[1][2].health == 0:
            print(f"{self.p1_group.name} are the Winners!")

    def run_game(self):
        self.display_welcome()
        self.player_set_up()
        self.battle_phase()
        self.display_winner()