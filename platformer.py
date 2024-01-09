import pygame
from sys import exit

#functions
def dispscore():
    currtime = pygame.time.get_ticks()-timestart 
    scorens = scoren.render(f'. {currtime//100}',False,'pink')   
    scorenr = scorens.get_rect(topleft=(100,1))
    screen.blit(scorens,scorenr)
    return currtime

#essentials
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Disoriented")
clock=pygame.time.Clock()
menufont1=pygame.font.Font('font/Pixeltype3.ttf',80)
menufont2=pygame.font.Font('font/Pixeltype3.ttf',50)
scoren=pygame.font.Font('font/Pixeltype2.ttf',43)
scorena=pygame.font.Font('font/Pixeltype2.ttf',55)
score=pygame.font.Font('font/Pixeltype.otf',30)
gamestatus=False
timestart=0
finscore=0

#surfaces
skys=pygame.image.load('graphics/Sky.png').convert()
grounds=pygame.image.load('graphics/ground.png').convert()

scores=score.render('SCORE', False, 'pink')
scorer=scores.get_rect(topleft=(10,-3))

hounds=pygame.image.load('graphics/snail/tile000.png').convert_alpha()
'''38 24'''
hounds = pygame.transform.scale(hounds, (80, 48))
houndr=hounds.get_rect(midbottom=(900,300))

players=pygame.image.load('graphics/Player/player1.png').convert_alpha()
'''37 39 -> 44 60'''
players = pygame.transform.scale(players, (75,100))
playerr=players.get_rect(midbottom=(50,300))
playermenur=players.get_rect(center=(400,232))
playerg=0

menus=pygame.image.load('graphics/bg.png').convert_alpha()
menur=menus.get_rect(center=(400,200))

#timer
tim1=pygame.USEREVENT +1 

#loops and placements
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if gamestatus==True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playerr.bottom==300:
                        playerg=-20    
                    else:
                        pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerr.collidepoint(event.pos):
                    if playerr.bottom==300:
                        playerg=-20

        else:
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestatus=True    
                    houndr.right=800 
                    timestart=pygame.time.get_ticks()
            if event.type==pygame.MOUSEBUTTONDOWN:
                gamestatus=True    
                houndr.right=800    
                timestart=pygame.time.get_ticks()   

    if gamestatus==True:
        screen.blit(skys,(0,0))
        screen.blit(grounds,(0,300))
        screen.blit(scores,scorer)
        finscore=dispscore()
        houndr.right+=-5
        if houndr.right<-100:
            houndr.right=900
        screen.blit(hounds,houndr)
        playerg+=0.96
        playerr.y+=playerg
        if playerr.bottom>=300:
            playerr.bottom=300
        screen.blit(players,playerr)

        if houndr.colliderect(playerr):
            gamestatus=False

    else:
        screen.blit(menus,menur)
        menufonts1=menufont1.render('(DISORIENTED)',False,'yellow')
        menufontr1=menufonts1.get_rect(center=(400,100))
        menufonts3=scorena.render(f'SCORE . {finscore//100}',False,'yellow')
        menufontr3=menufonts3.get_rect(center=(400,350))
        if finscore==0:
            menufonts2=menufont2.render('PRESS SPACE TO PLAY',False,'yellow')
            menufontr2=menufonts2.get_rect(center=(400,350))
            screen.blit(menufonts2,menufontr2)
        else:
            screen.blit(menufonts3,menufontr3)
        screen.blit(menufonts1,menufontr1)
        screen.blit(players,playermenur)

    pygame.display.update()
    clock.tick(60)