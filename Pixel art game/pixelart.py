import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        """
        self.image = pygame.Surface([20,20])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        """

        self.is_right = False
        self.is_left = False
        self.turn = 0 
        
        self.sprites = []
        self.sprites.append(pygame.image.load(r"C:\Users\Cindy\OneDrive\Desktop\Past coding\Pixel art game\pixil-frame-0.png").convert())
        self.sprites.append(pygame.image.load(r"C:\Users\Cindy\OneDrive\Desktop\Past coding\Pixel art game\pixil-frame-1.png").convert())
        self.sprites.append(pygame.image.load(r"C:\Users\Cindy\OneDrive\Desktop\Past coding\Pixel art game\pixil-frame-2.png").convert())
        self.sprites.append(pygame.image.load(r"C:\Users\Cindy\OneDrive\Desktop\Past coding\Pixel art game\pixil-frame-3.png").convert())

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]


    def walkRight(self):

        self.is_right = True
        self.pos_x+=1

    def walkLeft(self):

        self.is_left = True
        self.pos_x+=-1

        
    def update(self):

        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite-=0.2
                self.is_animating = False
                
            self.image = self.sprites[int(self.current_sprite)]

        if self.is_right == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite-=0.2
                self.is_animating = False



# General setup

pygame.init()
clock = pygame.time.Clock()

# Game screen

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")


# Createing the sprite and groups

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

# If player wants to quit

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                location -= 1
            if event.key == pygame.K_RIGHT:
                location += 1
    

    

    # DRAWING

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)



"""

diretion = 0/1/-1
location = x_pos


"""





















    
