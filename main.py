import pygame as pg
import numpy as np

class Render:
    def __init__(self, width:int = 1600, height:int = 900, fps:int = 60):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = width, height
        self.H_WIDTH, self.H_HEIGHT= self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = fps
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption("3D Renderer: " + str(int(self.clock.get_fps())) + " fps")
            pg.display.flip()
            if self.FPS <= 0: self.clock.tick()
            else: self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Render(800, 600, 0)
    app.run()