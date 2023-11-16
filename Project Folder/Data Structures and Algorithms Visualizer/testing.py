import pygame
import random

# Constants for the visualization
WIDTH = 800
HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Data Structures and Algorithms Visualizer")
clock = pygame.time.Clock()


def draw_array(arr):
    """
    Draw an array as vertical bars on the screen.
    """
    bar_width = WIDTH // len(arr)
    for i, value in enumerate(arr):
        bar_height = value * HEIGHT // max(arr)
        pygame.draw.rect(screen, BLUE, (i * bar_width, HEIGHT - bar_height, bar_width, bar_height))


def bubble_sort(arr):
    """
    Perform bubble sort on the given array.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Visualization
                screen.fill(WHITE)
                draw_array(arr)
                pygame.display.flip()
                pygame.time.wait(100)


def generate_random_array(size):
    """
    Generate a random array of the given size.
    """
    arr = []
    for _ in range(size):
        arr.append(random.randint(10, 500))
    return arr


def main():
    running = True

    # Generate a random array
    arr = generate_random_array(50)

    # Main loop
    while running:
        clock.tick(FPS)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bubble sort the array
        bubble_sort(arr)

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the array
        draw_array(arr)

        # Flip the display
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()