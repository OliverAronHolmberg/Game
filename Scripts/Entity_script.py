import pygame
from Renderer_script import SpriteSheetRenderer
from Animation_Script import animation


class Entity:

    image_cache = {}

    def __init__(self, game, entitytype, size_x, size_y, x, y, canmove, static, animations, mission=None, trading=None):
        self.game = game
        self.entitytype = entitytype
        self.size_x = size_x
        self.size_y = size_y
        self.pos_x = x
        self.pos_y = y
        self.animations = animations
        self.mission = mission
        self.trading = trading
        self.canmove = canmove
        self.moving = False
        self.static = static
        
        self.offset_x = self.pos_x + self.game.player.world_offset_x
        self.offset_y = self.pos_y+ self.game.player.world_offset_y
        
        
        self.direction = "Idle_Down"
        
        self.movementspeed = 0
        self.animatespeed = 0.05
        

        if entitytype not in Entity.image_cache:
            Entity.image_cache[entitytype] = self.load_image(entitytype)
        self.sheets = Entity.image_cache[entitytype]

        if self.static == True:
            self.animations = None
        else:
            self.animations = animation(self.sheets, self.direction)
        self.updatecollider()

    
    def load_image(self, entitytype):
        if entitytype == "Villager":
            return {"Idle_Down": pygame.image.load("Images\Villager\Idle\VillagerIdle.png").convert_alpha(),}
        elif entitytype == "House1":
            return {"Idle_Down": pygame.image.load("Images\Enviorment\VIllage\House\House1.png").convert_alpha(),}
        return {}


    def main(self):
        
        if self.animations:
            if not self.animations.moving:
                self.animations.animationsteps = 0
                self.animatespeed = 0.5
                self.animations.animation_speed = self.animatespeed
                self.animations.direction= "Idle_" + self.animations.last_direction.split("_")[1]
                self.animations.Load_animation_frames(self.animations.direction)
            
        
            
            deltatime = self.game.clock.tick(60) / 1000.0
            self.animations.update(deltatime)
        
        self.offset_x = self.pos_x + self.game.player.world_offset_x
        self.offset_y = self.pos_y + self.game.player.world_offset_y

        self.updatecollider()
        self.checkcollisions()

    def updatecollider(self):
        collider_height = self.size_y*5//3
        collider_width = self.size_x* 5
        self.collider = pygame.Rect(self.offset_x, self.offset_y + self.size_y-collider_height, collider_width, collider_height)

    def checkcollisions(self):
        return self.collider.colliderect(self.game.player.collider)
        

    


    def draw(self):
        self.offset_x = self.pos_x + self.game.player.world_offset_x
        self.offset_y = self.pos_y + self.game.player.world_offset_y
        self.updatecollider()
        if self.animations:
            self.animations.draw(self.game, self.offset_x, self.offset_y)
        else:
            sprite_renderer = SpriteSheetRenderer(self.sheets["Idle_Down"])
            scaled_image = sprite_renderer.get_image(self.offset_x, self.offset_y, 5, 0)
            self.game.window.blit(scaled_image, (self.offset_x-self.size_x,self.offset_y-self.size_y*3.5))
       
        pygame.draw.rect(self.game.window, (255,0,0), self.collider, 2)
            
    

    class Player:
        def __init__(self, game):
            self.game = game
            self.player_x = 500
            self.player_y = 500
            

            self.sheets = Entity.image_cache.get("Player") or self.load_images()
            self.direction = "Idle_Down" 

            self.animations = animation(self.sheets, self.direction)
            self.world_offset_x = 0
            self.world_offset_y = 0
            
            
            
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

        def load_images(self):
            images = {
                    "Idle_Right": pygame.image.load("Images/Player/Idle/PlayerIdle.png").convert_alpha(),
                    "Idle_Left": pygame.image.load("Images/Player/Idle/PlayerIdle.png").convert_alpha(),
                    "Walk_Left": pygame.image.load("Images/Player/PlayerWalking/PlayerWalkingleftright.png").convert_alpha(),
                    "Walk_Right": pygame.image.load("Images/Player/PlayerWalking/PlayerWalkingleftright.png").convert_alpha(),
                    "Walk_Down":pygame.image.load("Images\Player\PlayerWalking\PlayerWalkDown.png").convert_alpha(),
                    "Idle_Down":pygame.image.load("Images\Player\Idle\PlayerIdleDown.png").convert_alpha(),
                    "Idle_Up":pygame.image.load("Images\Player\Idle\PlayerIdleUp.png").convert_alpha(),
                    "Walk_Up": pygame.image.load("Images\Player\Idle\PlayerIdleUp.png").convert_alpha(),
            }
            Entity.image_cache["Player"] = images
            return images


        def MainPlayer(self):
            #Exit
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game.exitfunc()
            
            
            self.animations.moving = False
            move_x = 0
            move_y = 0
            
            if keys[pygame.K_LSHIFT]:
                self.movementspeed = 9
                self.animatespeed = 0.01
            else:
                self.movementspeed = 5
                self.animatespeed = 0.05
                self.animatespeed = 0.05

            
            self.colliding = Entity.checkcollisions(self)
            


            if keys[pygame.K_a]:
                self.animations.animationsteps = 0
                if self.animations.direction != "Walk_Left":
                    self.animations.last_direction = "Walk_Left"
                    self.animations.direction = "Walk_Left"
                
                
                move_x = -self.movementspeed
                
                
                    
                

                
                
            
                
                    
        
            if keys[pygame.K_d]:
                self.animations.animationsteps = 0
                if self.animations.direction != "Walk_Right":
                    self.animations.last_direction = "Walk_Right"
                    self.animations.direction = "Walk_Right"
                
                
                move_x = self.movementspeed
                

                
            if keys[pygame.K_s]:
                self.animations.animationsteps = 0
                if self.animations.direction != "Walk_Down":
                    self.animations.last_direction = "Walk_Down"
                    self.animations.direction = "Walk_Down"
                
                
                move_y = self.movementspeed
                

                
            if keys[pygame.K_w]:
                self.animations.animationsteps = 0
                if self.animations.direction != "Walk_Up":
                    self.animations.last_direction = "Walk_Up"
                    self.animations.direction = "Walk_Up"
                
                move_y = -self.movementspeed
            
            if move_x != 0 and move_y != 0:
                move_x *= 0.707
                move_y *= 0.707

            new_x = self.player_x + move_x
            new_y = self.player_y + move_y

            last_x = self.player_x
            last_y = self.player_y

            

            if new_y < self.top_boundry:
                self.world_offset_y += self.movementspeed
            elif new_y > self.bottom_boundry:
                self.world_offset_y -= self.movementspeed
            else:
                self.player_y = new_y

            if new_x < self.left_boundry:
                self.world_offset_x += self.movementspeed
            elif new_x > self.right_boundry:
                self.world_offset_x -= self.movementspeed
            else:
                self.player_x = new_x 
            
            
            

            self.update_playercollider()
                
            

            if any(entity.collider.colliderect(self.collider) for entity in self.game.entities):
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

