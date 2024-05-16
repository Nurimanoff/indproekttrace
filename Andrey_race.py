import pygame
import os
import random
os.chdir(os.path.dirname(os.path.abspath(__file__)))
screen_h = 1000
screen_w = 600
clock = pygame.time.Clock() 
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.init()
car1 = pygame.image.load('car1.bmp')
car2 = pygame.image.load('car2.bmp')
car3 = pygame.image.load('car3.bmp')
ROAD_COLOR = (66, 61, 56)
BLACK = (0,0,0)
WHITE = (255,255,255)
SIDE_COLOR = (179, 135, 100)
GRASS_COLOR = (19, 120, 44)

screen.fill(ROAD_COLOR)
car_width = 100
car_height = 200
car1 = pygame.transform.rotate(car1,180)
car2 = pygame.transform.rotate(car2,180)
car3 = pygame.transform.rotate(car3,180)
car1 = pygame.transform.scale(car1, (car_width,car_height))
car2 = pygame.transform.scale(car2, (car_width,car_height))
car3 = pygame.transform.scale(car3, (car_width,car_height))

# car2 = pygame.transform.rotate(car2,45)
car_arr = [car1,car2,car3]
race1_x,race2_x,race3_x = 100,240,380
arr_race = [race1_x,race2_x,race3_x]

screen.blit(car_arr[0],(race1_x,150))
current_race = 1

screen.blit(car_arr[2],(race3_x,10))
is_w = True
arr_cars = [car_arr[0],car_arr[2]]
c1_race = 0
c2_race = 0
c1_y = -car_height
c2_y = -car_height
c1_speed = random.randint(3,4)
c2_speed = random.randint(3,4)
car_pos_y = screen_h-car_height

while(c1_race==c2_race):
    c1_race = random.randint(0,2)
while is_w:
    if c1_y >= screen_h+car_height:
        c1_y = -car_height
        c1_speed = random.randint(1,3)
        c1_race = random.randint(0,2)
        if(c1_race==c2_race):
            while(c1_race==c2_race):
                c1_race = random.randint(0,2) 
    if c2_y >= screen_h+car_height:
        c2_y = -car_height
        c2_speed = random.randint(1,3)
        c2_race = random.randint(0,2)
        if(c1_race==c2_race):
            while(c1_race==c2_race):
                c2_race = random.randint(0,2) 
    if c1_race == current_race:
        if c1_y >= screen_h-car_height*2 and c1_y <= screen_h:
            is_w = False
    if c2_race == current_race:
        if c2_y >= screen_h-car_height*2 and c2_y <= screen_h:
            is_w = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_w = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and current_race != 0:
                temp_car = car_arr[1]
                car_arr[1] = pygame.transform.rotate(car_arr[1],10)
                pygame.draw.rect(screen,ROAD_COLOR,(arr_race[current_race],car_pos_y,car_width,car_height))
                screen.blit(car_arr[1],(arr_race[current_race],car_pos_y))
                current_race -=1
                pygame.display.flip()
                clock.tick(500)
                pygame.draw.rect(screen,ROAD_COLOR,(arr_race[current_race+1],car_pos_y,car_width,car_height))
                car_arr[1] = temp_car
            if event.key == pygame.K_d and current_race != 2:
                temp_car = car_arr[1]
                car_arr[1] = pygame.transform.rotate(car_arr[1],-10)
                pygame.draw.rect(screen,ROAD_COLOR,(arr_race[current_race],car_pos_y,car_width,car_height))
                screen.blit(car_arr[1],(arr_race[current_race],car_pos_y))
                current_race +=1
                pygame.display.flip()
                clock.tick(500)
                pygame.draw.rect(screen,ROAD_COLOR,(arr_race[current_race-1],car_pos_y,car_width,car_height))
                car_arr[1] = temp_car


    screen.fill(ROAD_COLOR)
    screen.blit(car_arr[1],(arr_race[current_race],car_pos_y)) 

    screen.blit(arr_cars[0],(arr_race[c1_race],c1_y)) 
    screen.blit(arr_cars[1],(arr_race[c2_race],c2_y))

    pygame.draw.rect(screen,GRASS_COLOR,(0,0,90,screen_h))
    pygame.draw.rect(screen,GRASS_COLOR,(screen_w-110,0,110,screen_h))
    pygame.draw.line(screen,SIDE_COLOR,[90,0],[90,screen_h],5)
    for i in range(0,40,2):
        pygame.draw.line(screen,WHITE,[220,i*27+27],[220,i*27],5)
    for i in range(0,40,2):
        pygame.draw.line(screen,WHITE,[360,i*27+27],[360,i*27],5)
    pygame.draw.line(screen,SIDE_COLOR,[490,0],[490,screen_h],5) 
    pygame.time.delay(10) 
    c1_y+=c1_speed
    c2_y+=c2_speed       
    pygame.display.flip()