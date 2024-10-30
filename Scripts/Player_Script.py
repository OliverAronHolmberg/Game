import pygame
from Animation_Script import animation

class Player:
    def __init__(self, game):
        self.game = game
        self.player_x = 200
        self.player_y = 200


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
        
        colliderheight = self.player_height//4
        self.collider = pygame.Rect(self.player_x, self.player_y + self.player_height - colliderheight, self.player_width, colliderheight)

    def MainPlayer(self):
        #Exit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.exitfunc()
        

        self.animations.moving = False
        move_x = 0
        move_y = 0

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
            move_y = -self.movementspeed
                

        if move_x != 0 and move_y != 0:
            move_x *= 0.707
            move_y *= 0.707

            
        new_x = self.player_x + move_x
        new_y = self.player_y + move_y

        self.player_x = max(self.left_boundry, min(self.right_boundry, new_x))
        self.player_y = max(self.top_boundry, min(self.bottom_boundry, new_y))

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
            
        self.update_collider()


        
           
        
        self.animations.update(self.game.clock.tick(60) / 1000.0)

    def update_collider(self):
        colliderheight= self.player_height//4
        self.collider = pygame.Rect(self.player_x, self.player_y + self.player_height - colliderheight, self.player_width, colliderheight)

        
            
    def draw(self):
        self.animations.draw(self.game, self.player_x, self.player_y)

