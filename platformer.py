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
scorer=scores.get_rect(center=(60,20))

hounds=pygame.image.load('graphics/snail/tile000.png').convert_alpha()
hounds = pygame.transform.scale(hounds, (144,72))
houndr=hounds.get_rect(midbottom=(900,300))

players=pygame.image.load('graphics/Player/player.png').convert_alpha()
players = pygame.transform.scale(players, (128, 128))
playerr=players.get_rect(midbottom=(50,318))

#loops and placements
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(60)
    screen.blit(skys,(0,0))
    screen.blit(grounds,(0,300))
    screen.blit(scores,scorer)
    houndr.right+=-5
    if houndr.right<-100:
        houndr.right=900
    screen.blit(hounds,houndr)
    screen.blit(players,playerr)


pygame.close()