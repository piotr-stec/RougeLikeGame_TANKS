# import random
# import element as el
#
# class Actor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Item(Actor):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.character = 'I'
#
#
# class Opponent(Actor):
#     def __init__(self, x, y, name, hp, avg_dmg):
#         super().__init__(x, y)
#         self.character = "%"
#         self.name = name
#         self.hp = hp
#         self.avg_dmg = avg_dmg
#         self.armour = 0
#
#     def take_damage(self, damage):
#         actual_damage = damage - self.armour
#         self.hp -= actual_damage
#         print(f"{self.name} took {actual_damage} damage. Remaining HP: {self.health}")
#
#     def attack_enemy(self, enemy):
#         damage = random.randint(int(0.75*self.avg_dmg), int(1.25*self.avg_dmg))
#         print(f"{self.name} attacks {enemy.name} for {damage} damage.")
#         enemy.take_damage(damage)
#
#
# class Player(Actor):
#     def __init__(self, x, y, name, hp, avg_dmg):
#         super().__init__(x, y)
#         self.character = "@"
#         self.name = name
#         self.prev_x = x
#         self.prev_y = y
#         self.hp = hp
#         self.avg_dmg = avg_dmg
#         self.armour = 0
#
#     def move_player(self, key):
#         self.prev_x = self.x
#         self.prev_y = self.y
#         if key == "w":
#             self.x -= 1
#         elif key == "s":
#             self.x += 1
#         elif key == "a":
#             self.y -= 1
#         elif key == "d":
#             self.y += 1
#
#     def heal(self):
#         self.hp += 50
#
#     def info(self):
#         print("Position: "+str(self.x)+" "+str(self.y)+" "+"Health: "+str(self.hp)+" Avg_DMG: "+str(self.avg_dmg))
#
#     def take_damage(self, damage):
#         actual_damage = damage - self.armour
#         self.health -= actual_damage
#         print(f"{self.name} took {actual_damage} damage. Remaining HP: {self.health}")
#
#     def attack_enemy(self, enemy):
#         damage = random.randint(int(0.75*self.avg_dmg), int(1.25*self.avg_dmg))
#         print(f"{self.name} attacks {enemy.name} for {damage} damage.")
#         enemy.take_damage(damage)
#
#
#
#
#
#
# class RMap:
#     map = [[]]
#     items = []
#     player: Player
#     opponents = []
#
#     def load(self):
#         for item in self.items:
#             if self.check_field(item.x, item.y):
#                 self.map[item.x][item.y] = item.character
#             else:
#                 raise Exception(f"Field {item.x} {item.y} is occupied")
#         for opp in self.opponents:
#             if self.check_field(opp.x, opp.y):
#                 self.map[opp.x][opp.y] = opp.character
#             else:
#                 raise Exception(f"Field {opp.x} {opp.y} is occupied")
#         # if self.check_field(self.player.x, self.player.y):
#         #     self.map[self.player.x][self.player.y] = self.player.character
#         # else:
#         #     raise Exception(f"Field {self.player.x} {self.player.y} is occupied")
#
#     def set_item(self, item: Item):
#         try:
#             if self.check_field(item.x, item.y):
#                 self.items.append(item)
#             else:
#                 raise Exception(f"Field {item.x} {item.y} is occupied or off the map")
#         except Exception as e:
#             print(e)
#
#     def set_opponent(self, opp: Opponent):
#         try:
#             if self.check_field(opp.x, opp.y):
#                 self.opponents.append(opp)
#             else:
#                 raise Exception(f"Field {opp.x} {opp.y} is occupied or off the map")
#         except Exception as e:
#             print(e)
#
#     def set_player(self, player: Player):
#         try:
#             if self.check_field(player.x, player.y):
#                 self.player = player
#                 self.map[player.x][player.y] = "@"
#             else:
#                 raise Exception(f"Field {player.x} {player.y} is occupied or off the map")
#         except Exception as e:
#             print(e)
#
#     def update_player_pos(self, player: Player):
#         try:
#             if self.check_field(player.x, player.y):
#                 self.player = player
#                 self.map[player.x][player.y] = "@"
#                 self.map[player.prev_x][player.prev_y] = "_"
#             else:
#                 raise Exception(f"Field {player.x} {player.y} is occupied or off the map")
#         except Exception as e:
#             print(e)
#
#     def delete_item(self, item: Item):
#         if item in self.items:
#             self.items.remove(item)
#             self.map[item.x][item.y] = "_"
#         else:
#             raise Exception("Item not found in the map")
#
#     def delete_opponent(self, opp: Opponent):
#         if opp in self.opponents:
#             self.opponents.remove(opp)
#             self.map[opp.x][opp.y] = "_"
#         else:
#             raise Exception("Opponent not found in the map")
#
#     def check_field(self, x, y):
#         try:
#             return self.map[x][y] == "_"
#         except IndexError:
#             return False
#
#     def printMap(self):
#         for row in self.map:
#             for element in row:
#                 if element == "_":
#                     print(" ", end="")
#                 else:
#                     print(element, end="")
#             print()
#
#
# # while True:
# mapT = [
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "#", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "#", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "_", "_", "#", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
# ]
#
# Tmap = [
#     [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#     [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall()]
# ]
#
