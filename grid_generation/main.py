from KicadModTree import *
import math
import os

ROW = 9 # y-axis
COL = 16 # x-axis

GRID_SIZE = 5
GAP = 0.2
NECK = 0.25
PITCH = GRID_SIZE + math.sqrt(2) * GAP

pythagorean = lambda x: math.sqrt( 2 * (x ** 2))

WIDTH = COL * PITCH
HEIGHT = ROW * PITCH

VIA_OUTER = 0.79
VIA_DRILL = 0.38

def TxPad(col, x, y):
    length = pythagorean(GRID_SIZE/2)/2
    shape = Polygon(nodes = [[-length,-length],[length,-length],[length,length],[-length,length]])
    shape.rotate(45)
    pad = Pad(
        number="Tx"+str(col),
        type=Pad.TYPE_SMT,
        shape=Pad.SHAPE_CUSTOM,
        at = [x, y],
        size=[1, 1],
        layers = ['F.Cu'],
        anchor_shape = Pad.ANCHOR_RECT,
        shape_in_zone = Pad.SHAPE_IN_ZONE_OUTLINE,
        primitives = [shape],
    )
    return pad

def RxPad(row, x, y):
    original = pythagorean(GRID_SIZE/2)/2
    border = (PITCH - 2 * GAP - NECK)
    length = pythagorean(border/2)
    side = pythagorean((original - length)/2)
    shape = Polygon(nodes = [[-original,-original],[-original+length,-original],[original,original-length],[original,original],[original-length,original],[-original,-original+length]])
    shape.rotate(45)
    pad = Pad(
        number="Rx"+str(row),
        type=Pad.TYPE_SMT,
        shape=Pad.SHAPE_CUSTOM,
        at = [x, y],
        size=[1, 1],
        layers = ['F.Cu'],
        anchor_shape = Pad.ANCHOR_RECT,
        shape_in_zone = Pad.SHAPE_IN_ZONE_OUTLINE,
        primitives = [shape],
    )
    return pad

def via(x,y,name):
    return Pad(
        number=name,
        type=Pad.TYPE_THT,
        shape=Pad.SHAPE_CIRCLE,
        at = [x, y],
        size=VIA_OUTER,
        drill=VIA_DRILL,
        layers = ["*.Cu"],
        anchor_shape = Pad.ANCHOR_CIRCLE,
        shape_in_zone = Pad.SHAPE_IN_ZONE_OUTLINE,
    )

def main():
    kicad_mod = Footprint("grid")
    for i in range(COL):
        for j in range(ROW+1):
            x = (i+0.5)*PITCH
            y = (j)*PITCH
            node = TxPad(i+1, x, y)
            kicad_mod.append(node)
            node = via(x, y, "Tx"+str(i+1))
            kicad_mod.append(node)

    for i in range(COL+1):
        for j in range(ROW):
            x = (i)*PITCH
            y = (j+0.5)*PITCH
            node = RxPad(j+1, x, y)
            kicad_mod.append(node)
            node = via(x, y, "Rx"+str(j+1))
            kicad_mod.append(node)

    kicad_mod.append(RectLine(start=[0, 0],end = [WIDTH, HEIGHT], layer='F.SilkS'))
    file_handler = KicadFileHandler(kicad_mod)
    isExist = os.path.exists("output")
    if not isExist:
        os.makedirs("output")
    file_handler.writeFile('output/grid.kicad_mod')

if __name__ == '__main__':
    main()

