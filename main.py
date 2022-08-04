import pygame as pg
from functions import Color, Default_graphs, Graph
import sys
pg.init()
W = int(1920)
H = int(1080)

sc = pg.display.set_mode((W,H))
clock = pg.time.Clock()
FPS = 120
time = 0
GP1 = Default_graphs.GP1
vert_matr = Graph.init_graph(GP1)

pg.display.update()

while True:
    sc.fill(Color.BLACK)
    time += 1
    events = pg.event.get()

    # Проверка на выход из программы
    for event in events:
        if event.type == pg.QUIT:
            sys.exit()

    Graph.plot_graph(GP1,vert_matr,sc)

    pg.display.update()
    clock.tick(FPS)

