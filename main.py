import pygame
import pygame_gui
from game import game_main


def main():
    FPS = 60
    WINDOW_SIZE = (400, 200)
    pygame.init()

    pygame.display.set_caption("Меню")
    window_surface = pygame.display.set_mode(WINDOW_SIZE)

    background = pygame.Surface(WINDOW_SIZE)
    background.fill((0, 0, 0))

    manager = pygame_gui.UIManager(WINDOW_SIZE)

    play = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 3), (100, 50)),
        text="Играть",
        manager=manager
    )

    quit = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 75), (100, 50)),
        text="Выйти",
        manager=manager
    )

    clock = pygame.time.Clock()
    run = True

    while run:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play:
                        game_main()
                        run = False
                        main()
                    elif event.ui_element == quit:
                        run = False

            manager.process_events(event)

        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == "__main__":
    main()
