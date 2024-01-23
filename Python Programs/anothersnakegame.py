import pygame
import time
import random
import neat
 
pygame.init()
                     

# Establishes colors
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (157, 193, 131)
blue = (50, 153, 213)

# Dimensions for window/display
 
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game Extreme Pixel') #Titles the top part 
 
#Sets the speed of the snake 

clock = pygame.time.Clock() 
snake_speed = 20

#Changes size of snake and fruit 

snake_block = 10

#Sets the fonts for the score and the end message 
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)
 
#Displays the score 

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [20, 20])

#Displays the snake
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

#Sets the paramenters for the end message 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 7.5, dis_height / 2.5])
 

# GAME LOOP 

def gameLoop():

    #allow the program to close or restart when the game ends or the player quits 
    
    game_over = False
    game_close = False
 
    #starting coordinates 

    x1 = dis_width / 2
    y1 = dis_height / 2

    #holds the updated values of the coordinates 
 
    x1_change = 0
    y1_change = 0

    #creates snake 
 
    snake_List = []
    Length_of_snake = 1

    #randomizes the coordinates of the food 
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:

            dis.fill(green) #fills background color for end message 
            message("You Lost! Press C-Play Again or Q-Quit", red) #creates end message 
            Your_score(Length_of_snake - 1) #updates score 
            pygame.display.update()
 
            #ends or restarts the program based on player input 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #moves snake and connects it to keyboard 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        #moving 
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(green)
        
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        #makes head 
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()

        #creates food  
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
