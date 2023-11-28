import map as m
import element as el
import unittest
# UNITTEST python
def test1():
    mapaTest = m.RMap()
    Tmap = [
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall()]
    ]

    mapaTest.map = Tmap


    it1 = m.Item(5, 9)
    it2 = m.Item(2, 10)
    op1 = m.Opponent(9, 15, "opponent_tank1", 100, 40)
    op2 = m.Opponent(13, 20, "opponent_tank2", 150, 50)

    player = m.Player(9, 25, "player_tank", 300, 60)

    mapaTest.set_item(it1)
    mapaTest.set_item(it2)
    mapaTest.set_opponent(op1)
    mapaTest.set_opponent(op2)
    mapaTest.set_player(player)

    mapaTest.load()
    mapaTest.printMap()
    print(player.info())

    player.move_player("w")
    mapaTest.update_player_pos(player)

    player.move_player("w")
    mapaTest.update_player_pos(player)

    op1.attack_enemy(player)
    player.attack_enemy(op1, mapaTest)
    player.attack_enemy(op2, mapaTest)
    op1.attack_enemy(player)
    op1.attack_enemy(player)
    player.heal()
    player.heal()
    op1.attack_enemy(player)
    op1.attack_enemy(player)
    op1.attack_enemy(player)
    op1.attack_enemy(player)
    player.heal()
    op1.attack_enemy(player)
    op1.attack_enemy(player)



    while(op1 in mapaTest.opponents):
        player.attack_enemy(op1, mapaTest)

    mapaTest.printMap()
    mapaTest.show_enemies()

    while (op2 in mapaTest.opponents):
        player.attack_enemy(op2, mapaTest)
        #    mapaTest.delete_item(it2)
#    mapaTest.delete_opponent(op1)

    mapaTest.printMap()
    print(player.info())
    mapaTest.show_enemies()


test1()


class TestMethods(unittest.TestCase):
    pass