import pygame
import random
import sys
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
        self.w=640
        self.h=480
        self.ends=False
        self.camera=0
        self.enemy=[]
        self.enemycount=3
        self.screens=None
        self.caption="games"
        self.bcolor=(0,0,0)


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
        clock = pygame.time.Clock()
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
             pygame.display.flip()
             # Limita o FPS
             clock.tick(60)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      gamestart=False
             if self.ends:
                 break

    def main(self):
        #put you code here
        pygame.init()
        self.screens=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption(self.caption)
        self.screens.fill(self.bcolor)
        pygame.display.flip()
        self.startvars()
        self.startgame()
        self.mainloop()
        pygame.quit()
        sys.exit()


games1=games()
games1.main()
