import pygame
import sys
import random


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing ball")

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [BLACK, WHITE, RED, BLUE]

# ball_1 settings
ball_1_radius = 20
ball_1_x = width // 2
ball_1_y = height // 2
ball_1_speed_x = 5
ball_1_speed_y = 5

# ball_2 settings
ball_2_radius = 5
ball_2_x = width // 2
ball_2_y = height // 2
ball_2_speed_x = 2
ball_2_speed_y = 2

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    color_index = random.randint(0, 3)

    # Move the ball_1
    ball_1_x += ball_1_speed_x
    ball_1_y += ball_1_speed_y

    # Move the ball_2
    ball_2_x += ball_2_speed_x
    ball_2_y += ball_2_speed_y

    # Bounce off the walls
    if ball_1_x - ball_1_radius < 0 or ball_1_x + ball_1_radius > width:
        ball_1_speed_x = -ball_1_speed_x
    if ball_1_y - ball_1_radius < 0 or ball_1_y + ball_1_radius > height:
        ball_1_speed_y = -ball_1_speed_y

    if ball_2_x - ball_2_radius < 0 or ball_2_x + ball_2_radius > width:
        ball_2_speed_x = -ball_2_speed_x
    if ball_2_y - ball_2_radius < 0 or ball_2_y + ball_2_radius > height:
        ball_2_speed_y = -ball_2_speed_y

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the ball_1
    color = colors[color_index]
    pygame.draw.circle(screen, color, (ball_1_x, ball_1_y), ball_1_radius)

    # Draw the ball_2
    pygame.draw.circle(screen, RED, (ball_2_x, ball_2_y), ball_2_radius)

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)
