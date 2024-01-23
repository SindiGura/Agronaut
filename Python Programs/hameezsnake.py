"""
Name: Hameez Iqbal
Started in May
- Displaying score begin there
- Boundary death problem
- Collision
- Make snake longer when eating
- Maybe try flappy bird way of text
"""
#Import statements
import pygame 
import time
import random

pygame.init() #imports all Pygame modules

#Create colours using RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Variables Section Begins
#Window measurmeants
dis_width = 600
dis_height  = 400


#Setup
dis = pygame.display.set_mode((dis_width, dis_height)) #creates parameters that will be used for display
pygame.display.set_caption("Hameez's game... Kinda") #Title


#Clock
clock = pygame.time.Clock()


#Snake
snake_block = 10 #size of snake and food
snake_speed = 20


#Text 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)


#Functions
#Displays the score
def Your_score(score): #Displays score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [20, 20])

#Diplays the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#Sets the parameters of the end message
def message(msg,color): #Message functions
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#Game Loop

game_over=False #boolean

def gameLoop(): #Game loop functions
    
    #allows the program to close or restart the game or the player quits
    game_over = False
    game_close = False

   #Starting coordinates / Keeps it centered
    x1 = dis_width / 2
    y1 = dis_height / 2

    #Holds the updated values of the coordinates
    x1_change = 0
    y1_change = 0

    #Snake part
    snake_List = []
    Length_of_snake = 1

    #Randomized coordinates of food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Assigned random range
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


    while not game_over:
     
        while game_close == True:
            dis.fill(blue) #fills background
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1) #updates score 
            pygame.display.update()

            #ends or restart the program based on the player input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #Control Snake movements
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

        #Leave boundary? Dead (Game over).
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        #Movement
        x1 += x1_change
        y1 += y1_change

        dis.fill(blue) #Fill background with ______ colour
        
        #Create Food
        pygame.draw.rect(dis,green,[foodx,foody, snake_block, snake_block]) #Creates rectangle (x, y, height, width)
        
        snake_Head= []
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

        pygame.display.update() #Keep on updating screen

        #Creates Food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed) #speed
    
    #Quit
    pygame.quit() #pygame quits
    quit() #program quits


gameLoop()
