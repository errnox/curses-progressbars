import sys
import time
import curses


class ProgressBar:
    def __init__(self):
        pass

    def render(self, it, prefix = "", size = 60):
        count = len(it)
        def _show(_i):
            x = int(size*_i/count)
            sys.stdout.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
            sys.stdout.flush()

        _show(0)
        for i, item in enumerate(it):
            yield item
            _show(i+1)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def add(self, win, it, prefix = "", size = 60):
        curses.curs_set(0) # Set cursor invisibley
        count = len(it)
        def _show(_i):
            x = int(size*_i/count)
            win.addstr("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), _i, count))
            win.refresh()
            curses.delay_output(9999)
            win.clear()

        _show(0)
        for i, item in enumerate(it):
            yield item
            _show(i+1)
        win.addstr("\n")
        win.refresh()
        curses.delay_output(9999)
        win.clear()
        curses.curs_set(1)


if __name__ == "__main__":
    pb = ProgressBar()

    # Initialization
    stdscr = curses.initscr();
    curses.noecho();
    curses.cbreak();
    stdscr.keypad(1);
    curses.start_color();

    # Render the progress bar
    for i in pb.add(stdscr, range(15), "Computing: ", 40):
        time.sleep(0.1) # Long computation etc.

    # Deinitialization
    curses.nocbreak;
    stdscr.keypad(0);
    curses.echo();
    curses.endwin();
