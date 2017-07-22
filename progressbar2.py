import curses
import random


class progressBar:
  def __init__(self, minValue = 0, maxValue = 10, totalWidth=12):
    self.progBar = "[]"   # This holds the progress bar string
    self.min = minValue
    self.max = maxValue
    self.span = maxValue - minValue
    self.width = totalWidth
    self.amount = 0       # When amount == max, we are 100% done
    self.updateAmount(0)  # Build progress bar string
  
  def updateAmount(self, newAmount = 0):
    if newAmount > self.max: newAmount = self.max
    self.amount = newAmount
    
    # Figure out the new percent done, round to an integer
    diffFromMin = float(self.amount - self.min)
    percentDone = (diffFromMin / float(self.span)) * 100.0
    percentDone = round(percentDone)
    percentDone = int(percentDone)
    
    # Figure out how many hash bars the percentage should be
    allFull = self.width - 2
    numHashes = (percentDone / 100.0) * allFull
    numHashes = int(round(numHashes))
    
    # Build a progress bar with hashes and spaces
    self.progBar = "[" + '#'*numHashes + ' '*(allFull-numHashes) + "]"
    
    # Figure out where to put the percentage, roughly centered
    percentPlace = (len(self.progBar) / 2) - len(str(percentDone))
    percentString = str(percentDone) + "%"
    
    # Slice the percentage into the bar
    self.progBar = self.progBar[0:percentPlace] + percentString + self.progBar[percentPlace+len(percentString):]

  def __str__(self):
    return str(self.progBar)


class Main:
  def __init__(self):
    self.stdscr = curses.initscr();
    self.initialize()
  
  def initialize(self):
    curses.noecho();
    curses.cbreak();
    self.stdscr.keypad(1);
    curses.start_color();
  
  def deinitialize(self):
    curses.nocbreak;
    self.stdscr.keypad(0);
    curses.echo();
    curses.endwin();
  
  def render_progress_bar(self, rg=random.randrange(0, 200, 10)):
    win = curses.newwin(20, 100, 0, 0)
    win.refresh()
    pb = progressBar(0, 100, 80)
    for i in range(100):
       pb.updateAmount(i)
       # win.clear()
       win.addstr(pb.progBar)
       win.refresh()
       curses.curs_set(0)
       win.move(0, 0)
       for i in range(rg):
               curses.delay_output(9999)
       win.clear()
  
  def render_progress_bar_loc(self, y, x, rg=random.randrange(0, 200, 10)):
    """
    DEFUNCT: Should render an array of independent progress bars.
    """
    winlist = []
    for i in range(10):
      winlist.append(curses.newwin(20, 100, i, x))
      winlist[-1].refresh
    for win in winlist:
      pb = progressBar(0, 100, 80)
      pb.updateAmount(i)
      # win.clear()
      win.addstr(pb.progBar)
      win.refresh()
      curses.curs_set(0)
      win.move(0, 0)
      for i in range(rg):
              curses.delay_output(9999)
      win.clear()


if __name__ == "__main__":
  prog = Main()
  prog.render_progress_bar()
  prog.deinitialize()

  # n = 10
  # for y in range(n):
  # 	prog.render_progress_bar_loc(y, 0, random.randrange(0, 100, 10))
