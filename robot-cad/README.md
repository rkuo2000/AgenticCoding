## Robot CAD (機器人設計)
`FreeCAD`<br>

[FreeCAD 下載](https://www.freecad.org/downloads.php)<br>
[FreeCAD MCP](https://github.com/neka-nat/freecad-mcp)<br>

#### Terminal 1:
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

### OpenCode

#### Prompt
```
study https://github.com/fuwei007/Navbot-EN01 to find its 3D CAD files, then create the robot in freecad
```

![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/robot-cad/freecad_Navbot-EN01.png)

