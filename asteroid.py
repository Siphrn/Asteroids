from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        newVector1 = self.velocity.rotate(angle)
        newVector2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid1.velocity = newVector1 * 1.2

        Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid2.velocity = newVector2 * 1.2




