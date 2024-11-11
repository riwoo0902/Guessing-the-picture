import pygame
from guessing import *
from picture import *
# from player import *

class Game():
    isActive = True
    screen = (1200,900)
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("codingnow.co.kr")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen)
        self.guessing = Guessing(self.screen)
        self.picture = Picturedrawc(self.screen)
        winimg = pygame.image.load(f'./image/win.png')
        self.winimg = pygame.transform.scale(winimg , (1200, 900))
    def eventProcess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.isActive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
            
    def run(self):
        while self.isActive:
            self.screen.fill((255, 255, 255))
            self.eventProcess()
            self.guessing.draw()
            self.picture.draw(self.guessing.Showpicture)
            if self.guessing.win:
                self.screen.blit(self.winimg, (0,0))
                self.isActive = False
            pygame.display.update()
            self.clock.tick(100)

if __name__ == '__main__':
    game = Game()
    game.run()
    
    