'''
Develop an RPG game 
with pygame
'''

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RPG Game')

# Player
player_img = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_img = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3

# Bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

# Score
score = 0

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def player(x, y):
    window.blit(player_img, (x, y))

def enemy(x, y):
    window.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX)**2 + (enemyY - bulletY)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

def show_score(score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 10))

def game_over_text():
    text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    window.blit(text, (200, 250))

# Main loop
running = True
while running:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    if playerX > 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 0.3
        enemyY += 40
    if enemyX > 736:
        enemyX_change = -0.3
        enemyY += 40

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(score)
    if enemyY > 440:
        game_over_text()
        break
    pygame.display.update()

pygame.quit()
quit()