
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)


player = pygame.Rect(375, 275, 50, 50)

enemies = []

for i in range(7):
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    enemy = pygame.Rect(x, y, 40, 40)
    enemies.append(enemy)

score = 0

def check_collision(a, b):
    distance = math.sqrt(
        (a.centerx - b.centerx) ** 2 +
        (a.centery - b.centery) ** 2
    )
    return distance < 45


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    player.x = max(0, min(player.x, 750))
    player.y = max(0, min(player.y, 550))

  
    for enemy in enemies:
        if check_collision(player, enemy):
            score += 1

            enemy.x = random.randint(0, 750)
            enemy.y = random.randint(0, 550)

    
    screen.fill((20, 20, 50))

   
    pygame.draw.rect(screen, (0, 150, 255), player)


    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

  
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
