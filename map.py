from actors import Player, Item, Opponent
import element as el
import random
import curses

class RMap:
    map = [[]]
    items = []
    player: Player
    opponents = []

    def load(self):
        for item in self.items:
            if self.check_field(item.x, item.y):
                self.map[item.x][item.y] = item
            else:
                raise Exception(f"Field {item.x} {item.y} is occupied")
        for opp in self.opponents:
            if self.check_field(opp.x, opp.y):
                self.map[opp.x][opp.y] = opp
            else:
                raise Exception(f"Field {opp.x} {opp.y} is occupied")
        # if self.check_field(self.player.x, self.player.y):
        #     self.map[self.player.x][self.player.y] = self.player.character
        # else:
        #     raise Exception(f"Field {self.player.x} {self.player.y} is occupied")

    def set_item(self, item: Item):
        try:
            if self.check_field(item.x, item.y):
                self.items.append(item)
            else:
                raise Exception(f"Field {item.x} {item.y} is occupied or off the map")
        except Exception as e:
            print(e)

    def set_opponent(self, opp: Opponent):
        try:
            if self.check_field(opp.x, opp.y):
                self.opponents.append(opp)
                self.map[opp.x][opp.y] = opp
            else:
                raise Exception(f"Field {opp.x} {opp.y} is occupied or off the map")
        except Exception as e:
            print(e)

    def set_player(self, player: Player):
        try:
            if self.check_field(player.x, player.y):
                self.player = player
                self.map[player.x][player.y] = player
            else:
                raise Exception(f"Field {player.x} {player.y} is occupied or off the map")
        except Exception as e:
            print(e)

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

    def check_field(self, x, y):
        try:
            return self.map[x][y].character == " "
        except IndexError:
            print("Fild is not available")


    def printMap(self, stdscr):
        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if isinstance(element, Player):
                    stdscr.addch(element.x, element.y, element.character)
                elif isinstance(element, Opponent):
                    stdscr.addch(element.x, element.y, element.character)
                else:
                    stdscr.addch(i, j, element.character)
            stdscr.addch("\n")


    def show_enemies(self,stdscr):
        print("OPPONENTS: ")
        for opp in self.opponents:
            stdscr.addstr(opp.info())




