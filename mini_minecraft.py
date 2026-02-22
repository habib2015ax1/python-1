import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
BLOCK_SIZE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Minecraft V2")

clock = pygame.time.Clock()

# Colors
SKY = (135, 206, 235)
GRASS = (34, 177, 76)
DIRT = (139, 69, 19)
PLAYER_COLOR = (255, 0, 0)

# World grid
cols = WIDTH // BLOCK_SIZE
rows = HEIGHT // BLOCK_SIZE
world = [[0 for _ in range(cols)] for _ in range(rows)]

# Generate terrain
for col in range(cols):
    ground_height = rows // 2
    for row in range(ground_height, rows):
        world[row][col] = 1

# Player
player = pygame.Rect(200, 200, 30, 40)
velocity_y = 0
gravity = 0.5
jump_power = -10
player_speed = 5
on_ground = False

def draw_world():
    for row in range(rows):
        for col in range(cols):
            if world[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    GRASS,
                    (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )

def check_collision(rect):
    for row in range(rows):
        for col in range(cols):
            if world[row][col] == 1:
                block_rect = pygame.Rect(
                    col * BLOCK_SIZE,
                    row * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                )
                if rect.colliderect(block_rect):
                    return block_rect
    return None

running = True
while running:
    clock.tick(60)
    screen.fill(SKY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            grid_x = mx // BLOCK_SIZE
            grid_y = my // BLOCK_SIZE

            if event.button == 1:
                world[grid_y][grid_x] = 0
            if event.button == 3:
                world[grid_y][grid_x] = 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed

    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power

    # Apply gravity
    velocity_y += gravity
    player.y += velocity_y
    on_ground = False

    collision = check_collision(player)
    if collision:
        if velocity_y > 0:
            player.bottom = collision.top
            velocity_y = 0
            on_ground = True
        elif velocity_y < 0:
            player.top = collision.bottom
            velocity_y = 0

    draw_world()
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    pygame.display.flip()

pygame.quit()
sys.exit()