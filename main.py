from robot_v_dinos_class import *

weapon_one = Weapon("Gatling Gun", 25)
weapon_two = Weapon("Buzzsaw", 25)
weapon_three = Weapon("Unibeam", 25)
ability_one = Weapon("Bite", 25)
ability_two = Weapon("Charging Ram", 25)
ability_three = Weapon("Tail Whip", 25)
weapon = input('''
Tyranozill stands before you. What weapon do you use?
(1) Gatling Gun
(2) Buzzsaw
(3) Unibeam
''')
ability = input('''
Bionic Baron stands before you. What ability do you use?
(1) Bite
(2) Charging Ram
(3) Tail Whip
''')
tyranozill = Dinosaur("Tyranozill", ability)
megabronze = Robot("Bionic Baron", weapon)
battlefield = Battlefield(megabronze, tyranozill)
battlefield.run_game()
