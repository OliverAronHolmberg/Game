import pygame
from Animation_Script import animation

class Player:
    def __init__(self, game):
        self.game = game
        self.player_x = 100
        self.player_y = 100

        self.animations = animation().Playeranimations()
        
        
        self.movementspeed = 0
        self.animatespeed = 0.05
        
    

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
            if keys[pygame.K_LSHIFT]:
                self.movementspeed = 9
                self.animatespeed = 0.01
            else:
                self.movementspeed = 5
                self.animatespeed = 0.07
            self.player_x -=self.movementspeed
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = self.animatespeed
                
    
        elif keys[pygame.K_d]:
            self.animations.animationsteps = 0
            if self.animations.direction != "Walk_Right":
                self.animations.last_direction = "Walk_Right"
                self.animations.direction = "Walk_Right"
            if keys[pygame.K_LSHIFT]:
                self.movementspeed = 9
                self.animatespeed = 0.01
            else:
                self.movementspeed = 5
                self.animatespeed = 0.07
            self.player_x += self.movementspeed
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = self.animatespeed
        
        if keys[pygame.K_s]:
            self.animations.animationsteps = 0
            if self.animations.direction != "Walk_Down":
                self.animations.last_direction = "Walk_Down"
                self.animations.direction = "Walk_Down"
            if keys[pygame.K_LSHIFT]:
                self.movementspeed = 9
                self.animatespeed = 0.01
            else:
                self.movementspeed = 5
                self.animatespeed = 0.07
            self.player_y +=self.movementspeed
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = self.animatespeed
        
        if keys[pygame.K_w]:
            self.animations.animationsteps = 0
            if self.animations.direction != "Walk_Up":
                self.animations.last_direction = "Walk_Up"
                self.animations.direction = "Walk_Up"
            if keys[pygame.K_LSHIFT]:
                self.movementspeed = 9
                self.animatespeed = 0.02
            else:
                self.movementspeed = 5
                self.animatespeed = 0.07
            self.player_y -=self.movementspeed
            self.animations.moving = True
            self.animations.LoadPlayer(self.animations.direction)
            self.animations.animation_speed = self.animatespeed
                

        if not self.animations.moving:
            self.animations.animationsteps = 0
            self.animatespeed = 0.5
            self.animations.animation_speed = self.animatespeed
            if self.animations.last_direction == "Walk_Right":
                self.animations.direction = "Idle_Right"
            elif self.animations.last_direction == "Walk_Left":
                self.animations.direction = "Idle_Left"
            elif self.animations.last_direction == "Walk_Down":
                self.animations.direction = "Idle_Down"
            elif self.animations.last_direction == "Walk_Up":
                self.animations.direction = "Idle_Up"
            self.animations.LoadPlayer(self.animations.direction)
            
            
           
        
        self.animations.update(self.game.clock.tick(60) / 1000.0)
            
    def draw(self):
        self.animations.draw(self.game, self.player_x, self.player_y)

