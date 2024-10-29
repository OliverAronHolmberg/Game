import pygame
from Renderer_script import SpriteSheetRenderer

class animation:
    class Playeranimations:
        def __init__(self):
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

            self.playeranimationlist = {key: [] for key in self.sheets.keys()}

            self.direction = "Idle_Right"  
            self.moving = False
            self.last_direction = self.direction

            self.animation_index = 0
            self.animation_timer = 0
            self.animation_speed = 0.1

            
            self.LoadPlayer(self.direction)

        def LoadPlayer(self, direction):
            
            if not self.playeranimationlist[direction]:
                sprite_sheet = SpriteSheetRenderer(self.sheets[direction])

                if direction in ["Idle_Right", "Idle_Left", "Idle_Down", "Idle_Up", "Walk_Up"]:
                    self.animationsteps = 2 
                elif direction in ["Walk_Right", "Walk_Left"]:
                    self.animationsteps = 6 
                elif direction in ["Walk_Down"]:
                    self.animationsteps = 8

                for x in range(self.animationsteps):
                    frame = sprite_sheet.get_image(14, 20, 5, x)
                    self.playeranimationlist[direction].append(frame)
                

            
            

        def update(self, deltatime):
            self.animation_timer += deltatime
            if self.animation_timer >= self.animation_speed and self.playeranimationlist[self.direction]:
                self.animation_index = (self.animation_index + 1) % len(self.playeranimationlist[self.direction])
                self.animation_timer = 0

                  

        def change_direction(self, new_direction):
            if new_direction != self.direction:
                self.direction = new_direction
                self.animation_index = 0  
                self.LoadPlayer(new_direction)  

        def draw(self, game, player_x, player_y):
            
            if self.playeranimationlist[self.direction]:

                if self.animation_index < len(self.playeranimationlist[self.direction]):
                    frame = self.playeranimationlist[self.direction][self.animation_index]
                else:
                    self.animation_index = 0
                    frame = self.playeranimationlist[self.direction][self.animation_index]
            

                
                match self.direction:
                    case "Idle_Left":
                        frame = pygame.transform.flip(frame, True, False)
                    case "Walk_Left":
                        frame = pygame.transform.flip(frame, True, False)
                    case "Idle_Right":
                        pass
                    case "Walk_Right":
                        pass
                    case "Walk_Down":
                        pass
                    case "Idle_Down":
                        pass
                    case "Idle_Up":
                        pass


                game.window.blit(frame, (player_x, player_y))
