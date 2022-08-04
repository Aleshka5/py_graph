import pygame as pg
import numpy as np
class Color():
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (255,255,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    GREEN = (0,255,0)

class Default_graphs():
    GP1 = [[1,2],[1,3],[1,4],[2,4],[2,3],[3,4]]

class Graph():
    def init_graph(graph):
        set_of_vertexes = set([graph[i][j] for i in range(len(graph)) for j in range(2)])
        #print(set_of_vertexes)
        vertex_coordinate = []
        for i in set_of_vertexes:
            random_x = np.random.randint(300,1620)
            random_y = np.random.randint(100,980)
            #print(random_x, random_y)
            vertex_coordinate.append([i,random_x,random_y])
            print(vertex_coordinate)
        return vertex_coordinate

    def update(vertex_coordinate,delta_matrix):
        for i in range(len(vertex_coordinate)):
            pass

    def plot_graph(graph,vertex_coordinate,sc,radius = 5):
        def peresechenie(x1, y1, x2, y2, x3, y3, x4, y4):
            n = 0
            if y2 - y1 != 0:
                q = (x2 - x1) / (y1 - y2)
                sn = (x3 - x4) + (y3 - y4) * q
                if not sn:
                    return None
                fn = (x3 - x1) + (y3 - y1) * q
                n = fn / sn
            else:
                if not (y3 - y4):
                    return None
                n = (y3 - y1) / (y3 - y4)
            dot = [x3 + (x4 - x3) * n, y3 + (y4 - y3) * n]
            return dot

        def check (x1, y1, x2, y2, x3, y3, x4, y4):

            if dot[1] > max(y1,y2):
                return False
            if dot[1] > max(y3,y4):
                return False
            if dot[0] > max(x1,x2):
                return False
            if dot[0] > max(x3,x4):
                return False

            if dot[1] < min(y1,y2):
                return False
            if dot[1] < min(y3,y4):
                return False
            if dot[0] < min(x1,x2):
                return False
            if dot[0] < min(x3,x4):
                return False
            return True

        for i in range(len(vertex_coordinate)):
            pg.draw.circle(sc, Color.YELLOW, (vertex_coordinate[i][1],vertex_coordinate[i][2]), radius)

        for i in graph:
            pg.draw.line(sc,Color.WHITE,vertex_coordinate[i[0]-1][1:],vertex_coordinate[i[1]-1][1:])

        for i in range(len(graph)-1):
            for j in range(i+1,len(graph)):
                if graph[i][0] != graph[j][0]:
                    if graph[i][0] != graph[j][1]:
                        if graph[i][1] != graph[j][0]:
                            if graph[i][1] != graph[j][1]:
                                dot = peresechenie(*vertex_coordinate[graph[i][0]-1][1:],*vertex_coordinate[graph[i][1]-1][1:],*vertex_coordinate[graph[j][0]-1][1:],*vertex_coordinate[graph[j][1]-1][1:])
                                if dot:
                                    is_red = check(*vertex_coordinate[graph[i][0] - 1][1:],*vertex_coordinate[graph[i][1] - 1][1:],*vertex_coordinate[graph[j][0] - 1][1:],*vertex_coordinate[graph[j][1] - 1][1:])
                                    if is_red:
                                        pg.draw.circle(sc, Color.RED, (dot[0], dot[1]),radius)
                                    else:
                                        pg.draw.circle(sc, Color.BLUE, (dot[0], dot[1]), radius)
