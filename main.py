import pygame

pygame.init()
clock = pygame.time.Clock()


class Main:
    def __init__(self):
        self.display_x = 300
        self.display_y = 400
        self.fps = 30

        self.surface = pygame.display.set_mode((self.display_x, self.display_y))

        self.running = True

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surface.fill((255, 0 , 0))

            pygame.display.update()
            clock.tick(self.fps)
        pygame.quit()


game = Main()
game.game_loop()