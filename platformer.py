import pygame
from sys import exit

pygame.init()

#essentials
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Disoriented")
clock=pygame.time.Clock()
score=pygame.font.Font('font/Pixeltype.otf',30)

#surfaces
skys=pygame.image.load('graphics/Sky.png').convert()
grounds=pygame.image.load('graphics/ground.png').convert()

scores=score.render('SCORE', False, 'pink')
scorer=scores.get_rect(topleft=(5,-3))

hounds=pygame.image.load('graphics/snail/tile000.png').convert_alpha()
hounds = pygame.transform.scale(hounds, (144,72))
houndr=hounds.get_rect(midbottom=(900,300))

players=pygame.image.load('graphics/Player/player.png').convert_alpha()
players = pygame.transform.scale(players, (128, 128))
playerr=players.get_rect(midbottom=(50,318))
playerg=0

#loops and placements
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playerr.bottom==318:
                    playerg=-20    
                else:
                    pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playerr.collidepoint(event.pos):
                playerg=-20
        if event.type == pygame.KEYUP:
            print("keydown")

    pygame.display.update()
    clock.tick(60)
    screen.blit(skys,(0,0))
    screen.blit(grounds,(0,300))
    screen.blit(scores,scorer)
    houndr.right+=-5
    if houndr.right<-100:
        houndr.right=900
    screen.blit(hounds,houndr)
    playerg+=1.1
    playerr.y+=playerg
    if playerr.bottom>=318:
        playerr.bottom=318
    screen.blit(players,playerr)


pygame.close()