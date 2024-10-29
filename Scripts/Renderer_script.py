import pygame

class SpriteSheetRenderer:
    def __init__(self, image):
        self.image = image

    def get_image(self, width, height, scale, frame):
            image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
            image.blit(self.image, (0 , 0), ((frame*width) , 0, width, height))
            image = pygame.transform.scale(image, (width*scale, height*scale))

            return image
    
    