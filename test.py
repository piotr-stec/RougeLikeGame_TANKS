import main as m


def test1():
    mapaTest = m.RMap()
    mapaTest.map = m.mapT
    it1 = m.Item(5, 2)
    it2 = m.Item(2, 9)
    op1 = m.Opponent(9, 10, "%")
    player = m.Player(13, 5, "Test")
    mapaTest.set_item(it1)
    mapaTest.set_item(it2)
    mapaTest.set_opponent(op1)
    mapaTest.set_player(player)

    mapaTest.load()
    mapaTest.printMap()

    mapaTest.delete_item(it2)
    mapaTest.delete_opponent(op1)

    mapaTest.printMap()

test1()