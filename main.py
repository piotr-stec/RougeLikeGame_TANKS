class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Item(Actor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.character = 'I'


class Opponent(Actor):
    def __init__(self, x, y, character):
        super().__init__(x, y)
        self.character = character


class Player(Actor):
    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.character = "@"
        self.name = name


class RMap:
    map = [[]]
    items = []
    player: Player
    opponents = []

    def load(self):
        for item in self.items:
            if self.check_field(item.x, item.y):
                self.map[item.x][item.y] = item.character
            else:
                raise Exception(f"Field {item.x} {item.y} is occupied")
        for opp in self.opponents:
            if self.check_field(opp.x, opp.y):
                self.map[opp.x][opp.y] = opp.character
            else:
                raise Exception(f"Field {opp.x} {opp.y} is occupied")
        if self.check_field(self.player.x, self.player.y):
            self.map[self.player.x][self.player.y] = self.player.character
        else:
            raise Exception(f"Field {self.player.x} {self.player.y} is occupied")

    def set_item(self, item: Item):
        if self.check_field(item.x, item.y):
            self.items.append(item)
        else:
            raise Exception(f"Field {item.x} {item.y} is occupied")

    def set_opponent(self, opp: Opponent):
        if self.check_field(opp.x, opp.y):
            self.opponents.append(opp)
        else:
            raise Exception(f"Field {opp.x} {opp.y} is occupied")

    def set_player(self, player: Player):
        if self.check_field(player.x, player.y):
            self.player = player
        else:
            raise Exception(f"Field {player.x} {player.y} is occupied")

    def delete_item(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            self.map[item.x][item.y] = "_"
        else:
            raise Exception("Item not found in the map")

    def delete_opponent(self, opp: Opponent):
        if opp in self.opponents:
            self.opponents.remove(opp)
            self.map[opp.x][opp.y] = "_"
        else:
            raise Exception("Opponent not found in the map")

    def check_field(self, x, y):
        if self.map[x][y] == "_":
            return True
        else:
            return False

    def printMap(self):
        for row in self.map:
            for element in row:
                if element == "_":
                    print(" ", end="")
                else:
                    print(element, end="")
            print()


# while True:
mapT = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "#", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "#", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]





