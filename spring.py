import curses
from curses import wrapper
import time

def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    width = 20
    count = 0
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        # Clear out anything else the user has typed in
        curses.flushinp()
        stdscr.clear()
        # If the user presses p, increase the width of the springy bar
        if c == ord('p') and count < 20:
            count += 1
        elif c == -1 and count > 0:
            count -= 1
        # Draw a springy bar
        stdscr.addstr("#" * (width - count))
        stdscr.addch('\n')
        stdscr.addstr("#" * (width - count))

        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)

wrapper(main)
