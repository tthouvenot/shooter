import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 0
        self.shield = 0
        self.velocity = 5
        self.image = pygame.image.load('./assets/player/ship/S_PlayerShip_A1.png')
        self.image =pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.position_x = float(self.rect.x)
        self.position_y = float(self.rect.y)

    def move_right(self):
        self.position_x += self.velocity
        self.rect.x = self.position_x
    def move_left(self):
        self.position_x -= self.velocity
        self.rect.x = self.position_x
    def move_down(self):
        self.position_y += self.velocity
        self.rect.y = self.position_y
    def move_up(self):
        self.position_y -= self.velocity
        self.rect.y = self.position_y
