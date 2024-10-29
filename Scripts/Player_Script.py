import pygame
from Animation_Script import animation

class Player:
    def __init__(self, game):
        self.game = game
        self.player_x = 100
        self.player_y = 100

        self.animations = animation().Playeranimations()
        
        

        
    

    def MainPlayer(self):
        #Exit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.exitfunc()
        

        self.animations.moving = False

        if keys[pygame.K_a]:
            self.animations.animationsteps = 0
            if self.animations.direction != "Walk_Left":
                self.animations.last_direction = "Walk_Left"
                self.animations.direction = "Walk_Left"
            self.player_x -=7
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = 0.07
                
    
        elif keys[pygame.K_d]:
            self.animations.animationsteps = 0
            if self.animations.direction != "Walk_Right":
                self.animations.last_direction = "Walk_Right"
                self.animations.direction = "Walk_Right"
            self.player_x +=7
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = 0.07
                

        if not self.animations.moving:
            self.animations.animationsteps = 0
            self.animations.animation_speed = 0.5
            if self.animations.last_direction == "Walk_Right":
                self.animations.direction = "Idle_Right"
            elif self.animations.last_direction == "Walk_Left":
                self.animations.direction = "Idle_Left"
            self.animations.LoadPlayer(self.animations.direction)
            
           
        
        self.animations.update(self.game.clock.tick(60) / 1000.0)
            
    def draw(self):
        self.animations.draw(self.game, self.player_x, self.player_y)

