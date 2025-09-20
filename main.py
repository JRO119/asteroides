import pygame
from constants import *
from player import *
from circleshape import *


def main():
    ### starting tasks ###
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    ### setup variables ###
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    ### initiate player ###
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    
    ### start game loop ###
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for dr in drawable:
            dr.draw(screen)        
        
        ### do last after all drawings ##
        pygame.display.flip()


if __name__ == "__main__":
    main()
