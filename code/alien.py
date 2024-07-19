import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = '../graphics/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        if color == 'red':
            self.value = 100
        elif color == 'green':
            self.value = 200
        else:
            self.value = 300

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        self.image = pygame.image.load('../graphics/extra.png').convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 80))

    def update(self):
        self.rect.x += self.speed


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        original_image = pygame.image.load('../graphics/Explosion.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, (50, 50))  # Scale the image to desired size
        self.rect = self.image.get_rect(center=pos)
        self.frame_rate = 5
        self.counter = 0
        self.lifetime = 25  # Display the explosion for a short period

    def update(self):
        self.counter += 1
        if self.counter >= self.lifetime:
            self.kill()  # Remove the sprite after the lifetime
