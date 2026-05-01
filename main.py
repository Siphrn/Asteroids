import sys
import pygame
from circleshape import CircleShape
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    # Log some initial info about the game environment
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame and create the game window

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up the game clock for managing frame rate and delta time


    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups and initialize the player

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop

    while True:
        log_state() # Logs state of spires

        updatable.update(dt) # Updates all sprites in updatable group

        for asteroid in asteroids: # Checks for collisions between player and asteroids
            if player.collides_with(asteroid):
                log_event("player_hit") # Logs collision event
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot") # Logs collision event
                    asteroid.split()
                    shot.kill()
        
        screen.fill("black") # - 
        for thing in drawable: # Draws all sprites in draw group
            thing.draw(screen)

        pygame.display.flip() # - 

        for event in pygame.event.get(): # For quitting the game 
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and convert to seconds 



if __name__ == "__main__":
    main()
