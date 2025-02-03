import pygame
import pygame_gui
from player import Hero
from level import Map
from functions import show_message, show_live
from settings import TILE_SIZE
life = 10


class Game:
    def __init__(self, map, hero):
        self.map = map
        self.hero = hero
        self.y_moment = 0
        self.hero_movement = [0, 0]

    def render(self, screen):
        self.map.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        global life
        from functions import prev_pos

        next_x, next_y = self.hero.get_position()

        self.y_moment += 0.02

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 0.2

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 0.2

        if not self.map.is_free((next_x, int(next_y) + 1)):
            if self.map.is_free((next_x, int(next_y))):
                prev_pos[0] = next_x
                prev_pos[1] = next_y
            self.y_moment = 0

        if pygame.key.get_pressed()[pygame.K_UP] and self.y_moment == 0:
            self.y_moment = -0.4

        next_y += self.y_moment

        if self.map.is_free((next_x, next_y)) != 2:
            if self.map.is_free((next_x, next_y)):
                self.hero.set_position((next_x, next_y))
        else:
            self.hero.set_position(prev_pos)
            life -= 1

    def check_win(self):
        coords = (self.hero.get_position()[0], (self.hero.get_position()[1] + 1))

        if self.map.is_free(coords) != 2:
            return self.map.get_tile_id(coords) == self.map.finish_tile

    def check_loose(self):
        return life == 0


def game_main():
    global life
    from functions import scroll

    WINDOW_SIZE = 800, 600
    FPS = 60

    manager = pygame_gui.UIManager(WINDOW_SIZE)

    quit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 10), (100, 40)),
        text="Выйти",
        manager=manager
    )
             
    
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Pixel Adventures")

    map = Map("untitled.tmx", [47], 407)
    hero = Hero((20, 46))
    game = Game(map, hero)

    clock = pygame.time.Clock()
    running = True
    stop_game = False

    while running:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scroll[0] = 0
                scroll[1] = 0
                life = 10
                return
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == quit:
                        scroll[0] = 0
                        scroll[1] = 0
                        life = 10
                        return
            if event.type == pygame.MOUSEBUTTONDOWN:
                stop_game = not stop_game

            manager.process_events(event)

        if not stop_game:
            scroll[0] += (hero.get_position()[0] * TILE_SIZE - scroll[0] - 400) / 10
            scroll[1] += (hero.get_position()[1] * TILE_SIZE - scroll[1] - 300) / 10

            game.update_hero()

            screen.fill((0, 0, 0))
            game.render(screen)

            if game.check_loose():
                stop_game = True
                show_message(screen, "You dead!", WINDOW_SIZE)

            if game.check_win():
                stop_game = True
                show_message(screen, "You won!", WINDOW_SIZE)

        manager.update(time_delta)
        manager.draw_ui(screen)
        show_live(screen, f"Количество жизни: {life}", (10, 70))

        pygame.display.flip()
        clock.tick(FPS)
