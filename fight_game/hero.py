


class Hero:

    def __init__(self,name,hp,power):
        self.name=name
        self.hp=hp
        self.power=power

    def speak(self):
        print(f"The hp and power of current hero: {self.name} are {self.hp},{self.power}")

    def fight(self, enemy_name, enemy_hp, enemy_power):
        # get final hp og current hero
        my_final_hp = self.hp - enemy_power
        # get final hp of enemy
        enemy_final_hp = enemy_hp - self.power
        if my_final_hp > enemy_final_hp:
            print(f"{self.name} win")
        elif enemy_final_hp > my_final_hp:
            print(f"The enemy: {enemy_name} win")
        else:
            print("The game ended in a draw")
