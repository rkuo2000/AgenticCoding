# [Text-to-CAD (文生機構)](https://github.com/earthtojake/text-to-cad)
`Skills`<br>

## CAD Skills
Install the library to give agents focused workflows for CAD, fabrication, robot description files, simulation, and local review. <br>

| Skill        | Summary                                                                                                                                            | Source                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| CAD          | Creates and edits CAD models from plain-language or image requests, with STEP as the main output along with options to export to STL, 3MF and GLB. | [skills/cad](skills/cad/SKILL.md)                   |
| CAD Viewer   | Shows local browser previews for CAD, G-code, and robot files.                                                                                     | [skills/cad-viewer](skills/cad-viewer/SKILL.md)     |
| step.parts   | Finds off-the-shelf STEP parts like screws, bearings, motors, and connectors.                                                                      | [skills/step-parts](skills/step-parts/SKILL.md)     |
| DXF          | Creates 2D DXF drawings like profiles, templates, gaskets, and cut layouts from Python sources or CAD geometry.                                    | [skills/dxf](skills/dxf/SKILL.md)                   |
| URDF         | Writes robot structure files with links, joints, limits, inertials, and meshes.                                                                    | [skills/urdf](skills/urdf/SKILL.md)                 |
| SRDF         | Adds MoveIt planning groups, end effectors, poses, and collision rules to a URDF.                                                                  | [skills/srdf](skills/srdf/SKILL.md)                 |
| SDF          | Creates simulator models and worlds with frames, physics, sensors, and lights.                                                                     | [skills/sdf](skills/sdf/SKILL.md)                   |
| SendCutSend  | Checks DXF and STEP files before upload to SendCutSend.                                                                                            | [skills/sendcutsend](skills/sendcutsend/SKILL.md)   |
| G-code       | Slices supported mesh files into validated, printer-profiled FDM `.gcode` with real slicer CLIs.                                                   | [skills/gcode](skills/gcode/SKILL.md)               |
| Bambu Labs   | Dry-runs, uploads, and cautiously starts local Bambu Lab print jobs from validated `.gcode`.                                                       | [skills/bambu-labs](skills/bambu-labs/SKILL.md)     |
| Implicit CAD | Creates browser-native implicit CAD models using GLSL signed-distance fields and CAD Viewer raymarch rendering. Experimental.                      | [skills/implicit-cad](skills/implicit-cad/SKILL.md) |

---
### install CAD skills
```
npx skills install earthtojake/text-to-cad
```

---
### Plugins
`opencode` <br>
```
plugin install marketplace add earthtojake/text-to-cad
plugin add cad@text-to-cad
```

---
## [Benchmarks](https://github.com/earthtojake/text-to-cad/tree/main#-benchmarks)

### 2. Circular Flange With Bolt-Hole Pattern
#### Prompt
```
Create a single solid circular flange as a STEP model in millimeters. The flange is a cylinder with an outside diameter of 80 mm and a thickness of 10 mm. Its axis is vertical along Z, with the bottom face at Z = 0 and the center at X = 0, Y = 0.
Add a central vertical through-bore with diameter 30 mm.
Add six equally spaced vertical through-holes, each 6 mm in diameter, on a 60 mm bolt-circle diameter.
Add a 1.5 mm fillet to the top and bottom outside circular edges.
Export as a STEP file.
```
<img width="240" src="https://github.com/earthtojake/text-to-cad/raw/main/benchmarks/benchmark_02_circular_flange.gif">

---
### 3. L-Bracket With Gussets and Two Hole Directions
#### Prompt
```
Create a single solid L-bracket STEP model in millimeters.
The bracket has a horizontal base plate 80 mm long in X, 50 mm wide in Y, and 8 mm thick in Z. Center the base plate on the XY origin, with its bottom at Z = 0.
Add a vertical back plate along the rear long edge of the base. The back plate is 80 mm long in X, 8 mm thick in Y, and 50 mm tall in Z, rising from the top of the base plate. The back plate should sit along the rear edge at positive Y.
Add two vertical through-holes in the base plate, each 6 mm in diameter, located at X = +/-25 mm and Y = -10 mm.
Add two horizontal through-holes in the vertical plate, each 6 mm in diameter, located at X = +/-25 mm and Z = 30 mm, passing through the 8 mm thickness of the vertical plate.
Add two triangular gussets, each 8 mm thick in X, located at X = +/-20 mm. Each gusset should connect the base plate to the back plate with a right-triangle side profile 30 mm tall and 30 mm deep.
Add 2 mm fillets to the outside corner where the base and back plate meet.
Export as a STEP file.
```
<img width="240" src="https://github.com/earthtojake/text-to-cad/raw/main/benchmarks/benchmark_03_l_bracket.gif">

---
### 5. Open-Top Electronics Enclosure With Bosses
#### Prompt
```
Create a single solid open-top electronics enclosure base as a STEP model in millimeters.
The outer shape is a rectangular box 100 mm long in X, 70 mm wide in Y, and 30 mm tall in Z. Center it on the XY origin, with the bottom face at Z = 0.
The enclosure is open at the top. The wall thickness is 3 mm and the bottom floor thickness is 3 mm.
Add four internal cylindrical standoffs rising from the inside floor. Each standoff has an outside diameter of 10 mm and a height of 12 mm above the inside floor. Place the standoffs at X = +/-35 mm and Y = +/-25 mm.
Add a centered blind hole in each standoff, 3 mm in diameter and 8 mm deep from the top of the standoff.
Add 2 mm radius fillets to the four outside vertical corners of the enclosure.
Export as a STEP file.
```
<img width="240" src="https://github.com/earthtojake/text-to-cad/raw/main/benchmarks/benchmark_05_open_top_electronics_enclosure.gif">


