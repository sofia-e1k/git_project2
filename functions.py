import pygame
import os

scroll = [0, 0]
prev_pos = [0, 0]


def load_image(name):
    pygame.init()
    pygame.display.set_mode((1, 1))
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def show_message(screen, message, window_size):
    font = pygame.font.Font(None, 50)
    text = font.render(message, True, (50, 70, 0))
    text_x = window_size[0] // 2 - text.get_width() // 2
    text_y = window_size[1] // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(screen, (200, 150, 50), (text_x - 10, text_y - 10, text_w + 20, text_h + 20))
    screen.blit(text, (text_x, text_y))


def show_live(screen, message, coord):
    font = pygame.font.Font(None, 25)
    text = font.render(message, True, (255, 255, 255))
    text_x = coord[0]
    text_y = coord[1]
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
