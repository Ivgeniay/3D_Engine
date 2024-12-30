import math
import pygame as pg
import numpy as np
from Entities.camera import *
from Entities.projection import *
from Entities.object import *

class Render:
    def __init__(self, width:int = 1600, height:int = 900, fps:int = 60):
        self.axes = None
        self.world_axes = None
        self.object = None
        self.camera = None
        self.projection = None
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = width, height
        self.H_WIDTH, self.H_HEIGHT= self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = fps
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_object()

    def create_object(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object(self)
        self.object.translate([0.2, 0.4, 0.2])
        #self.object.rotate_y(math.pi / 6)
        self.axes = Axes(self)
        self.axes.translate([0.7, 0.9, 0.7])
        self.world_axes = Axes(self)
        self.world_axes.movement_flag = False
        self.world_axes.scale(2.5)
        self.world_axes.translate([0.0001, 0.0001, 0.0001])


    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.world_axes.draw()
        self.axes.draw()
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption("3D Renderer: " + str(int(self.clock.get_fps())) + " fps")
            pg.display.flip()
            if self.FPS <= 0: self.clock.tick()
            else: self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Render(800, 600, 0)
    app.run()