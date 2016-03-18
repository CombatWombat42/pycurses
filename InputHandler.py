import threading
import datetime
import curses
class InputHandler(threading.Thread):
    myScreen = None
    myPad = None
    myColor = 0
    f = None
    def __init__(self,screen,pad):
        threading.Thread.__init__(self)
        self.f = open('InputHandler.log', 'a')
        now = datetime.datetime.now()
        self.f.write("InputHandler started: ")
        self.f.write(now.isoformat())
        self.f.write("\n")

        print "InputHandler started"
        self.myScreen = screen
        self.myPad = pad
    def run(self):
        self.f.write("InputHandler \"run\"\n")
        while 1:
            self.f.write("InputHandler running\n")
            inputKey = self.myScreen.getkey()
            if inputKey == 'w':
                self.myColor = (self.myColor + 1)%255
            if inputKey == 's':
                self.myColor = (self.myColor - 1)%255
            self.myPad.addch(1,1,inputKey)
            curses.init_pair(2,curses.COLOR_WHITE,self.myColor)
