import pygame
from sys import exit

pygame.init()

#essentials
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Disoriented")
clock=pygame.time.Clock()
score=pygame.font.Font('font/Pixeltype.otf',30)
gamestatus=True

#surfaces
skys=pygame.image.load('graphics/Sky.png').convert()
grounds=pygame.image.load('graphics/ground.png').convert()

scores=score.render('SCORE', False, 'pink')
scorer=scores.get_rect(topleft=(5,-3))

hounds=pygame.image.load('graphics/snail/tile000.png').convert_alpha()
'''38 24'''
hounds = pygame.transform.scale(hounds, (80, 48))
houndr=hounds.get_rect(midbottom=(900,300))

players=pygame.image.load('graphics/Player/player1.png').convert_alpha()
'''37 39 -> 44 60'''
players = pygame.transform.scale(players, (75,100))
playerr=players.get_rect(midbottom=(50,300))
playerg=0

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
                    playerg=-20
            if event.type == pygame.KEYUP:
                print("keydown")
        else:
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestatus=True    
                    houndr.right=800    

    if gamestatus==True:
        screen.blit(skys,(0,0))
        screen.blit(grounds,(0,300))
        screen.blit(scores,scorer)
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
        screen.fill('red')

    pygame.display.update()
    clock.tick(60)