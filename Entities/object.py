import numpy as np
import pygame as pg
from Math.matrix_functions import *
from main import Render

cubeVertexs = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1),(1, 0, 0, 1),
                        (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1), (1, 0, 1, 1)])
cubeFaces = np.array([(0, 1, 2, 3), (4, 5, 6, 7),
                      (0, 4, 5, 1), (2, 3, 7, 6),
                      (1, 2, 6, 5), (0, 3, 7, 4)])

class Object:

    def __init__(self, renderer:Render):
        self.renderer = renderer
        self.vertexes = cubeVertexs
        self.faces = cubeFaces

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = True, True
        self.label = ''

    def draw(self):
        self.screen_projection()
        self.movement()

    #sample
    def movement(self):
        if self.movement_flag:
            self.rotate_y(pg.time.get_ticks() % 0.0005)

    def screen_projection(self):
        vertexes = self.vertexes @ self.renderer.camera.camera_matrix()
        vertexes = vertexes @ self.renderer.projection.projection_matrix
        #normalize
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.renderer.projection.to_screen_matrix
        vertexes = vertexes[:, :2] #[x,y,z,w] -> [x,y]

        # for face in self.faces:
        #     polygon = vertexes[face]
        #     if not np.any((polygon == self.renderer.H_WIDTH) | (polygon == self.renderer.H_HEIGHT)):
        #         pg.draw.polygon(self.renderer.screen, pg.Color('orange'), polygon, 3)

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]
            if not np.any((polygon == self.renderer.H_WIDTH) | (polygon == self.renderer.H_HEIGHT)):
                pg.draw.polygon(self.renderer.screen, color, polygon, 3)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.renderer.screen.blit(text, polygon[-1])

        if self.draw_vertexes:
            for vertex in vertexes:
                if not np.any((vertex == self.renderer.H_WIDTH) | (vertex == self.renderer.H_HEIGHT)):
                    pg.draw.circle(self.renderer.screen, pg.Color('white'), vertex, 6)

    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ rotate_z(angle)

class Axes(Object):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.vertexes = np.array([(0,0,0,1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'