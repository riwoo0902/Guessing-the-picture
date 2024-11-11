import pygame
from guessing import *
class Picturedrawc():
    imgtime = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

    def __init__(self,screen):
        self.screen = screen
        self.imgtype = []
        for i in range(1,7):
            img = pygame.image.load(f'./image/player{i}.png')
            self.imgtype.append(pygame.transform.scale(img , (300, 300)))
        self.rec = (0,0)
        
    def draw(self,Showpicture):
        for i in range(3):
            for k in range(4):
                if Showpicture[i][k] != 0:
                    self.rec = (k*300,i*300)
                    if Showpicture[i][k] == 'player1.png':
                        self.screen.blit(self.imgtype[0], self.rec)
                    elif Showpicture[i][k] == 'player2.png':
                        self.screen.blit(self.imgtype[1], self.rec)
                    elif Showpicture[i][k] == 'player3.png':
                        self.screen.blit(self.imgtype[2], self.rec)
                    elif Showpicture[i][k] == 'player4.png':
                        self.screen.blit(self.imgtype[3], self.rec)
                    elif Showpicture[i][k] == 'player5.png':
                        self.screen.blit(self.imgtype[4], self.rec)
                    elif Showpicture[i][k] == 'player6.png':
                        self.screen.blit(self.imgtype[5], self.rec)
        self.draw2()
        
    def draw2(self):
        time = pygame.time.get_ticks()
        for i in range(3):
            for k in range(4):
                if self.imgtime[i][k] != 0:
                    if self.imgtime[i][k][0] == 'player1.png':
                        self.screen.blit(self.imgtype[0],(k*300,i*300))
                    elif self.imgtime[i][k][0] == 'player2.png':
                        self.screen.blit(self.imgtype[1],(k*300,i*300))
                    elif self.imgtime[i][k][0] == 'player3.png':
                        self.screen.blit(self.imgtype[2],(k*300,i*300))
                    elif self.imgtime[i][k][0] == 'player4.png':
                        self.screen.blit(self.imgtype[3],(k*300,i*300))
                    elif self.imgtime[i][k][0] == 'player5.png':
                        self.screen.blit(self.imgtype[4],(k*300,i*300))
                    elif self.imgtime[i][k][0] == 'player6.png':
                        self.screen.blit(self.imgtype[5],(k*300,i*300)) 
                    if time - self.imgtime[i][k][1] >=500:
                        self.imgtime[i][k] = 0








