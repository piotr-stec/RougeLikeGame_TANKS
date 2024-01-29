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

    def display_message(self, message, win, pair):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        win.clear()
        win.addstr(message, curses.color_pair(pair) | curses.A_BOLD)
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
        self.character, self.name, self.hp, self.avg_dmg, self.range= opponent_type.value
        self.armour = 0

    def info(self):
        return "Character: " + str(self.character) + " Health: " + str(self.hp) + " Avg_DMG: " + str(
            self.avg_dmg) + " Range: " + str(self.range)+'\n'

    def take_damage(self, damage, game_map, stdscr, mapaTest):
        actual_damage = int(damage - self.armour)
        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            # self.display_message(f"{self.name} DEFEATED!", win, 1)
            stdscr.clear()
            mapaTest.printMap(stdscr)
            stdscr.addstr(f"\n{self.name} DEFEATED!\n", curses.color_pair(1))


            game_map.delete_opponent(self)
            stdscr.refresh()
        else:
            # self.display_message(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}", win, 1)
            stdscr.addstr(f"{self.name} took {actual_damage} damage. Remaining HP: {self.hp}\n", curses.color_pair(1))
            stdscr.refresh()
    def attack_player(self, enemy, win):
        if self.selected_ammo.quantity > 0:
            damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
            self.selected_ammo.quantity -= 1
            if self.selected_ammo.quantity == 0:
                self.switch_ammo("2")
            # win.addstr(f"{self.name} attacks {enemy.name} for {damage} damage.")
            enemy.take_damage(int(damage), win)
        else:
            pass


class Player(Actor):
    def __init__(self, x, y, name, hp, avg_dmg, LVL, DefaultQantity, GoldQuantity):
        super().__init__(x, y)
        self.character = "@"
        self.name = name
        self.prev_x = x
        self.prev_y = y
        self.hp = hp
        self.avg_dmg = avg_dmg
        self.armour = 0
        self.LVL = LVL
        self.range = 5
        self.ammo_inventory[0].quantity = DefaultQantity
        self.ammo_inventory[1].quantity = GoldQuantity

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

    def info(self):
        return ("Health: " + str(int(self.hp)) + " Avg_DMG: " + str(self.avg_dmg * self.selected_ammo.dmg_boost) \
               + " Selected Ammo: " + str(self.selected_ammo.name)+"("+str(self.selected_ammo.quantity)+")" +" LVL: "+str(self.LVL)+'\n')

    def equipment_info(self):
        message = "PLAYER EQUIPMENT:\n""Selected Ammo: " + str(self.selected_ammo.name) + "\nDefault Ammo quantity: " + str(
            self.ammo_inventory[0].quantity) + "\nGold Ammo quantity: " + str(self.ammo_inventory[1].quantity)+"\n"
        return message




    def LVL_UP(self, stdscr):
        stdscr.addstr(f"LEVEL UP!!!")



    def take_damage(self, damage, stdscr):
        actual_damage = int(damage - self.armour)

        self.armour = self.armour * 0.9
        self.hp -= actual_damage
        if self.hp <= 0:
            pass
            # self.display_message(f"{self.name} YOU LOST - KONIEC GRY!", win, 2)
        else:
            # self.display_message(f"You took {actual_damage} damage. Remaining HP: {self.hp}", win, 2)
            stdscr.addstr(f"You took {actual_damage} damage. Remaining HP: {int(self.hp)}\n", curses.color_pair(2))
            stdscr.refresh()


    def attack_enemy(self, enemy, game_map, stdscr, mapaTest, win):
        if (self.selected_ammo.quantity > 0):
            damage = random.randint(int(0.75 * self.avg_dmg), int(1.25 * self.avg_dmg)) * self.selected_ammo.dmg_boost
            self.selected_ammo.quantity -= 1
            # self.display_message(f"{self.name} attacks {enemy.name} for {damage} damage.", win)
            enemy.take_damage(int(damage), game_map, stdscr,mapaTest)
        else:
            self.display_message(f"YOU HAVE NO AMMO - COLLECT ITEMS ON MAP!", win, 4)

