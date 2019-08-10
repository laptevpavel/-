import numpy as np
import random as rnd

class Line():
    def __init__(self):
        self.line = []
    def get_line(self):
        return self.line
    def set_line(self, line):
        self.line = line
    def generate_random_line(self,num_points, dir, limits=[5,10]):
        line = []
        for i in range(num_points):
            point = [rnd.randrange(limits[0],limits[1]), rnd.randrange(limits[0],limits[1])]
            if point not in line:
                line.append(point)
                limits = [limits[0]+dir,limits[1]+dir]
        self.line = np.array(line,dtype='double')
        return np.array(line,dtype='double')
