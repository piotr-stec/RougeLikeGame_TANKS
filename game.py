import map as m
import element as el
import unittest
from opponents_library import OpponentType
import curses


def test3(stdscr):
    curses.curs_set(0)
    mapaTest = m.RMap(25, 60)

    mapaTest.generate_map(20)

    win = stdscr.subwin(20, 50, 0, 62)
    win.bkgd(' ', curses.color_pair(1))
    win.border()

    mapaTest.set_player(400, 60, 1, 10, 5)

    mapaTest.set_opponents_BY_LVL(mapaTest.player.LVL)
    mapaTest.set_opponents()
    mapaTest.set_items(1)
    flag_win = False
    next_lvl = False
    display_first_time = True
    display_for_next_lvl = False

    starting_screen = ("\t\t\tWitaj w grze TANKS\n\n"
                       "Zasady oraz instrukcja gry: \n"
                       "\n\t-Twoim zadaniem jest pokonanie wszystkich przeciwników znajdujących się na mapie\n"
                       "\n\t-Gdy pokonasz wszystkie czołgi przeciwnika naciśnij przycisk N aby przejść do kolejnego etapu\n"
                       "\nOznaczenia na mapie:\n"
                       "\n\t-@ - Gracz\n"
                       "\n\t-M T K I O - CZOŁGI PRZECIWNIKA: MS1, T28, KV85, IS3, OBJ277\n"
                       "\n\t-H - Zestaw naprawczy dodający hp\n"
                       "\n\t-D - Amunicja podstawowa\n"
                       "\n\t-G - Amunicja złota zadająca 15% więcej obrażeń\n"
                       "\nKlawisze w grze:\n"
                       "\n\t-W A S D - poruszanie się gracza po mapie\n"
                       "\n\t-ENTER - atak przeciwnika\n"
                       "\n\t-1/2 - zmiana amunicji na Default(1) lub Gold(2)\n"
                       "\n\t-c - podnoszenie przedmiotów znajdujących się na mapie\n"
                       "\n\t-n - przejdź do następnego poziomu\n"
                       "\n\t-i - menu gry\n"
                       "\nABY ROZPOCZĄĆ GRE NACIŚNIJ DOWOLNY PRZYCISK")
    while (True):
        win.clear()
        if display_first_time:
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

            stdscr.addstr(starting_screen, curses.color_pair(1)|curses.A_BOLD)
            display_first_time = not display_first_time

        if display_for_next_lvl:
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            mapaTest.printMap(stdscr)
            mapaTest.show_messages(mapaTest.player.info(), stdscr)
            display_for_next_lvl = not display_for_next_lvl

        key = stdscr.getkey()
        stdscr.clear()

        if flag_win:
            break
        else:
            mapaTest.printMap(stdscr)
            mapaTest.show_messages(mapaTest.player.info(), stdscr)
            opp2 = mapaTest.find_player_in_range()

            if key in ['w', 'a', 's', 'd']:
                mapaTest.player.move_player(key)
                if mapaTest.check_field(mapaTest.player.x, mapaTest.player.y):
                    mapaTest.update_player_pos(mapaTest.player)
                    mapaTest.printMap(stdscr)
                    mapaTest.show_messages(mapaTest.player.info(), stdscr)
                    stdscr.refresh()
                else:
                    mapaTest.player.x = mapaTest.player.prev_x
                    mapaTest.player.y = mapaTest.player.prev_y

            opponent_in_range = mapaTest.find_opponent_in_range(mapaTest.player.range)

            if opponent_in_range:
                opponent_in_range_flag = True
            else:
                opponent_in_range_flag = False

            if opponent_in_range_flag and not next_lvl:
                curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
                stdscr.addstr("OPPONENT IN RANGE PRESS ENTER\n", curses.color_pair(1))
                stdscr.refresh()

            if key == 'n' and next_lvl:
                stdscr.clear()
                display_for_next_lvl = True
                mapaTest.player.LVL += 1
                next_lvl = False
                mapaTest.generate_map(20)
                mapaTest.set_player(mapaTest.player.hp + mapaTest.player.hp * 0.3,
                                    mapaTest.player.avg_dmg + mapaTest.player.LVL * 7, mapaTest.player.LVL,
                                    mapaTest.player.ammo_inventory[0].quantity,
                                    mapaTest.player.ammo_inventory[1].quantity)
                mapaTest.set_opponents_BY_LVL(mapaTest.player.LVL)
                mapaTest.set_opponents()
                mapaTest.set_items(mapaTest.player.LVL)

            if not mapaTest.opponents:
                if mapaTest.player.LVL > 8:
                    flag_win = True
                    stdscr.clear()
                    mapaTest.printMap(stdscr)
                    mapaTest.show_messages(mapaTest.player.info(), stdscr)
                    stdscr.refresh()
                    break
                next_lvl = True

            if key in ['1', '2']:
                mapaTest.player.switch_ammo(key)
                mapaTest.printMap(stdscr)
                mapaTest.show_messages(mapaTest.player.info(), stdscr)
                stdscr.refresh()

            if key == 'i' or key == chr(27):
                end_game = mapaTest.game_instruction(win, 4)
                if end_game:
                    break
                win.refresh()

            if key == '\n':
                opp = mapaTest.find_opponent_in_range(mapaTest.player.range)
                if opp:
                    mapaTest.player.attack_enemy(opp, mapaTest, stdscr, mapaTest, win)
                    mapaTest.printMap(stdscr)
                    mapaTest.show_messages(mapaTest.player.info(), stdscr)
                    stdscr.refresh()

            if mapaTest.find_player_in_range():
                opp1 = mapaTest.find_player_in_range()
                opp1.attack_player(mapaTest.player, stdscr)


            if key == 'c' and mapaTest.find_item_in_range():
                it1 = mapaTest.find_item_in_range()
                mapaTest.collect_item(it1)
                mapaTest.printMap(stdscr)
                mapaTest.show_messages(mapaTest.player.info(), stdscr)
                stdscr.refresh()
                mapaTest.display_message2(f"COLLECTED ITEM: {it1.info}", win, 1)

            if mapaTest.player.hp <= 0:
                break
            if not opp2:
                mapaTest.move_opponents()
            else:
                if key in ['w', 'a', 's', 'd']:
                    mapaTest.move_opp_in_fight(opp2, key)


        if next_lvl:
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            stdscr.clear()
            mapaTest.printMap(stdscr)
            mapaTest.show_messages(mapaTest.player.info(), stdscr)
            stdscr.addstr("ABY PRZEJŚĆ DO NASTĘPNEGO POZIOMU NACIŚNIJ - N", curses.color_pair(1))
            stdscr.refresh()

        win.refresh()
        stdscr.refresh()

    win.clear()
    if flag_win:
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


if __name__ == "__main__":
    curses.wrapper(test3)
