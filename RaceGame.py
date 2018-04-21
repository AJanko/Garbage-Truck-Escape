import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


background_image = pygame.image.load("indeks.jpg")
enemy = pygame.image.load("trashmaster.png")
carImg = pygame.image.load('porsche.png')
point = pygame.image.load('point.png')

car_height = 90
car_width = 45

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Would you escape from a garbage truck?')
clock = pygame.time.Clock()



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))


def things(thingx,thingy):
    gameDisplay.blit(enemy, (thingx,thingy))


def speed_addition(sx,sy):
    gameDisplay.blit(point, (sx,sy))
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('GAME OVER')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    sa_starty = -400
    sa_startx = random.randrange(50, display_width - 50)
    sa_width = 50
    sa_height = 50
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 152
    thing_height = 72
    
    car_speed_change = 5
    dodged = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed_change
                if event.key == pygame.K_RIGHT:
                    x_change = car_speed_change
                if event.key == pygame.K_UP:
                    y_change = -(car_speed_change - 1)
                if event.key == pygame.K_DOWN:
                    y_change = car_speed_change - 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change           #pozycja samochodu
        y += y_change
        
        gameDisplay.blit(background_image, [0,0])       #wyswietlanie tla
        
        things(thing_startx, thing_starty)
        dg = dodged % 10
        if dg == 0 and dodged > 9:
            speed_addition(sa_startx, sa_starty)
        
        thing_starty += thing_speed
        sa_starty += (thing_speed + 1)
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:  #Jesli pojazd wyjedzie poza droge
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width - thing_width)
            dodged += 1
            if (dodged % 7 == 0):
                thing_speed += 1

        #print(dg,"-----",sa_startx,"-",sa_starty)
        if sa_starty > 1500:
            if (dg == 0):
                sa_starty = 0 - sa_height
                sa_startx = random.randrange(50, display_width - 50)

        if thing_startx + thing_width - 20 > x  > thing_startx - car_width + 15:
            if thing_starty + thing_height - 20 > y > thing_starty:
                crash()
            if thing_starty + thing_height > y + car_height > thing_starty:
                crash()

        #if kolizja z speed_addition then car_speed_change += 1 and point undisplay
        if sa_startx + sa_width > x  > sa_startx - car_width:
            if sa_starty + sa_height > y > sa_starty:
                car_speed_change += 1
                sa_starty = 700
            if sa_starty + sa_height > y + car_height > sa_starty:
                car_speed_change += 1
                sa_starty = 700
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
