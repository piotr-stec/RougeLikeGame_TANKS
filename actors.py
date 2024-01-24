import random
import opponents_library
from element import GoldAmmo, DefaultAmmo
import curses

class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ammo_inventory = [DefaultAmmo(10,0,0), GoldAmmo(5,0,0)]
        self.selected_ammo = self.ammo_inventory[0]

    def switch_ammo(self, AmmoNumber):
        if AmmoNumber == "1":
            self.selected_ammo = self.ammo_inventory[0]
        elif (AmmoNumber == "2"):
            self.selected_ammo = self.ammo_inventory[1]

    def display_message(self, message, win):
        win.addstr(message, curses.A_BOLD)
        win.addch('\n')
        win.getch()


class Item(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.character = 'I'


class Opponent(Actor):
    def __init__(self, x, y, opponent_type: opponents_library.OpponentType):
        super().__init__(x, y)
        self.prev_x = x
        self.prev_y = y
        self.character, self.name, self.hp, self.avg_dmg = opponent_type.value
        self.armour = 0

    def info(self):
        return "Name: " + str(self.name) + " Character: " + str(self.character) + " Position: " + str(
            self.x) + " " + str(self.y) + " Health: " + str(self.hp) + " Avg_DMG: " + str(
            self.avg_dmg) + " Selected Ammo: " + str(self.selected_ammo.name) + " | Default Ammo quantity: " + str(
            self.ammo_inventory[0].quantity) + " Gold Ammo quantity: " + str(self.ammo_inventory[1].quantity)




    def take_damage(self, damage, game_map, win):
        actual_damage = damage - self.armour
        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            self.display_message(f"{self.name} DEFEATED!", win)
            game_map.delete_opponent(self)
        else:
            self.display_message(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}", win)

    def attack_player(self, enemy, win):
        if (self.selected_ammo.quantity > 0):
            damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
            self.selected_ammo.quantity -= 1
            # win.addstr(f"{self.name} attacks {enemy.name} for {damage} damage.")
            enemy.take_damage(damage, win)
        else:
            pass


class Player(Actor):
    def __init__(self, x, y, name, hp, avg_dmg, LVL):
        super().__init__(x, y)
        self.character = "@"
        self.name = name
        self.prev_x = x
        self.prev_y = y
        self.hp = hp
        self.avg_dmg = avg_dmg
        self.armour = 0
        self.LVL = LVL

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



    def heal(self, win):
        self.hp += 50
        self.display_message("HEALING", win)

    def info(self, stdscr):
        stdscr.addstr("Health: " + str(self.hp) + " Avg_DMG: " + str(self.avg_dmg * self.selected_ammo.dmg_boost) \
               + " Selected Ammo: " + str(self.selected_ammo.name)+"("+str(self.selected_ammo.quantity)+")" +" LVL: "+str(self.LVL)+'\n')

    def LVL_UP(self, stdscr):
        stdscr.addstr(f"LEVEL UP!!!")



    def take_damage(self, damage, win):
        actual_damage = damage - self.armour
        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            self.display_message(f"{self.name} YOU LOST - KONIEC GRY!",win)
        else:
            self.display_message(f"You took {actual_damage} damage. Remaining HP: {self.hp}", win)


    def attack_enemy(self, enemy, game_map, win):
        if (self.selected_ammo.quantity > 0):
            damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
            self.selected_ammo.quantity -= 1
            # self.display_message(f"{self.name} attacks {enemy.name} for {damage} damage.", win)
            enemy.take_damage(damage, game_map, win)
        else:
            # win.clear()
            # win.addstr("Brak Amunicji!!!")
            pass