import pygame



class animation:
    class Playeranimations:
        def __init__(self):
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