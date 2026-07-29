from build123d import *


def gen_step():
    outer_length = 100.0
    outer_width = 70.0
    outer_height = 30.0
    wall_t = 3.0
    floor_t = 3.0
    standoff_od = 10.0
    standoff_h = 12.0
    hole_d = 3.0
    hole_depth = 8.0
    so_x = 35.0
    so_y = 25.0
    fillet_r = 2.0

    with BuildPart() as p:
        with Locations((0, 0, outer_height / 2)):
            Box(outer_length, outer_width, outer_height)

        corner_edges = [
            e for e in p.edges().filter_by(Axis.Z)
            if abs(abs(e.center().X) - outer_length / 2) < 1
            and abs(abs(e.center().Y) - outer_width / 2) < 1
        ]
        fillet(corner_edges, fillet_r)

        inner_length = outer_length - 2 * wall_t
        inner_width = outer_width - 2 * wall_t
        inner_height = outer_height - floor_t
        with Locations((0, 0, floor_t + inner_height / 2)):
            Box(inner_length, inner_width, inner_height, mode=Mode.SUBTRACT)

        for sx in (-so_x, so_x):
            for sy in (-so_y, so_y):
                with Locations((sx, sy, floor_t + standoff_h / 2)):
                    Cylinder(radius=standoff_od / 2, height=standoff_h)

        for sx in (-so_x, so_x):
            for sy in (-so_y, so_y):
                with Locations((sx, sy, floor_t + standoff_h - hole_depth / 2)):
                    Cylinder(radius=hole_d / 2, height=hole_depth, mode=Mode.SUBTRACT)

    return p.part
