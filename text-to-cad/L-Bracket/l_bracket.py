from build123d import *


def gen_step():
    with BuildPart() as p:
        with Locations((0, 0, 4)):
            Box(80, 50, 8)

        with Locations((0, 21, 33)):
            Box(80, 8, 50)

        with BuildSketch(Plane.YZ.offset(16)) as s:
            Polygon((17, 8), (17, 38), (-13, 8))
        extrude(amount=8)

        with BuildSketch(Plane.YZ.offset(-24)) as s:
            Polygon((17, 8), (17, 38), (-13, 8))
        extrude(amount=8)

        for x in (-25, 25):
            with Locations((x, -10, 4)):
                Cylinder(radius=3, height=10, mode=Mode.SUBTRACT)

        for x in (-25, 25):
            with Locations((x, 21, 30)):
                Cylinder(radius=3, height=10, rotation=(90, 0, 0), mode=Mode.SUBTRACT)

        outside_corner = [
            e for e in p.part.edges()
            if abs(e.center().Y - 25) < 0.5
            and abs(e.center().Z) < 0.5
        ]
        if outside_corner:
            fillet(outside_corner, 2)

    return p.part
