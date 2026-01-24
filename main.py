import pygame
from constants import * # Using * to get all constants easily
from logger import log_state
from player import Player
from asteroid import Asteroid         # New import
from asteroidfield import AsteroidField # New import

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # 1. Create the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() # New group for asteroids

    # 2. Set containers for the classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # 3. Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() # This handles spawning automatically

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Updates all objects (Player and Asteroids and the Field)
        updatable.update(dt)

        screen.fill("black")

        # Draws all objects (Player and Asteroids)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()