from build123d import *

flange_od = 80.0
flange_r = flange_od / 2
flange_h = 10.0
bore_d = 30.0
bore_r = bore_d / 2
bolt_d = 6.0
bolt_r = bolt_d / 2
bcd = 60.0
bcd_r = bcd / 2
n_bolts = 6
fillet_r = 1.5


def gen_step():
    with BuildPart() as p:
        with BuildSketch(Plane.XY) as sk:
            Circle(flange_r)
        extrude(amount=flange_h)

        with BuildSketch(Plane.XY.offset(-1)) as sk:
            Circle(bore_r)
        extrude(amount=flange_h + 2, mode=Mode.SUBTRACT)

        with BuildSketch(Plane.XY.offset(-1)) as sk:
            with PolarLocations(bcd_r, n_bolts):
                Circle(bolt_r)
        extrude(amount=flange_h + 2, mode=Mode.SUBTRACT)

        top_face = p.part.faces().sort_by(Axis.Z)[-1]
        bottom_face = p.part.faces().sort_by(Axis.Z)[0]

        top_outer = max(
            (e for e in top_face.edges() if e.geom_type == GeomType.CIRCLE),
            key=lambda e: e.radius,
        )
        bottom_outer = max(
            (e for e in bottom_face.edges() if e.geom_type == GeomType.CIRCLE),
            key=lambda e: e.radius,
        )

        fillet([top_outer, bottom_outer], fillet_r)

    return p.part
