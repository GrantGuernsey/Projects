import pygame
import random

# Constants for the visualization
WIDTH = 800
HEIGHT = 600
FPS = 144
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
            screen.fill(WHITE)
            draw_array(arr)
            pygame.display.flip()
            pygame.time.wait(1)


def insertion_sort(arr):
    """
    Perform insertion sort on the given array.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(100)


def selection_sort(arr):
    """
    Perform selection sort on the given array.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(100)

def merge_sort(arr):
    """
    Perform merge sort on the given array (iterative implementation).
    """
    n = len(arr)
    size = 1
    while size < n:
        for start in range(0, n - size, 2 * size):
            mid = start + size - 1
            end = min(start + 2 * size - 1, n - 1)
            merge(arr, start, mid, end)
            screen.fill(WHITE)
            draw_array(arr)
            pygame.display.flip()
            pygame.time.wait(100)
        size *= 2


def merge(arr, start, mid, end):
    """
    Merge the two sorted subarrays into a single sorted subarray.
    """
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
def quick_sort(arr):
    """
    Perform quicksort on the given array (iterative implementation).
    """
    stack = []
    stack.append((0, len(arr) - 1))
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot_index = partition(arr, start, end)
        stack.append((pivot_index + 1, end))
        stack.append((start, pivot_index - 1))
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(100)


def partition(arr, start, end):
    """
    Choose a pivot and rearrange the elements around it.
    """
    pivot_index = random.randint(start, end)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def heapify(arr, n, i):
    """
    Heapify the array from a given index.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(50)
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Perform heapsort on the given array.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(50)
        heapify(arr, i, 0)

def counting_sort(arr):
    max_val = max(arr)  # Find the maximum value in the array
    count = [0] * (max_val + 1)  # Create a count list with size (max_val + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1

    # Modify the input array to store the sorted values
    i = 0
    for num, freq in enumerate(count):
        while freq > 0:
            arr[i] = num
            i += 1
            freq -= 1
        screen.fill(WHITE)
        draw_array(arr)
        pygame.display.flip()
        pygame.time.wait(10)

    return arr

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

    # Track the current sorting algorithm
    current_sort = 'bubble'

    # Main loop
    while running:
        clock.tick(FPS)
        arr = generate_random_array(100)
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Perform the sorting algorithm
        if current_sort == 'bubble':
            pygame.display.set_caption("Bubble Sort")
            bubble_sort(arr)
        elif current_sort == 'insertion':
            pygame.display.set_caption("Insertion Sort")
            insertion_sort(arr)
        elif current_sort == 'selection':
            pygame.display.set_caption("Selection Sort")
            selection_sort(arr)
        elif current_sort == 'merge':
            pygame.display.set_caption("Merge Sort")
            merge_sort(arr)
        elif current_sort == 'quick':
            pygame.display.set_caption("Quick Sort")
            quick_sort(arr)
        elif current_sort == 'heap':
            pygame.display.set_caption("Heap Sort")
            heap_sort(arr)
        elif current_sort == 'counting':
            pygame.display.set_caption("Counting Sort")
            counting_sort(arr)

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the array
        draw_array(arr)

        # Flip the display
        pygame.display.flip()

        # Switch to the next sorting algorithm
        if current_sort == 'bubble':
            current_sort = 'insertion'
        elif current_sort == 'insertion':
            current_sort = 'selection'
        elif current_sort == 'selection':
            current_sort = 'merge'
        elif current_sort == 'merge':
            current_sort = 'quick'
        elif current_sort == 'quick':
            current_sort = 'heap'
        elif current_sort == 'heap':
            current_sort = 'counting'
        else:
            return

    pygame.quit()


if __name__ == '__main__':
    main()