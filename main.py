from robot_v_dinos_class import *

weapon_one = Weapon("Gatling Gun", 25)
weapon_two = Weapon("Buzzsaw", 25)
weapon_three = Weapon("Unibeam", 25)
ability_one = Weapon("Bite", 25)
ability_two = Weapon("Charging Ram", 25)
ability_three = Weapon("Tail Whip", 25)
tyranozill = Dinosaur("Tyranozill", ability_one, ability_two, ability_three)
megabronze = Robot("Bionic Baron", weapon_one, weapon_two, weapon_three)
battlefield = Battlefield(megabronze, tyranozill)
battlefield.run_game()
