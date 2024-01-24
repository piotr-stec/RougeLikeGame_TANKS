class Field():
    def __init__(self):
        self.actor = None


class Wall():
    def __init__(self):
        self.name = "wall"
        self.character = '#'


class Floor():
    def __init__(self):
        self.name = "floor"
        self.character = ' '


class Healing():
    def __init__(self,health_points, x, y):
        self.x = x
        self.y = y
        self.health_points = health_points
        self.name = "healing potion"
        self.character = 'H'





class DefaultAmmo():
    def __init__(self, quantity, x, y):
        self.x = x
        self.y = y
        self.name = "Default Ammo"
        self.character = "D"
        self.dmg_boost = 1
        self.quantity = quantity


class GoldAmmo():
    def __init__(self, quantity, x, y):
        self.x = x
        self.y = y
        self.name = "Gold Ammo"
        self.character = "G"
        self.dmg_boost = 1.15
        self.quantity = quantity



