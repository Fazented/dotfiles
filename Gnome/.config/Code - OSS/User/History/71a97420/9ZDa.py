import numpy as np
import pygame
from pygame.locals import *

class Trig:
    def __init__(self, width=1600, height=900, gap=100, fps=60, radius=100):
        self.width = width
        self.height = height
        self.fps = fps
        self.gap = gap
        self.radius = radius
        self.t = 0
        self.Ys = []  # Initialize Ys list
        
        self.setup()
        self.loop_running()

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop_running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

    def draw_circle(self, x, y):
        pygame.draw.circle(self.screen, 'blue', (x, y), self.radius, 5)

    def draw_line(self, start, end, color='grey', thickness=3):
        pygame.draw.line(self.screen, color, start, end, thickness)

    def loop_running(self):
        self.loop_running = True
        while self.loop_running:
            self.clock.tick(self.fps)
            self.handle_events()
            self.screen.fill('white')

            center_x, center_y = self.width // 2, self.height // 2
            x = center_x + (self.radius * np.cos(self.t))
            y = center_y + (self.radius * np.sin(self.t))

            # Calculate the x-coordinate of the end point of the green line based on the current angle
            end_x = center_x + (self.radius * np.cos(self.t + np.pi))  # Shift the angle by pi radians

            self.draw_line((center_x, center_y), (end_x, center_y), 'green')  # Adjusted line
            self.draw_line((center_x, center_y), (center_x + 1000, center_y))
            self.draw_line((center_x, center_y + self.radius), (center_x + 1000, center_y + self.radius))
            self.draw_line((center_x, center_y - self.radius), (center_x + 1000, center_y - self.radius))
            self.draw_circle(center_x, center_y)
            self.draw_line((center_x, center_y), (x, y), 'green')
            
            self.Ys.insert(0, y)
            if len(self.Ys) > 1100 - self.gap:
                self.Ys.pop()

            for i, y_value in enumerate(self.Ys):
                self.screen.set_at((i + center_x + self.gap, int(y_value)), pygame.Color('red'))

            pygame.display.update()

            self.t += 0.05

if __name__ == '__main__':
    sin = Trig()
    pygame.quit()