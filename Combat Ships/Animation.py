import pygame
import config

aux = 0


class AnimationGif(pygame.sprite.Sprite):
    def __init__(self, path, tiles, pos_x, pos_y, w, h, speed, play_once):
        super().__init__()
        self.sprites = []
        self.speed = speed
        self.w = w
        self.h = h
        self.play_once = play_once

        for i in range(0, tiles):
            image = pygame.image.load(f"{path}{i:03d}.png")
            self.sprites.append(image)

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (w, h))

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def update(self):
        global aux
        self.current_sprite += self.speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            if self.play_once == 1:
                self.kill()

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.sprites[int(self.current_sprite)], (self.w, self.h))


yipee_sprites = pygame.sprite.Group()
yipee = AnimationGif("Sprites/yipee/tile", 23, config.screen_width / 2, config.screen_height / 2 + 50,
                     config.screen_width / 3, config.screen_width / 3, 0.6, 0)
yipee_sprites.add(yipee)

boom_sprites = pygame.sprite.Group()


def create_explosion(pos_x, pos_y):
    global boom_sprites, aux
    boom = AnimationGif("Sprites/Boom/tile", 16, pos_x, pos_y,
                        80, 80, 0.6, 1)
    boom_sprites.add(boom)
