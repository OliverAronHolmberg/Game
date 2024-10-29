import pygame
from Renderer_script import SpriteSheetRenderer

class Player:
    def __init__(self, game):
        self.game = game
        self.player_x = 100
        self.player_y = 100

        self.facingleft = False

        self.sheets = {"Idle": pygame.image.load("Images\Player\Idle\PlayerIdle.png").convert_alpha(),
                       "Walk":pygame.image.load("Images\Player\PlayerWalking\PlayerWalkingleftright.png").convert_alpha(),
                        }
        
        self.playeranimationlist = {"Idle": [],
                                    "Walk": [],
                                    }

        self.animationsteps = 2
        self.current_animation = "Idle"
        self.animation_index = 0
        self.animation_timer = 0.0
        self.animation_speed = 0.1
        self.frames_per_animation = 4
        


    def LoadPlayer(self):

        self.sprite_sheet = SpriteSheetRenderer(self.sheets[self.current_animation])
        self.playeranimationlist[self.current_animation] = []

        if self.current_animation == "Idle":
            self.animationsteps = 2
        elif self.current_animation == "Walk":
            self.animationsteps = 6

        
        for x in range(self.animationsteps):
            frame = self.sprite_sheet.get_image(14, 20, 5, x)
            self.playeranimationlist[self.current_animation].append(frame)
        
        
        

        
        
    def update(self, deltatime):
        self.animation_timer += deltatime

        if self.animation_timer >= self.animation_speed:
            self.animation_index += 1
            
            if self.animation_index >= len(self.playeranimationlist[self.current_animation]):
                self.animation_index = 0

            self.animation_timer = 0
            

    def MainPlayer(self):
        #Exit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.exitfunc()
        

        self.moving = False

        if keys[pygame.K_a]:
            if self.current_animation != "Walk":
                self.current_animation = "Walk"
                
                self.LoadPlayer()
            self.facingleft = True
            self.player_x -=5
            self.moving = True
            
            
            
        if keys[pygame.K_d]:
            if self.current_animation != "Walk":
                self.current_animation = "Walk"
                
                self.LoadPlayer()
            self.facingleft = False
            self.player_x +=5
            self.moving = True

        if not self.moving:
            if self.current_animation != "Idle":
                self.current_animation = "Idle"
                
                self.LoadPlayer()
            

    def draw(self):
        if self.playeranimationlist[self.current_animation] and self.animation_index < len(self.playeranimationlist[self.current_animation]):
            frame = self.playeranimationlist[self.current_animation][self.animation_index]
            if self.facingleft:
                frame = pygame.transform.flip(frame, True, False)
            self.game.window.blit(frame, (self.player_x, self.player_y))
    

        #PlayerControls
