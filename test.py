import map as m
import element as el
import unittest
from opponents_library import OpponentType
import curses


# # UNITTEST python
# def test1():
#     mapaTest = m.RMap()
#     Tmap = [
#         [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall()]
#     ]
#
#     mapaTest.map = Tmap
#
#     it1 = m.Item(5, 9)
#     it2 = m.Item(2, 10)
#     op1 = m.Opponent(9, 15, "opponent_tank1", 100, 40)
#     op2 = m.Opponent(13, 20, "opponent_tank2", 150, 50)
#
#     player = m.Player(9, 25, "player_tank", 300, 60)
#
#     mapaTest.set_item(it1)
#     mapaTest.set_item(it2)
#     mapaTest.set_opponent(op1)
#     mapaTest.set_opponent(op2)
#     mapaTest.set_player(player)
#
#     mapaTest.load()
#     mapaTest.printMap()
#     print(player.info())
#
#     player.move_player("w")
#     mapaTest.update_player_pos(player)
#
#     player.move_player("w")
#     mapaTest.update_player_pos(player)
#
#     op1.attack_enemy(player)
#     player.attack_enemy(op1, mapaTest)
#     player.attack_enemy(op2, mapaTest)
#
#     op1.attack_enemy(player)
#     op1.attack_enemy(player)
#
#     player.heal()
#     player.heal()
#
#     op1.attack_enemy(player)
#     op1.attack_enemy(player)
#     op1.attack_enemy(player)
#     op1.attack_enemy(player)
#
#     player.heal()
#
#     op1.attack_enemy(player)
#     op1.attack_enemy(player)
#
#     while (op1 in mapaTest.opponents):
#         player.attack_enemy(op1, mapaTest)
#
#     mapaTest.printMap()
#     mapaTest.show_enemies()
#
#     while (op2 in mapaTest.opponents):
#         player.attack_enemy(op2, mapaTest)
#         #    mapaTest.delete_item(it2)
#     #    mapaTest.delete_opponent(op1)
#
#     mapaTest.printMap()
#     print(player.info())
#     mapaTest.show_enemies()


# def test2():
#     mapaTest = m.RMap()
#     Tmap = [
#         [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Wall(), el.Wall(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Floor(), el.Floor(), el.Wall(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(),
#          el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Floor(), el.Wall()],
#         [el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(), el.Wall(),
#          el.Wall(), el.Wall(), el.Wall(), el.Wall()]
#     ]
#
#     mapaTest.map = Tmap
#
#     player = m.Player(9, 25, "player_tank", 300, 60)
#
#     MS1 = m.Opponent(5, 15, OpponentType.MS1)
#     T28 = m.Opponent(8, 23, OpponentType.T28)
#     KV85 = m.Opponent(13, 13, OpponentType.KV85)
#     IS3 = m.Opponent(12, 27, OpponentType.IS3)
#     O277 = m.Opponent(13, 21, OpponentType.O277)
#
#     tanks = [MS1, T28, KV85, IS3, O277]
#
#     mapaTest.set_player(player)
#
#     for tank in tanks:
#         mapaTest.set_opponent(tank)
#         mapaTest.player.hp = 300
#         while (tank in mapaTest.opponents and player.hp > 0):
#             if (player.selected_ammo.quantity == 0 and player.selected_ammo.name == "Default Ammo"):
#                 player.switch_ammo(2)
#             player.attack_enemy(tank, mapaTest)
#             print(player.info())
#
#             if (tank not in mapaTest.opponents):
#                 print(f"{player.name} win against {tank.name} with {player.hp} left")
#                 break
#             tank.attack_enemy(player)
#             print(tank.info())
#             if (player.hp <= 0):
#                 print(f"{tank.name} win against {player.name} with {tank.hp} left")
#                 break
#         print('\n')


def test3(stdscr):
    curses.curs_set(0)
    mapaTest = m.RMap(25, 60)

    mapaTest.generate_map(20)

    win = stdscr.subwin(20, 50, 0, 62)
    win.bkgd(' ', curses.color_pair(1))
    win.border()

    mapaTest.set_player(400, 60, 1)

    mapaTest.set_opponents_BY_LVL(mapaTest.player.LVL)
    mapaTest.set_opponents()
    mapaTest.set_items(1)
    flag_win = False
    next_lvl = False
    while (True):
        win.clear()
        if (flag_win):
            break
        else:
            mapaTest.printMap(stdscr)
            key = stdscr.getkey()
            if not mapaTest.opponents:
                if (mapaTest.player.LVL > 8):
                    flag_win = True
                    break
                next_lvl = True

            if key == 'n' and next_lvl:
                stdscr.clear()
                mapaTest.player.LVL += 1
                next_lvl = False
                mapaTest.generate_map(20)
                mapaTest.set_player(mapaTest.player.hp, mapaTest.player.avg_dmg+10,mapaTest.player.LVL)
                mapaTest.set_opponents_BY_LVL(mapaTest.player.LVL)
                mapaTest.set_opponents()
                mapaTest.set_items(1)

            if key in ['w', 'a', 's', 'd']:
                mapaTest.player.move_player(key)
                if mapaTest.check_field(mapaTest.player.x, mapaTest.player.y):
                    mapaTest.update_player_pos(mapaTest.player)
                    stdscr.refresh()
                else:
                    mapaTest.player.x = mapaTest.player.prev_x
                    mapaTest.player.y = mapaTest.player.prev_y
            if key in ['1', '2']:
                mapaTest.player.switch_ammo(key)
            if key == '\n':
                opp = mapaTest.find_opponent_in_range()
                if (opp):
                    mapaTest.player.attack_enemy(opp, mapaTest, win)
            if mapaTest.find_opponent_in_range():
                opp1 = mapaTest.find_opponent_in_range()
                opp1.attack_player(mapaTest.player, win)
            if key == 'c' and mapaTest.find_item_in_range():
                it1 = mapaTest.find_item_in_range()
                mapaTest.collect_item(it1)
            if(mapaTest.player.hp <= 0):
                break
            mapaTest.move_opponents()
            if key == 'q':
                break

        mapaTest.player.info(stdscr)
        if (next_lvl):
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            stdscr.addstr("ABY PRZEJŚĆ DO NASTĘPNEGO POZIOMU NACIŚNIJ - N", curses.color_pair(1))
        win.refresh()
        stdscr.refresh()


    win.clear()
    if(flag_win):
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        stdscr.clear()
        stdscr.addstr("         WYGRAŁEŚ!!!!!!!", curses.color_pair(2))
        stdscr.refresh()
        stdscr.getkey()

    else:
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        win.clear()
        stdscr.clear()
        stdscr.addstr("         YOU LOST - GAME OVER", curses.color_pair(2))
        stdscr.refresh()
        stdscr.getkey()



    # test1()


# test2()

if __name__ == "__main__":
    curses.wrapper(test3)
