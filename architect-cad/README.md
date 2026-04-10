## Architect CAD (建築設計）
`FreeCAD`<br>

[FreeCAD 下載](https://www.freecad.org/downloads.php)<br>
[FreeCAD MCP](https://github.com/neka-nat/freecad-mcp)<br>

### Terminal 1:
```
cd ~/AgenticCoding/architect-cad
git clone https://github.com/neka-nat/freecad-mcp.git
cd freecad-mcp
cp -r addon/FreeCADMCP ~/snap/freecad/common/Mod/
rm -rf freecad-mcp
freecad
```
FreeCAD > View > Workbench > MCP Addon <br>
`Start RCP Server`<br>

### Terminal 2:
```
cd ~/AgenticCoding/architect-cad
opencode
```
/models `Gemini 3 Flash Preview`<br>

---
#### Prompt
```
read ./floorplan_3_bedroom.webp, then draw the floorplan in freecad
```
##### floorplan_3_bedroom.webp
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/architect-cad/floorplan_3_bedroom.webp)
##### freecad
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/architect-cad/freecad_floorplan_3_bedroom.png)

---
#### Prompt
```
read ./Simple-House-Design.webp, then create the house in freecad
```
#### Simple-House-Design.webp
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/architect-cad/Simple-House-Design.webp)
#### freecad
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/architect-cad/freecad_SimpleHouseDesign.png)

