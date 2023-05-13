import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moja Zaawansowana Gra")

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
    
    def update(self):
        # Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        
        # Sprawdzanie kolizji z przeszkodami
        if pygame.sprite.spritecollide(self, obstacles, False):
            # Kod obsługujący kolizję
            pass

# Klasa przeszkód
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.rect.y += 3
        if self.rect.top > screen_height:
            self.kill()

# Grupa przeszkód
obstacles = pygame.sprite.Group()

# Tworzenie przeszkód
def create_obstacles():
    x = random.randrange(0, screen_width)
    y = random.randrange(-screen_height, -50)
    obstacle = Obstacle(x, y)
    obstacles.add(obstacle)

# Tworzenie obiektów
player = Player()

# Główna pętla gry
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Aktualizacja obiektów
    player.update()
    obstacles.update()

    # Tworzenie przeszkód
    if len(obstacles) < 10:
        create_obstacles()

    # Rysowanie obiektów na ekranie
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    obstacles.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Zamknięcie Pygame
pygame.quit()
