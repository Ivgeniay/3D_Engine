import math
import pygame as pg
import numpy as np
from Entities.camera import *
from Entities.projection import *
from Entities.object import *
from Settings.colors_const import *

class Render:
    def __init__(self, width:int = 1600, height:int = 900, fps:int = 60):
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
        self.camera = Camera(self, [5, 10, -50])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('Resources/Lata de refresco (alta resolución).obj')
        self.object.scale(0.1)
        self.object.rotate_z(100)

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object(self, vertex, faces)


    def draw(self):
        self.screen.fill(LIGHT_BLUE)
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