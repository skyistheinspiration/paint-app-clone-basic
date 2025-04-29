import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App with Colors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ERASE_COLOR = WHITE
colors = [BLACK, RED, GREEN, BLUE, YELLOW]
button_rects = []

radius = 5
drawing = False
current_color = BLACK
erase_mode = False
erase_radius = 10

screen.fill(WHITE)

def draw_buttons():
    button_width, button_height = 50, 50
    button_x = 10
    button_y = HEIGHT - button_height - 10
    button_spacing = 60

    for i, color in enumerate(colors):
        button_rect = pygame.Rect(button_x + i * button_spacing, button_y, button_width, button_height)
        pygame.draw.rect(screen, color, button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
        button_rects.append(button_rect)

    erase_button_rect = pygame.Rect(button_x + len(colors) * button_spacing, button_y, button_width, button_height)
    pygame.draw.rect(screen, (200, 200, 200), erase_button_rect)
    pygame.draw.rect(screen, (0, 0, 0), erase_button_rect, 3)
    button_rects.append(erase_button_rect)
    font = pygame.font.Font(None, 30)
    erase_text = font.render("Erase", True, (0, 0, 0))
    screen.blit(erase_text, (erase_button_rect.x + 5, erase_button_rect.y + 5))

    clear_button_rect = pygame.Rect(button_x + (len(colors) + 1) * button_spacing, button_y, button_width, button_height)
    pygame.draw.rect(screen, (255, 100, 100), clear_button_rect)
    pygame.draw.rect(screen, (0, 0, 0), clear_button_rect, 3)
    button_rects.append(clear_button_rect)
    clear_text = font.render("Clear", True, (0, 0, 0))
    screen.blit(clear_text, (clear_button_rect.x + 5, clear_button_rect.y + 5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i, button_rect in enumerate(button_rects):
                if button_rect.collidepoint(mouse_pos):
                    if i < len(colors):
                        current_color = colors[i]
                        erase_mode = False
                    elif i == len(colors):
                        erase_mode = not erase_mode
                        current_color = ERASE_COLOR if erase_mode else BLACK
                    elif i == len(colors) + 1:
                        screen.fill(WHITE)
                    break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill(WHITE)
            if event.key == pygame.K_EQUALS and erase_mode:  # Increase erase size
                erase_radius += 5
            if event.key == pygame.K_MINUS and erase_mode:  # Decrease erase size
                erase_radius = max(5, erase_radius - 5)

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if erase_mode:
            pygame.draw.circle(screen, ERASE_COLOR, mouse_pos, erase_radius)
        else:
            pygame.draw.circle(screen, current_color, mouse_pos, radius)

    button_rects.clear()
    draw_buttons()

    pygame.display.flip()
