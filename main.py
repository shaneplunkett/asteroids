import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatetable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatetable, drawable)
    Asteroid.containers = (updatetable, drawable, asteroids)
    AsteroidField.containers = updatetable
    Shot.containers = (updatetable, drawable, bullets)

    protag = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        for object in drawable:
            object.draw(screen)
        for object in updatetable:
            object.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()
        for object in asteroids:
            if protag.collide(object):
                print("Game Over!")
                exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
