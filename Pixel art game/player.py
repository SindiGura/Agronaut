import pygame 
from support import import_floder 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        #Player movement 
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16 #negative because the player is jumping up


    def import_character__assets(self):
        character_path = to be decided
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation 
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump() 

    def apply_gravity(self):
        self.direction.y += self.gravity #applying gravity to the direction and self rect
        self.rect.y += self.direction.y 

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input() # Getting keyboard input
        self.rect.x += self.direction.x * self.speed # updating player direction and speed
        self.apply_gravity() # applying gravity