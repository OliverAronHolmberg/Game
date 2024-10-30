import pygame
from Renderer_script import SpriteSheetRenderer
from Animation_Script import animation

class Entity:
    def __init__(self, game, entitytype, size_x, size_y, animations, mission=None, trading=None):
        self.game = game
        self.entitytype = entitytype
        self.size_x = size_x
        self.size_y = size_y
        self.animations = animations
        self.mission = mission
        self.trading = trading

        self.moving = False

        self.pos_x = 200
        self.pos_y = 400

        self.sheets = {"Idle_Down": pygame.image.load("Images\Villager\Idle\VillagerIdle.png").convert_alpha(),}
        self.direction = "Idle_Down"
        
        self.animations = animation(self.sheets, self.direction)
        
        self.movementspeed = 0
        self.animatespeed = 0.05
        

        colliderheight = self.size_y//4
        self.collider = pygame.Rect(self.pos_x, self.pos_y + self.size_y - colliderheight, self.size_x, colliderheight)
        


    def main(self):
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
            self.animations.Load_animation_frames(self.animations.direction)
            



        self.animations.update(self.game.clock.tick(60) / 1000.0)
        self.updatecollider()

    def updatecollider(self):
        collider_height = self.size_y//4
        self.collider.topleft = (self.pos_x, self.pos_y + self.size_y - collider_height)


    def draw(self):
        self.animations.draw(self.game, self.pos_x, self.pos_y)
    



    
        