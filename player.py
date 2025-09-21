import pygame
from circleshape import *
from constants import *
from main import *
from shot import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, width=2 )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        if self.cooldown > 0:
            pass
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS) 
        shot.velocity = pygame.Vector2(0, 1) * PLAYER_SHOT_SPEED
        shot.velocity = shot.velocity.rotate(self.rotation)


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                pass
            else:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN

