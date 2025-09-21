import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *


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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    ### initiate players ###
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    asteroidfield = AsteroidField()
    
    ### start game loop ###
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if not asteroid.collision(player):
                print("Game over!!")
                exit()
            
            

        for dr in drawable:
            dr.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if not asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                pass
            pass
        
        ### do last after all drawings ##
        pygame.display.flip()


if __name__ == "__main__":
    main()
