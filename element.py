class Field():
    def __init__(self):
        self.actor = None


class Wall():
    def __init__(self):
        self.name = "wall"
        self.character = "#"


class Floor():
    def __init__(self):
        self.name = "floor"
        self.character = "_"




class DefaultAmmo():
    def __init__(self):
        self.name = "Default Ammo"
        self.dmg_boost = 1
        self.quantity = 5


class GoldAmmo():
    def __init__(self):
        self.name = "Gold Ammo"
        self.dmg_boost = 1.15
        self.quantity = 5



