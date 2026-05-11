import time
class games:
    #put you code here
    def __init__(self):
        #put you code here
        self.score=0
        self.fire=0
        self.live=0
        self.lives=3
        self.x=0
        self.y=0
        self.z=0
        self.ends=False
        self.camera=0
        self.enemy=[]
        self.enemycount=3

    def debugs(self,value):
        #put you code here
        print(value)
        time.sleep(0.1)

    def startvars(self):
        #put you code here
        self.debugs("startvars")

    def startgame(self):
        #put you code here
        self.debugs("startgame")
    
    def handlenemy(self):
       #put you code here
       for enemy in range(self.enemycount):
           self.debugs("handle enemy : "+str(enemy))

    def handlekeymouse(self):
        #put you code here
        self.debugs("handlekeymouse")

    def drawmain(self):
        #put you code here
        self.debugs("drawmain")

    def drawenemys(self):
        #put you code here
        self.debugs("drawenemys")

    def drawplayers(self):
         #put you code here
         self.debugs("drawplayers")

    def changenetwork(self):
        #put you code here
        self.debugs("changenetwork")

    def handlescore(self):
        #put you code here
        self.debugs("handlescore")

    def refreshscreen(self):
        #put you code here
        time.sleep(1)

    def checkgameover(self):
        #put you code here
        self.debugs("checkgameover")


    def mainloop(self):
        #put you code here
        #you can chage list events order
        gamestart=True
        self.debugs("mainloop")
        while gamestart:
             self.drawmain()
             self.handlenemy()
             self.drawenemys()
             self.handlekeymouse()
             self.drawplayers() 
             self.changenetwork()
             self.handlescore()
             self.refreshscreen()
             self.checkgameover()
             if self.ends:
                 break

    def main(self):
        #put you code here
        self.startvars()
        self.startgame()
        self.mainloop()


games1=games()
games1.main()
