from fight_game.hero import Hero
from fight_game.utils import timer


class AD(Hero):

    def __init__(self, name, hp, power):
        super().__init__(name, 0.8 * hp, 1.2*power)


    @timer
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
