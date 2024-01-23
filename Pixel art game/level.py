import pygame 
from tiles import Tile 
from settings import tile_size, screen_width
from player import Player 

class Level:
    def __init__(self, level_data, surface):

        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift = 0 # Level shifting 

    def setup_level(self, layout): #level data
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle() 

        for row_index, row in enumerate(layout): #level data/map
            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)  #Add to group
                
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite) #Add to group

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx #taking the center position of the player
        direction_x = player.direction.x  #direction player is moving in 

        if player_x < screen_width / 7 and direction_x <0: #if the player is at the left end of the screen and moves left
            self.world_shift = 8 
            player.speed = 0 #player speed drops so they stay in the screen

        elif player_x > screen_width - (screen_width / 2) and direction_x >0: #if the screen scrolls beyond the right side 
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0 #else world stops shifting and player can move
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed # updating player direction and speed

        for sprite in self.tiles.sprites():   
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity() # applying gravity
       
        for sprite in self.tiles.sprites():   
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):

        #level tiles

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x() #scroll through the screen when player reaches end

        #player

        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
        