import curses
from curses import wrapper
import threading
import CurseRenderer
import InputHandler
import datetime

f = open('pycurs.log', 'a')

stdscr = curses.initscr()
curses.start_color()

def main(stdscr):
    now = datetime.datetime.now()
    f.write("My curs started: ")
    f.write(now.isoformat())
    f.write("\n")
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLUE)
    curses.init_pair(2,6,6)
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

    begin_x = 20
    begin_y = 7
    height = 5
    width = 40
    # win = curses.newwin(height,width,begin_y,begin_x)
    # stdscr.refresh()
    # stdscr.getkey()
    pairnum=1
    pad = curses.newpad(100,100)
    inHandle = InputHandler.InputHandler(stdscr,pad)
    render = CurseRenderer.CurseRenderer(stdscr,pad)
    inHandle.daemon = True
    render.daemon = True
    inHandle.start()
    render.start()
    for y in range(0,99):
        for x in range(0,99):
            pairnum=(255+y*100+x)
            #curses.init_pair(pairnum,y,x)
            pad.addch(y,x,ord('a'),curses.color_pair(2)) #+ (x*x+y*y)%(26))

#    stdscr.refresh()
    # i = 1
    # pos = 1
    # inputChar = 'b'
    # while inputChar != 'q':
    #     curses.init_pair(i+2,i,(i+2)%255)
    #     pad.addch(pos%20,pos%75,inputChar,curses.color_pair(i+2)|curses.A_REVERSE)
    #     pad.addstr(0,2,str(i))
    #     i = (i + 1) %255
    #     pos = pos + 1
    #     pad.refresh(0,0,1,1,20,75)
    #     inputChar = stdscr.getkey()
    while 1:
        pass
    exit()
            
#terminate
# curses.nocbreak()
# stdscr.keypad(0)
# curses.echo()
# curses.endwin()

if __name__ == '__main__':
    wrapper(main)
