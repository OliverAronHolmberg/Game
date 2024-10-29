import pygame
import sys
from Player_Script import Player


class Game:
    def __init__(self):
        #Setup
        pygame.init()
        self.window = pygame.display.set_mode((0,0), pygame.NOFRAME | pygame.FULLSCREEN)
        self.run = True
        pygame.event.set_grab(True)
    
        #Player
        self.player = Player(self)
        
        #FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        
    
    def main(self):
        while self.run:
            self.window.fill((50,50,50))
            deltatime = self.clock.tick(self.fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitfunc()

                    
            
            
            self.player.draw()
            self.player.MainPlayer()
            

            pygame.display.update()

    def exitfunc(self):
        self.run = False
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().main()

