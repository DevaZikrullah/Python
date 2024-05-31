import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Stick Man")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up stick man parameters
stick_man_x = 50
stick_man_y = HEIGHT - 100
stick_man_speed = 5

# Set up obstacle parameters
obstacle_width = 30
obstacle_height = 60
obstacle_speed = 5
obstacles = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to create a new obstacle
def create_obstacle():

    obstacle_x = range(1,800)
    obstacle_y = range(1,800) - obstacle_height
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move stick man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        stick_man_speed = 10
    else:
        stick_man_speed = 5
    if keys[pygame.K_UP] and stick_man_y > 0:
        stick_man_y -= stick_man_speed
    if keys[pygame.K_DOWN] and stick_man_y < HEIGHT - 100:
        stick_man_y += stick_man_speed

    # Move obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

    # Create new obstacles
    if random.randint(0, 100) < 5:
        create_obstacle()

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(stick_man_x, stick_man_y, 20, 50)):
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw stick man
    pygame.draw.rect(screen, WHITE, (stick_man_x, stick_man_y, 20, 50))  # Body
    pygame.draw.circle(screen, WHITE, (stick_man_x + 10, stick_man_y - 20), 10)  # Head

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
