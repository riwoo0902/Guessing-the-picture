import pygame
import random
from picture import *
class Guessing():
    picture = [
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]
              ]
    clicksave1 = []
    clicksave2 = []
    Showpicture = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
       ]
    clicktype = 1
    chickstart = 0
    win = False
    
    
    
    def __init__(self, screen):
        self.screen = screen
        self.randompicture()
 
        
        self.picturerec = []
        self.lock1 = 0
        
    def randompicture(self):
        temp1 = ['player1.png','player2.png','player3.png','player4.png','player5.png','player6.png',
                 'player1.png','player2.png','player3.png','player4.png','player5.png','player6.png']
        random.shuffle(temp1)
        self.picture[0] = temp1[0:4]
        self.picture[1] = temp1[4:8]
        self.picture[2] = temp1[8:12]
        for i in range(3):
            for k in range(4):
                self.picture[i][k] = [self.picture[i][k],[i,k]]
        print(self.picture[0])
        print(self.picture[1])
        print(self.picture[2])
    
    def choice(self):
        if pygame.mouse.get_pressed()[0]:
            if self.lock1 == 0:
                self.lock1 = 1
                pos = pygame.mouse.get_pos()
                if pos[0] < 300:
                    a = 0
                elif pos[0] < 600:
                    a = 1
                elif pos[0] < 900:
                    a = 2
                else:
                    a = 3
                if pos[1] < 300:
                    b = 0
                elif pos[1] < 600:
                    b = 1
                else:
                    b = 2        
                if self.clicktype == 1:
                    self.clicktype = 2
                    self.clicksave1 = [b,a]
                    Picturedrawc.imgtime[b][a] = [self.picture[b][a][0],pygame.time.get_ticks()]
                    if self.clicksave2 != []:
                        self.chickstart = 1
                elif self.clicktype == 2:
                    self.clicktype = 1
                    self.clicksave2 = [b,a]
                    Picturedrawc.imgtime[b][a] = [self.picture[b][a][0],pygame.time.get_ticks()]
                    self.chickstart = 1
                print(self.clicksave1,self.clicksave2)
        else:
            self.lock1 = 0
    
    def acomparison(self):
        if self.chickstart == 1:
            if self.clicksave1 != self.clicksave2:
                if self.picture[self.clicksave1[0]][self.clicksave1[1]][0] == self.picture[self.clicksave2[0]][self.clicksave2[1]][0]:
                    self.Showpicture[self.clicksave1[0]][self.clicksave1[1]] = self.picture[self.clicksave1[0]][self.clicksave1[1]][0]
                    self.Showpicture[self.clicksave2[0]][self.clicksave2[1]] = self.picture[self.clicksave2[0]][self.clicksave2[1]][0]
            self.chickstart = 0

    def winchick(self):
        a = 0
        for i in range(3):
            for k in range(4):
                if self.Showpicture[i][k] != 0:
                    a += 1
        if a == 12:
            self.win = True

    def draw(self):
        for i in range(300,1200,300):
            pygame.draw.line(self.screen,(0, 0, 0),(i, 0),(i, 900))
            pygame.draw.line(self.screen,(0, 0, 0),(0, i),(1200, i))
        self.choice()
        self.acomparison()
        self.winchick()


