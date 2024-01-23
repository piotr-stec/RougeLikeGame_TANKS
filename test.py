import map as m
import element as el
import unittest
from opponents_library import OpponentType
import curses
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

    while(op2 in mapaTest.opponents):
        player.attack_enemy(op2, mapaTest)
        #    mapaTest.delete_item(it2)
#    mapaTest.delete_opponent(op1)

    mapaTest.printMap()
    print(player.info())
    mapaTest.show_enemies()


def test2():
    mapaTest = m.RMap()
    Tmap = [
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall()]
    ]

    mapaTest.map = Tmap

    player = m.Player(9, 25, "player_tank", 300, 60)

    MS1 = m.Opponent(5, 15, OpponentType.MS1)
    T28 = m.Opponent(8, 23, OpponentType.T28)
    KV85 = m.Opponent(13, 13, OpponentType.KV85)
    IS3 = m.Opponent(12, 27, OpponentType.IS3)
    IS7 = m.Opponent(13, 21, OpponentType.IS7)

    tanks = [MS1, T28, KV85, IS3, IS7]

    mapaTest.set_player(player)




    for tank in tanks:
        mapaTest.set_opponent(tank)
        mapaTest.player.hp = 300
        while(tank in mapaTest.opponents and player.hp > 0):
            if(player.selected_ammo.quantity==0 and player.selected_ammo.name == "Default Ammo"):
                player.switch_ammo(2)
            player.attack_enemy(tank, mapaTest)
            print(player.info())

            if(tank not in mapaTest.opponents):
                print(f"{player.name} win against {tank.name} with {player.hp} left")
                break
            tank.attack_enemy(player)
            print(tank.info())
            if(player.hp <=0):
                print(f"{tank.name} win against {player.name} with {tank.hp} left")
                break
        print('\n')


def test3(stdscr):
    curses.curs_set(0)
    mapaTest = m.RMap()
    Tmap = [
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
         el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
        [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
         el.Wall(), el.Wall(), el.Wall(), el.Wall()]
    ]
    mapaTest.map = Tmap
    player = m.Player(9, 25, "player_tank", 300, 60)
    mapaTest.set_player(player)

    MS1 = m.Opponent(8, 23, OpponentType.MS1)
    T28 = m.Opponent(3, 13, OpponentType.T28)
    KV85 = m.Opponent(13, 13, OpponentType.KV85)
    IS3 = m.Opponent(12, 27, OpponentType.IS3)
    IS7 = m.Opponent(13, 21, OpponentType.IS7)

    tanks = [MS1, T28, KV85, IS3, IS7]
    for tank in tanks:
        mapaTest.set_opponent(tank)


    while(True):
        mapaTest.printMap(stdscr)
        key = stdscr.getkey()
        if key in ['w', 'a', 's', 'd']:
            player.move_player(key)
            if mapaTest.check_field(player.x, player.y):
                mapaTest.update_player_pos(player)
            else:
                player.x = player.prev_x
                player.y = player.prev_y
        if key in ['1', '2']:
            player.switch_ammo(key)
        elif key == 'q':
            break

        mapaTest.player.info(stdscr)

        stdscr.refresh()

    #test1()
# test2()

if __name__ == "__main__":
    curses.wrapper(test3)