import random
import opponents_library
from element import GoldAmmo, DefaultAmmo


class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ammo_inventory = [DefaultAmmo(), GoldAmmo()]
        self.selected_ammo = self.ammo_inventory[0]

    def switch_ammo(self):
        if self.selected_ammo == DefaultAmmo:
            self.selected_ammo = self.ammo_inventory[1]
        else:
            self.selected_ammo = self.ammo_inventory[0]


class Item(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.character = 'I'


class Opponent(Actor):
    def __init__(self, x, y, opponent_type: opponents_library.OpponentType):
        super().__init__(x, y)
        self.character = "%"
        self.name, self.hp, self.avg_dmg = opponent_type.value
        self.armour = 0

    def info(self):
        return "Name: " + str(self.name) + " Character: " + str(self.character) + " Position: " + str(
            self.x) + " " + str(self.y) + " Health: " + str(self.hp) + " Avg_DMG: " + str(
            self.avg_dmg) + " Default Ammo quantity: " + str(
            self.ammo_inventory[0].quantity) + " Gold Ammo quantity: " + str(self.ammo_inventory[1].quantity)

    def take_damage(self, damage, game_map):
        actual_damage = damage - self.armour
        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            game_map.delete_opponent(self)
            print(f"{self.name} DEFEATED!")
        else:
            print(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}")

    def attack_enemy(self, enemy):
        damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
        self.selected_ammo.quantity -= 1
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)


class Player(Actor):
    def __init__(self, x, y, name, hp, avg_dmg):
        super().__init__(x, y)
        self.character = "@"
        self.name = name
        self.prev_x = x
        self.prev_y = y
        self.hp = hp
        self.avg_dmg = avg_dmg
        self.armour = 0

    def move_player(self, key):
        self.prev_x = self.x
        self.prev_y = self.y
        if key == "w":
            self.x -= 1
        elif key == "s":
            self.x += 1
        elif key == "a":
            self.y -= 1
        elif key == "d":
            self.y += 1

    def heal(self):
        self.hp += 50
        print("HEALING")

    def info(self):
        return "Name: " + str(self.name) + " Character: " + str(self.character) + " Position: " + str(
            self.x) + " " + str(self.y) + " Health: " + str(self.hp) + " Avg_DMG: " + str(self.avg_dmg)

    def take_damage(self, damage):
        actual_damage = damage - self.armour
        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            print(f"{self.name} DEFEATED - KONIEC GRY!")
            print(f"{self.name} przegrałeś - KONIEC GRY")
        else:
            print(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}")

    def attack_enemy(self, enemy, game_map):
        damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
        self.selected_ammo.quantity -= 1
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage, game_map)
