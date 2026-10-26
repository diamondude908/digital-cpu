import pygame
import components.memory as memory

class Display():

    def __init__(self):
        self.scale = 20
        self.on_color = (230, 230, 230)
        self.off_color = (20, 20, 20)

        self.width = memory.display_width
        self.height = memory.display_height
        self.running = True

        self.pixels = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.pixels.append(row)

    def run_window(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width * self.scale, self.height * self.scale))
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            for y in range(self.height):
                for x in range(self.width):
                    if self.pixels[y][x]:
                        color = self.on_color
                    else:
                        color = self.off_color
                    rect = pygame.Rect(x * self.scale, y * self.scale, self.scale, self.scale)
                    pygame.draw.rect(self.window, color, rect)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def draw_pixel(self, x, y, on):
        self.pixels[x][y] = on
