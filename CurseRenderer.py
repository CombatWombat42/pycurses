import threading
import datetime
from time import sleep

class CurseRenderer(threading.Thread):
    myScreen = None
    myPad = None
    f = None
    def __init__(self,screen,pad):
        threading.Thread.__init__(self)
        self.f = open('CurseRenderer.log', 'a')
        now = datetime.datetime.now()
        self.f.write("CurseRenderer started: ")
        self.f.write(now.isoformat())
        self.f.write("\n")
        self.myScreen = screen
        self.myPad = pad
    def run(self):
        self.f.write("CurseRenderer run\n")
        while 1:
            self.f.write("CurseRenderer running\n")
            sleep(0.1)
            self.myScreen.refresh()
            self.myPad.refresh(0,0,1,1,20,75)
