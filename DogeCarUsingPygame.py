import pygame # importing pygame module
import time
import random 

x = pygame.init()

white = (255 , 255 , 255 )
red = (255 , 0 , 0 )
black = ( 0 , 0 , 0 )
green = (0 , 255 , 0)
blue = ( 0 , 0 , 225)

screen_width = 300
screen_height = 600

clock = pygame.time.Clock()

gameWindow = pygame.display.set_mode(( screen_width , screen_height ))

font = pygame.font.SysFont(None,55)



def textScreen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text, [x,y])



def plot_block(gameWindow , color , block_x , block_y , block_size_y , block_size_x):
    pygame.draw.rect(gameWindow , color , [ block_x , block_y , block_size_y , block_size_x ])
    
def gameloop():

    block_size = 50

    block_x = 150
    block_y = 500

    firstObject_x = 50 
    firstObject_y = 20

    secondObject_x = 20
    secondObject_y =  250

    thirdObject_x = 200
    thirdObject_y = 300

    velocity_x = 10
    velocity_y = 3

    exit_game = False
    game_over = False

    count = 0

    gameWindow.fill(white)
    textScreen(" Game Over !" , red , 150 , 300 )


    # This is the main gaming loop
    while not exit_game :

        if game_over :
            gameWindow.fill(white)
            textScreen(" Game Over ! Press Enter to Restart" , red , 150 , 300 )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    exit_game = True


                
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_w:
                        if block_y > 0 :
                            block_y -= 75
                        

                    if event.key == pygame.K_a:
                        if block_x > 0 :
                            block_x -= 20

                    if event.key == pygame.K_d:
                        if block_x < 250 :
                            block_x += 20

                    if block_y < 500 :
                        if event.key == pygame.K_s:
                            block_y += 75

        gameWindow.fill(blue)

        plot_block(gameWindow , black , block_x , block_y , block_size , 100 )

        if ( secondObject_y > 650):
            secondObject_x = random.randint(20 , screen_width/2)
            secondObject_y = -100
            plot_block(gameWindow, white , secondObject_x ,secondObject_y , 75, 100 )

        elif ( firstObject_y > 630 ):
            firstObject_x = random.randint(20 , screen_width)
            firstObject_y = -120
            plot_block(gameWindow, red , firstObject_x ,firstObject_y , 75 , 100 )

        elif ( thirdObject_y > 660) :
            thirdObject_x = random.randint(20 , screen_width)
            thirdObject_y = -150
            plot_block(gameWindow, red , thirdObject_x ,thirdObject_y , 75 , 100 )

        else:
            firstObject_y += velocity_y 
            secondObject_y += velocity_y + 3
            thirdObject_y += velocity_y + 2

            if block_y == firstObject_y or block_y == secondObject_y or block_y == thirdObject_y :
                game_over = True
                
            elif block_x == firstObject_x or block_x == secondObject_x or block_x == thirdObject_x :
                game_over = True

            plot_block(gameWindow, red , firstObject_x ,firstObject_y , 50 , 100)
            plot_block(gameWindow, white , secondObject_x ,secondObject_y , 50 , 100)
            plot_block(gameWindow, green , thirdObject_x , thirdObject_y , 75 , 100 )

        count = count + 1
        velocity_y += count/10000 #This will increase the speed of the blocks with the time 
        textScreen("Score : " + str(count/30) , red , 5 , 5)
        
        # Conditions when player will be out

        

        pygame.display.update()
        clock.tick(25)

        time.sleep(0)

    pygame.quit()
    quit()


gameloop()

    