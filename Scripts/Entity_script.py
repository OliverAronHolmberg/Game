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
        if self.entitytype == "Villager":
            self.sheets = {"Idle_Down": pygame.image.load("Images\Villager\Idle\VillagerIdle.png").convert_alpha(),}
        if self.entitytype == "House1":
            self.sheets = {"Idle_Down": pygame.image.load("Images\Enviorment\VIllage\House\House1.png").convert_alpha(),}

        
        self.direction = "Idle_Down"
        self.animations = animation(self.sheets, self.direction)
        
        self.movementspeed = 0
        self.animatespeed = 0.05
        

        collider_height = self.size_y//4+10
        collider_width = self.size_x
        self.collider = pygame.Rect(self.pos_x - 10, self.pos_y + self.size_y-collider_height, collider_width, collider_height)

    
        

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
        self.checkcollisions()

    def updatecollider(self):
        collider_height = self.size_y//4+10
        collider_width = self.size_x + self.size_x*3
        self.collider = pygame.Rect(self.pos_x - 10, self.pos_y + self.size_y-collider_height, collider_width, collider_height)

    def checkcollisions(self):
        if self.collider.colliderect(self.game.player.collider):
            return True
        return False

            


    def draw(self):
        self.animations.draw(self.game, self.pos_x, self.pos_y)
    

    class Player:
        def __init__(self, game):
            self.game = game
            self.player_x = 500
            self.player_y = 500
            

            self.sheets = {
                    "Idle_Right": pygame.image.load("Images/Player/Idle/PlayerIdle.png").convert_alpha(),
                    "Idle_Left": pygame.image.load("Images/Player/Idle/PlayerIdle.png").convert_alpha(),
                    "Walk_Left": pygame.image.load("Images/Player/PlayerWalking/PlayerWalkingleftright.png").convert_alpha(),
                    "Walk_Right": pygame.image.load("Images/Player/PlayerWalking/PlayerWalkingleftright.png").convert_alpha(),
                    "Walk_Down":pygame.image.load("Images\Player\PlayerWalking\PlayerWalkDown.png").convert_alpha(),
                    "Idle_Down":pygame.image.load("Images\Player\Idle\PlayerIdleDown.png").convert_alpha(),
                    "Idle_Up":pygame.image.load("Images\Player\Idle\PlayerIdleUp.png").convert_alpha(),
                    "Walk_Up": pygame.image.load("Images\Player\Idle\PlayerIdleUp.png").convert_alpha(),
                }
            self.direction = "Idle_Down" 

            self.animations = animation(self.sheets, self.direction)


            
            
            
            self.movementspeed = 0
            self.animatespeed = 0.05
            self.player_width = 14
            self.player_height = 20


            self.left_boundry = (self.game.screen_width/10) - self.player_width*4
            self.right_boundry = self.game.screen_width - (self.game.screen_width/10) - self.player_width
            self.top_boundry = self.game.screen_height/7 - self.player_height*4
            self.bottom_boundry = self.game.screen_height - (self.game.screen_height/7) - self.player_height
            
            playercolliderheight = self.player_height//4+10
            playercolliderwidth = self.player_width+30
            self.collider = pygame.Rect(self.player_x, self.player_y + self.player_height - playercolliderheight, playercolliderwidth, playercolliderheight)

            self.update_playercollider()

        def MainPlayer(self):
            #Exit
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game.exitfunc()
            
            
            self.animations.moving = False
            move_x = 0
            move_y = 0
            
            
            
            self.colliding = Entity.checkcollisions(self)
            


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
                    self.animatespeed = 0.05
                
                move_x = -self.movementspeed
                
                
                    
                

                
                
            
                
                    
        
            if keys[pygame.K_d]:
                self.animations.animationsteps = 0
                if self.animations.direction != "Walk_Right":
                    self.animations.last_direction = "Walk_Right"
                    self.animations.direction = "Walk_Right"
                if keys[pygame.K_LSHIFT]:
                    self.movementspeed = 9
                    self.animatespeed = 0.01
                else:
                    self.movementspeed = 5
                    self.animatespeed = 0.05
                    self.animatespeed = 0.05
                
                move_x = self.movementspeed
                

                
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
                    self.animatespeed = 0.05
                
                move_y = self.movementspeed
                

                
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
                    self.animatespeed = 0.05
                
                move_y = -self.movementspeed
            
            if move_x != 0 and move_y != 0:
                move_x *= 0.707
                move_y *= 0.707

            new_x = self.player_x + move_x
            new_y = self.player_y + move_y

            last_x = self.player_x
            last_y = self.player_y

            self.player_x = max(self.left_boundry, min(self.right_boundry, new_x))
            self.player_y = max(self.top_boundry, min(self.bottom_boundry, new_y))


            self.update_playercollider()
            

            if self.game.entity.checkcollisions():
                self.player_x = last_x
                self.player_y = last_y
                self.update_playercollider()
        
            if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]:
                self.animations.moving = True
                self.animations.Load_animation_frames(self.animations.direction)
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
                self.animations.Load_animation_frames(self.animations.direction)
                
            

            
            
            
            
            self.animations.update(self.game.clock.tick(60) / 1000.0)

        def update_playercollider(self):
            playercolliderheight = self.player_height//4+10
            playercolliderwidth = self.player_width+30
            self.collider = pygame.Rect(self.player_x, self.player_y + self.player_height - playercolliderheight, playercolliderwidth, playercolliderheight)
        

            
                
        def draw(self):
            self.animations.draw(self.game, self.player_x, self.player_y)

