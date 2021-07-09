import pygame
import random   #for creating food at random location
pygame.init()   #for initializing  all pygame modules
#defining screen coords
width=400
height=500
white=(255,255,255)
red=(255,0,0)  #RGB codes
green=(0,255,0)
black=(0,0,0)
blue=(0,0,255)
snake_size=10 
#using clock for counting 
clock=pygame.time.Clock()
def_font= pygame.font.SysFont(None,45)
window=pygame.display.set_mode((width,height))
pygame.display.set_caption(("Snake Game"))  #Title of window
pygame.display.update()
def disp_text(text,color,x,y):
    text_=def_font.render(text,True,color)
    window.blit(text_,[x,y])
def plot_snk(snk_body):
    for x,y in snk_body:
        pygame.draw.rect(window,green,(x,y,snake_size,snake_size))
def start_game():
    score=0
    exit=False 
    vel_x=0
    snk_body=[]
    snk_len=1
    snake_x=50 
    snake_y=50
    vel_y=0 #for motion
    fps=10  # for update time 
    #   FOOD
    food_x=random.randint(10,width)
    food_y=random.randint(10,height)
    game_over=False
    while not exit:
        if game_over==True:
            window.fill(white)
            disp_text("GAME OVER !!!",red,int(width/2-50),int(height/2))
            disp_text("Press ENTER to continue ",blue,int(width/2-60),int(height/2+50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit=True
                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_RETURN:
                        start_game()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x=5
                        vel_y=0
                    if event.key == pygame.K_UP:
                        vel_y=-5
                        vel_x=0
                    if event.key == pygame.K_LEFT:
                        vel_x=-5
                        vel_y=0
                    if event.key == pygame.K_DOWN:
                        vel_y=5
                        vel_x=0
            # if vel_x or vel_y is defined then the snake moves in straight line
            snake_x=snake_x+vel_x
            snake_y=snake_y+vel_y       # moves the snake with the operation
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1
                snk_len+=5
                food_x=random.randint(10,width/2)
                food_y=random.randint(10,height/2)
            head=[snake_x,snake_y]
            snk_body.append(head)
            #snk_body.append(snk_len)
            window.fill(white)
            disp_text("Score : "+str(score*5),black,5,5)
            #inc_snk(snake_x,snake_y,snk_body)
            plot_snk(snk_body)
            if snake_x not in range(0,width) or snake_y not in range(0,height):
                game_over=True
            if head in snk_body[:-2]:
                game_over=True
            if len(snk_body)>snk_len:
                del snk_body[0]
            pygame.draw.rect(window,red,(food_x,food_y,snake_size,snake_size))
        pygame.display.update()     #necessary to get the changes
        clock.tick(fps)
    pygame.quit()
    quit()
start_game()