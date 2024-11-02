import pygame
from Renderer_script import SpriteSheetRenderer

class animation:

    def __init__(self, sheets, direction):
            
            self.sheets = sheets
            self.direction = direction

            self.playeranimationlist = {key: [] for key in self.sheets.keys()}

             
            self.moving = False
            self.last_direction = self.direction

            self.animation_index = 0
            self.animation_timer = 0
            self.animation_speed = 0.1

            
            self.Load_animation_frames(self.direction)

    def Load_animation_frames(self, direction):
            
            if not self.playeranimationlist[direction]:
                sprite_sheet = SpriteSheetRenderer(self.sheets[direction])
                self.animationsteps = self.get_animation_steps(direction)
                

                for x in range(self.animationsteps):
                    frame = sprite_sheet.get_image(14, 20, 5, x)
                    self.playeranimationlist[direction].append(frame)
                
    def get_animation_steps(self, direction):
            if direction in ["Idle_Right", "Idle_Left", "Idle_Down", "Idle_Up", "Walk_Up"]:
                    return 2 
            elif direction in ["Walk_Right", "Walk_Left"]:
                    return 6 
            elif direction in ["Walk_Down"]:
                    return 8
            return 0
            

    def update(self, deltatime):
            self.animation_timer += deltatime
            if self.animation_timer >= self.animation_speed and self.playeranimationlist[self.direction]:
                self.animation_index = (self.animation_index + 1) % len(self.playeranimationlist[self.direction])
                self.animation_timer = 0

                  

    def change_direction(self, new_direction):
            if new_direction != self.direction:
                self.direction = new_direction
                self.animation_index = 0  
                self.Load_animation_frames(new_direction)  

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
                    


                game.window.blit(frame, (player_x, player_y))



        






        
