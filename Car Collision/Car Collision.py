import pygame,random
from car import Car


pygame.init()



GREY = (128,128,128)
WHITE = (255,255,255)
GREEN = (34,139,34)
RED = (255,0,0)
PURPLE = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
BLUE = (100,100,255)



speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)



SCREENWIDTH = 600
SCREENHEIGHT = 900



size = (SCREENWIDTH,SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")



all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 50, 100, 70)
playerCar.rect.x = 292
playerCar.rect.y = 775

car1 = Car(PURPLE, 50, 100, random.randint(50,100))
car1.rect.x = 140
car1.rect.y = -100
 
car2 = Car(YELLOW, 50, 100, random.randint(50,100))
car2.rect.x = 240
car2.rect.y = -600
 
car3 = Car(CYAN, 50, 100, random.randint(50,100))
car3.rect.x = 340
car3.rect.y = -300
 
car4 = Car(BLUE, 50, 100, random.randint(50,100))
car4.rect.x = 440
car4.rect.y = -900



all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)



all_coming_cars = pygame.sprite.Group()

all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05



    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > SCREENHEIGHT:
            car.changeSpeed(random.randint(50,100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200
    


    car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False)
    for car in car_collision_list:
        print("CRASHED")

        carryOn = False
    
            

    all_sprites_list.update()

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, [0, 0, 100, 900],0)
    pygame.draw.rect(screen, WHITE, [100, 0, 5, 900],0)
    pygame.draw.rect(screen, GREY, [105, 0, 95, 900],0)
    pygame.draw.rect(screen, WHITE, [200, 0, 5, 900],0)
    pygame.draw.rect(screen, GREY, [205, 0, 95, 900],0)
    pygame.draw.rect(screen, WHITE, [300, 0, 5, 900],0)
    pygame.draw.rect(screen, GREY, [305, 0, 95, 900],0)
    pygame.draw.rect(screen, WHITE, [400, 0, 5, 900],0)
    pygame.draw.rect(screen, GREY, [405, 0, 95, 900],0)
    pygame.draw.rect(screen, WHITE, [500, 0, 5, 900],0)
    pygame.draw.rect(screen, GREEN, [505, 0, 100, 900],0)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


