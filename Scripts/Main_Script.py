import pygame
import sys

from Entity_script import Entity


class Game:
    def __init__(self):
        #Setup
        pygame.init()
        self.window = pygame.display.set_mode((0,0), 0, pygame.DOUBLEBUF | pygame.FULLSCREEN)
        pygame.display.set_caption("Game alpha")
        pygame.display.set_icon(pygame.image.load("Images\Player\Idle\PlayerIdle.png"))
        
        pygame.event.set_grab(True)
        self.run = True
        
        
        #Monitor
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
    
        #Entities
        self.player = Entity.Player(self)
        self.entities = [
                        Entity(self, "Villager", 14, 20, 200, 200, True, False, None, "Menu"),
                        Entity(self, "House1", 88, 112, 500, 700, False, True, None, None),
                        ]
        

        
        
        
        
        #FPS
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        

    
    def main(self):
        while self.run:
            self.clearwindow()
            self.clock.tick(self.fps) / 1000.0
            print(self.clock.get_fps())
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitfunc()

                    
            for entity in self.entities:
                if abs(entity.pos_x - self.player.player_x) < self.screen_width // 2 \
                        and abs(entity.pos_y - self.player.player_y) < self.screen_height // 2:
                    entity.main()
            self.player.MainPlayer()
            self.render_entities()

            
            

            pygame.display.flip()

    
            

    def render_entities(self):
        render_object = [(self.player, self.player.player_y + self.player.world_offset_y)] +[(entity, entity.offset_y + self.player.world_offset_y) for entity in self.entities]
        
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

