import pygame


class MainMenu:
    def __init__(self, screen_width, screen_height, font):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font

    def display_menu(self, screen):
        screen.fill((0, 0, 0))
        title_surf = self.font.render('Space Invaders', True, 'white')
        title_rect = title_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 4))

        start_surf = self.font.render('Press SPACE to Start', True, 'white')
        start_rect = start_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        controls_surf = self.font.render('Controls: Left/Right Arrows, Space to Shoot', True, 'white')
        controls_rect = controls_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + 50))

        screen.blit(title_surf, title_rect)
        screen.blit(start_surf, start_rect)
        screen.blit(controls_surf, controls_rect)


class PauseMenu:
    def __init__(self, screen_width, screen_height, font):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = font

    def display_pause_menu(self, screen):
        screen.fill((0, 0, 0))
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        pause_surf = self.font.render('Game Paused', True, 'white')
        pause_rect = pause_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 50))

        resume_surf = self.font.render('Press P to Resume', True, 'white')
        resume_rect = resume_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2))

        main_menu_surf = self.font.render('Press M for Main Menu', True, 'white')
        main_menu_rect = main_menu_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + 50))

        screen.blit(pause_surf, pause_rect)
        screen.blit(resume_surf, resume_rect)
        screen.blit(main_menu_surf, main_menu_rect)
