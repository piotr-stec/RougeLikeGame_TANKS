from actors import Player, Item, Opponent
import element as el
import random
import opponents_library
import curses


class RMap:
    map = [[el.Wall() for _ in range(30)] for _ in range(30)]
    items = []
    player: Player
    opponents = []
    opponents_types = [opponents_library.OpponentType.MS1, opponents_library.OpponentType.MS1,
                       opponents_library.OpponentType.MS1, opponents_library.OpponentType.MS1,
                       opponents_library.OpponentType.MS1]

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def set_items(self, LVL):
        for i in range(8):
            # 0-5 HEALING 6 - 10 GOLD AMMO 11-20 DEFAULT
            choice = random.randint(1, 20)
            quantity_default = random.randint(LVL, LVL+6)
            quantity_gold = random.randint(LVL-1, LVL+2)
            if choice <= 5:
                random_x = random.randint(1, self.size_x - 2)
                random_y = random.randint(1, self.size_y - 2)
                while not self.check_field(random_x, random_y):
                    random_x = random.randint(1, self.size_x - 2)
                    random_y = random.randint(1, self.size_y - 2)
                new_item = el.Healing(50 + (10 * LVL), random_x, random_y)
            if 5 < choice <= 10:
                random_x = random.randint(1, self.size_x - 2)
                random_y = random.randint(1, self.size_y - 2)
                while not self.check_field(random_x, random_y):
                    random_x = random.randint(1, self.size_x - 2)
                    random_y = random.randint(1, self.size_y - 2)
                new_item = el.GoldAmmo(quantity_gold, random_x, random_y)
            if 10 < choice <= 20:
                random_x = random.randint(1, self.size_x - 2)
                random_y = random.randint(1, self.size_y - 2)
                while not self.check_field(random_x, random_y):
                    random_x = random.randint(1, self.size_x - 2)
                    random_y = random.randint(1, self.size_y - 2)
                new_item = el.DefaultAmmo(quantity_default, random_x, random_y)

            self.items.append(new_item)
            self.map[new_item.x][new_item.y] = new_item

    def check_field(self, x, y):
        return self.map[x][y].character == " "

    def set_opponents(self):

        for i in range(5):
            random_x = random.randint(1, self.size_x - 2)
            random_y = random.randint(1, self.size_y - 2)
            while not self.check_field(random_x, random_y):
                random_x = random.randint(1, self.size_x - 2)
                random_y = random.randint(1, self.size_y - 2)
            new_opponent = Opponent(random_x, random_y, self.opponents_types[i])
            self.opponents.append(new_opponent)
            self.map[new_opponent.x][new_opponent.y] = new_opponent

    def set_opponents_BY_LVL(self, LVL):
        if LVL == 1:
            self.opponents_types = opponents_library.OpponentLvl1.opponentlv1
        elif LVL == 2:
            self.opponents_types = opponents_library.OpponentLvl2.opponentlv2
        elif LVL == 3:
            self.opponents_types = opponents_library.OpponentLvl3.opponentlv3
        elif LVL == 4:
            self.opponents_types = opponents_library.OpponentLvl4.opponentlv4
        elif LVL == 5:
            self.opponents_types = opponents_library.OpponentLvl5.opponentlv5
        elif LVL == 6:
            self.opponents_types = opponents_library.OpponentLvl6.opponentlv6
        elif LVL == 7:
            self.opponents_types = opponents_library.OpponentLvl7.opponentlv7
        elif LVL == 8:
            self.opponents_types = opponents_library.OpponentLvl8.opponentlv8
        else:
            self.opponents_types = opponents_library.OpponentLvl1.opponentlv1

    def set_player(self, hp_1, dmg, LVL, DefaultAmmo, GoldAmmo):
        random_x = random.randint(1, self.size_x - 2)
        random_y = random.randint(1, self.size_y - 2)
        while self.check_field(random_x, random_y) == False:
            random_x = random.randint(1, self.size_x - 2)
            random_y = random.randint(1, self.size_y - 2)
        self.player = Player(random_x, random_y, "player_tank", hp_1, dmg, LVL, DefaultAmmo, GoldAmmo)
        self.map[self.player.x][self.player.y] = self.player

    def update_player_pos(self, player: Player):
        try:
            if self.check_field(player.x, player.y):
                self.player = player
                self.map[player.x][player.y] = player
                self.map[player.prev_x][player.prev_y] = el.Floor()
            else:
                raise Exception(f"Field {player.x} {player.y} is occupied or off the map")
        except Exception as e:
            print(e)

    def random_move(self):
        key_move = random.randint(1, 4)
        if (key_move == 1):
            return 'w'
        elif key_move == 2:
            return 's'
        elif key_move == 3:
            return 'd'
        elif key_move == 4:
            return 'a'

    def move(self, opp, key):
        opp.prev_x = opp.x
        opp.prev_y = opp.y
        if key == "w":
            opp.x -= 1
        elif key == "s":
            opp.x += 1
        elif key == "a":
            opp.y -= 1
        elif key == "d":
            opp.y += 1
    def move_opp_in_fight(self, opp, key):
        opp.prev_x = opp.x
        opp.prev_y = opp.y
        if key == "w":
            opp.x -= 1
        elif key == "s":
            opp.x += 1
        elif key == "a":
            opp.y -= 1
        elif key == "d":
            opp.y += 1
        if self.check_field(opp.x, opp.y):
            self.map[opp.x][opp.y] = opp
            self.map[opp.prev_x][opp.prev_y] = el.Floor()
        else:
            opp.x = opp.prev_x
            opp.y = opp.prev_y

    def move_opponents(self):
        for opp in self.opponents:
            self.move(opp, self.random_move())
            if self.check_field(opp.x, opp.y):
                self.map[opp.x][opp.y] = opp
                self.map[opp.prev_x][opp.prev_y] = el.Floor()
            else:
                opp.x = opp.prev_x
                opp.y = opp.prev_y

    def delete_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            self.map[item.x][item.y] = el.Floor()
        else:
            raise Exception("Item not found in the map")

    def delete_opponent(self, opp: Opponent):
        if opp in self.opponents:
            self.opponents.remove(opp)
            self.map[opp.x][opp.y] = el.Floor()
        else:
            raise Exception("Opponent not found in the map")

    def find_opponent_in_range2(self, distance=1):
        for opponent in self.opponents:
            if (
                    abs(self.player.x - opponent.x) <= distance and
                    abs(self.player.y - opponent.y) <= distance
            ):
                return opponent
        return None

    def find_opponent_in_range(self, distance):
        for opponent in self.opponents:
            if (
                    abs(self.player.x - opponent.x) <= distance and
                    abs(self.player.y - opponent.y) <= distance
            ):
                if (self.player.x == opponent.x or self.player.y == opponent.y) and \
                        self.check_path_clear(self.player, opponent):
                    return opponent

        return None

    def find_player_in_range(self):
        for opponent in self.opponents:
            if (
                    abs(self.player.x - opponent.x) <= opponent.range and
                    abs(self.player.y - opponent.y) <= opponent.range
            ):
                if (self.player.x == opponent.x or self.player.y == opponent.y) and \
                        self.check_path_clear(self.player, opponent):
                    return opponent

        return None

    def check_path_clear(self, start, end):
        if start.x == end.x:
            step_y = 1 if start.y < end.y else -1
            for y in range(start.y + step_y, end.y, step_y):
                if isinstance(self.map[start.x][y], el.Wall):
                    return False
        elif start.y == end.y:
            step_x = 1 if start.x < end.x else -1
            for x in range(start.x + step_x, end.x, step_x):
                if isinstance(self.map[x][start.y], el.Wall):
                    return False

        return True

    def find_item_in_range(self, distance=1):
        for it in self.items:
            if (
                    abs(self.player.x - it.x) <= distance and
                    abs(self.player.y - it.y) <= distance
            ):
                return it
        return None

    def collect_item(self, it1):
        if isinstance(it1, el.Healing):
            self.player.hp += it1.health_points
        elif isinstance(it1, el.DefaultAmmo):
            self.player.ammo_inventory[0].quantity += it1.quantity
        elif isinstance(it1, el.GoldAmmo):
            self.player.ammo_inventory[1].quantity += it1.quantity
        self.delete_item(it1)

    def make_connections(self, centers):
        centers_list = list(centers)

        for i in range(len(centers_list) - 1):
            center1_x, center1_y = centers_list[i]
            center2_x, center2_y = centers_list[i + 1]

            for x in range(min(center1_x, center2_x), max(center1_x, center2_x) + 1):
                self.map[x][center1_y] = el.Floor()

            for y in range(min(center1_y, center2_y), max(center1_y, center2_y) + 1):
                self.map[center2_x][y] = el.Floor()

    def make_rooms(self, center_x, center_y, max_square):
        rows, cols = len(self.map), len(self.map[0])

        square_size = random.randint(2, max_square)

        region_to_replace = set()

        for i in range(max(0, center_x - square_size), min(rows, center_x + square_size + 1)):
            for j in range(max(0, center_y - square_size), min(cols, center_y + square_size + 1)):
                if i == 0 or j == 0 or i == self.size_x - 1 or j == self.size_y - 1:
                    pass
                else:
                    region_to_replace.add((i, j))

        for x, y in region_to_replace:
            self.map[x][y] = el.Floor()

    def generate_random_coordinates(self, num_coordinates):
        coordinates = set()

        for i in range(num_coordinates):
            if i % 4 == 0:
                center_x = random.randint(1, self.size_x - 2)
                center_y = random.randint(1, self.size_y - 2)
            elif i % 4 == 1:
                center_x = random.randint(self.size_x // 2, self.size_x - 2)
                center_y = random.randint(1, self.size_y - 2)
            elif i % 4 == 2:
                center_x = random.randint(1, self.size_x // 2)
                center_y = random.randint(self.size_y // 2, self.size_y - 2)
            else:
                center_x = random.randint(self.size_x // 2, self.size_x - 2)
                center_y = random.randint(self.size_y // 2, self.size_y - 2)

            coordinates.add((center_x, center_y))

        return coordinates

    def generate_map(self, num_rooms):
        self.map = [[" " for _ in range(self.size_y)] for _ in range(self.size_x)]

        # Fill the map with walls initially
        for i in range(self.size_x):
            for j in range(self.size_y):
                self.map[i][j] = el.Wall()
        cords = self.generate_random_coordinates(num_rooms)
        for cor in cords:
            center_x, center_y = cor
            self.make_rooms(center_x, center_y, 4)
        self.make_connections(cords)

    def printMap(self, stdscr):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if isinstance(element, Player):
                    stdscr.addch(element.x, element.y, element.character, curses.color_pair(1))
                elif isinstance(element, Opponent):
                    stdscr.addch(element.x, element.y, element.character, curses.color_pair(2))
                elif isinstance(element, el.Healing):
                    stdscr.addch(element.x, element.y, element.character, curses.color_pair(6))
                elif isinstance(element, el.DefaultAmmo):
                    stdscr.addch(element.x, element.y, element.character, curses.color_pair(5))
                elif isinstance(element, el.GoldAmmo):
                    stdscr.addch(element.x, element.y, element.character, curses.color_pair(4))
                else:
                    stdscr.addch(i, j, element.character, curses.color_pair(3))
            stdscr.addch('\n')
    def show_opponents(self):
        message = "OPPONENT TANKS ON MAP:\n"
        for opp in self.opponents:
            message += opp.info()
        return message

    def game_items_list(self):
        message = ("GAME ITEMS:\nD - Default Ammo\nG - Gold Ammo\nH - Healing - extra HP points\n")
        return message
    def display_message(self, message, win, pair):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        win.clear()
        win.addstr(message, curses.color_pair(pair) | curses.A_BOLD)
        win.addch('\n')
        win.refresh()
        key1 = ""

        while(key1!=ord('x') and key1!=ord('q')):
            key1 = win.getch()
            if key1 == ord('e'):
                win.clear()
                win.addstr(str(self.player.equipment_info()), curses.color_pair(1) | curses.A_BOLD)
                win.addstr("B - BACK", curses.color_pair(4) | curses.A_BOLD)
                win.refresh()
            elif key1 == ord('o'):
                win.clear()
                win.addstr(str(self.show_opponents()), curses.color_pair(2) | curses.A_BOLD)
                win.addstr("B - BACK", curses.color_pair(4) | curses.A_BOLD)
                win.refresh()

            elif key1 == ord('i'):
                win.clear()
                win.addstr(str(self.game_items_list()), curses.color_pair(1) | curses.A_BOLD)
                win.addstr("B - BACK", curses.color_pair(4) | curses.A_BOLD)
                win.refresh()
            if key1 == ord('b'):
                win.clear()
                win.addstr(message, curses.color_pair(pair) | curses.A_BOLD)
                win.addch('\n')
                win.refresh()
                # key1 = win.getch()

        win.clear()
        win.refresh()
        if key1 == ord('q'):
            return True
        else:
            return False


    def display_message2(self, message, win, pair):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        win.clear()
        win.refresh()
        win.addstr(message, curses.color_pair(pair) | curses.A_BOLD)
        win.addch('\n')



    def game_instruction(self, win, pair):
        message = "GAME INSTRUCTION:\nI - Items Characters\nE - Equipment\nO - Opponent Tanks\nC - Collect Item\nMoving " \
                  "keys: w, a, s, d\nQ - Quit Game\nX - Exit "
        return self.display_message(message, win, pair)



    def show_messages(self, message, stdscr):
        stdscr.addstr(message)

