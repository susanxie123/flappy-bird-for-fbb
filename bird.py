import curses
from curses import wrapper
import time

def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    curses.curs_set(0)
    stdscr.clear()
    width = 20
    pos = 10
    face = 1 # facing right if 1, facing left if 0
    win = curses.newwin(10,23,0,pos)
    win.addstr(draw_right_bird())
    stdscr.refresh()
    win.refresh()
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        if c == -1:
            time.sleep(0.1)
            continue
        # Clear out anything else the user has typed in
        curses.flushinp()
        # If the user presses a, move left, if the user presses d, move right
        if c == ord('a') and pos > 0:
            pos -= 1
            if face == 1:
                win.addstr(0,0,draw_left_bird())
                face = 0
        elif c == ord('d') and pos < width:
            pos += 1
            if face == 0:
                win.addstr(0,0,draw_right_bird())
                face = 1
        win.mvwin(0, pos)
        stdscr.clear()
        stdscr.refresh()
        win.refresh()

        time.sleep(0.1)

def draw_left_bird():
    bird = ""
    bird += "               ^     \n"
    bird += "             /  |    \n"
    bird += "  __   ____ /  /___/|\n"
    bird += " / o \/             |\n"
    bird += "X    |         /---\|\n"
    bird += " \__/         /      \n"
    bird += "     \_______/       \n"
    return bird

def draw_right_bird():
    bird = ""
    bird += "     ^               \n"
    bird += "    |  \             \n"
    bird += "|\___\  \_____  __   \n"
    bird += "|             \/ o \ \n"
    bird += "|/---\         |    X\n"
    bird += "      \         \__/ \n"
    bird += "       \_______/     \n"
    return bird

wrapper(main)
