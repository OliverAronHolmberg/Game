import pygame
from Renderer_script import SpriteSheetRenderer


class animation:
    class Playeranimations:
        def __init__(self):

            
            self.sheets = {"Idle": pygame.image.load("Images\Player\Idle\PlayerIdle.png").convert_alpha(),
                            "Walk_Left":pygame.image.load("Images\Player\PlayerWalking\PlayerWalkingleftright.png").convert_alpha(),
                            "Walk_Right":pygame.image.load("Images\Player\PlayerWalking\PlayerWalkingleftright.png").convert_alpha()
                                }
            
            self.playeranimationlist = {key: [] for key in self.sheets.keys()}

            self.direction = "Idle"
            self.moving = False

            

            self.animationsteps = 2
            self.animation_index = 0
            self.animation_timer = 0.0
            self.animation_speed = 0.1

            self.LoadPlayer(self.direction)

        def LoadPlayer(self, direction):
            
            if not self.playeranimationlist[direction]:
                self.playeranimationlist[direction] = []
                sprite_sheet = SpriteSheetRenderer(self.sheets[direction])
            

            self.playeranimationlist[direction] = []
            self.sprite_sheet = SpriteSheetRenderer(self.sheets[direction])
            

            if direction == "Idle":
                self.animationsteps = 2
            elif direction in ["Walk_Right", "Walk_Left"]:
                self.animationsteps = 6

            
            for x in range(self.animationsteps):
                frame = self.sprite_sheet.get_image(14, 20, 5, x)
                self.playeranimationlist[direction].append(frame)
            
            
            

            
            
        def update(self, deltatime):
            self.animation_timer += deltatime

            if self.animation_timer >= self.animation_speed:
                self.animation_index += 1
                
                if self.animation_index >= len(self.playeranimationlist[self.direction]):
                    self.animation_index = 0

                self.animation_timer = 0


        def draw(self, game, player_x, player_y):
            if self.playeranimationlist[self.direction]:
                frame = self.playeranimationlist[self.direction][self.animation_index]
                match self.direction:
                    case "Idle":
                        pass
                    case "Walk_Right":
                        pass
                    case "Walk_Left":
                        frame = pygame.transform.flip(frame, True, False)
                    
                game.window.blit(frame, (player_x, player_y))
            