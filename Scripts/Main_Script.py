import pygame
import sys

from Entity_script import Entity

class Game:
    def __init__(self):
        #Setup
        pygame.init()
        self.window = pygame.display.set_mode((0,0), 0, pygame.DOUBLEBUF | pygame.FULLSCREEN)
        
        pygame.event.set_grab(True)
        self.run = True
        
        
        #Monitor
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
    
        #Entities
        self.entity = Entity(self, "House1", 128, 128, None, None)
        self.entity = Entity(self, "Villager", 14, 20, None, "Menu")
        self.player = Entity.Player(self)
        
        
        
        #FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        

    
    def main(self):
        while self.run:
            self.clearwindow()
            deltatime = self.clock.tick(self.fps) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitfunc()

                    
            
            self.entity.main()
            self.player.MainPlayer()
            self.render_entities()

            
            

            pygame.display.flip()

    
            

    def render_entities(self):
        render_object = [(self.player, self.player.player_y),
                         (self.entity, self.entity.pos_y)]
        
        render_object.sort(key=lambda obj: obj[1])

        for entity, _ in render_object:
            entity.draw()

    def exitfunc(self):
        self.run = False
        pygame.quit()
        sys.exit()

    def clearwindow(self):
        self.window.fill((50,150,50))


if __name__ == "__main__":
    Game().main()

