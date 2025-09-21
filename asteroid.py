import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):   
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
        #circle(surface, color, center, radius, width=0
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this ws a small asteroid"
        else:
            angle = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(angle) 
            vel_2 = self.velocity.rotate(angle * -1) 
            radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position[0], self.position[1], radius)
            asteroid2 = Asteroid(self.position[0], self.position[1], radius)
            asteroid1.velocity = vel_1 * 1.2
            asteroid2.velocity = vel_2 * 1.2
            




