import matplotlib.pyplot as plt
import random as rnd
import matplotlib.patches as patches
import numpy as np
import math


class Opheim():
    def point_line_distance(self, x0, y0, x1, y1, x2, y2):
        return abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / math.sqrt(
            (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def point_point_distance(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        return math.sqrt(dx * dx + dy * dy)

    def simplify_opheim(self, tolerance, maxdist, p, step=-1):
        mask = np.ones(len(p), dtype='bool')
        marker = np.array([], dtype='double')
        first = 0
        second = 1
        third = 2

        marker = np.array([p[first], p[second]], dtype='double')

        for i in range(0, min(step, len(p) - 2)):
            ldist = self.point_line_distance(p[third, 0], p[third, 1], p[first, 0], p[first, 1], p[second, 0],
                                             p[second, 1])
            pdist = self.point_point_distance(p[third, 0], p[third, 1], p[first, 0], p[first, 1])
            if ldist <= tolerance and pdist < maxdist:
                mask[second] = False
                second = third
                third = third + 1
            else:
                first = second
                second = third
                third = third + 1
        marker = np.array([p[first], p[second]], dtype='double')
        return mask, marker
