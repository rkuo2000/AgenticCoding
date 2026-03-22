# Agentic Coding
**Paper**: [Vibe Coding vs Agentic Coding](https://arxiv.org/html/2505.19443v1)<br>
<img width="50%" height="50%" src="https://arxiv.org/html/2505.19443v1/x3.png">

## Coder

### [OpenCode](https://github.com/rkuo2000/AgenticCoding/edit/main/OpenCode.md)

---
## Use-Cases

### Depth-Camera (深度相機)
`模型:Depth-Anything-V2`<br>

#### Prompt
```
use Depth-Anything-V2 to create a webcam app for depth image, and point-cloud image generation
```

`python main.py`<br>
用電腦打開瀏覽器`localhost:7860`<br>
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/depth-camera/depth-camera.png)

---
### PMSM-Current-Control (永磁同步馬達之電流控制)
`MATLAB/Octave`<br>

[MATLAB MCP-Core-Server](https://github.com/matlab/matlab-mcp-core-server)<br>

#### Prompt
```
create MATLAB mcp server for my current-control project use
```

```
create a PMSM current-control circuit, and call Matlab/Octave to simulate the circuit to provide result
```

![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/pmsm-current-control/result.png)


---
### Navbot-CAD
`FreeCAD`<br>

#### Prompt
```
study https://github.com/fuwei007/Navbot-EN01 to find its 3D CAD files, then create the robot in freecad
```
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/navbot-cad/freecad_Navbot-EN01.png)

---
### Architect-CAD
`FreeCAD`<br>

[FreeCAD MCP](https://github.com/neka-nat/freecad-mcp)<br>
~/.config/opencode/opencode.json <br>

```
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ollama/nemotron-cascade-2:latest",
  "provider": {
    "ollama": {
      "models": {
        "nemotron-cascade-2:latest": {
          "_launch": true,
          "name": "Nemotron-Cascade-2"
        }
      },
      "name": "Ollama (local)",
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      }
    }
  },
  "mcp": {
    "freecad": {
      "type": "local",
      "command": [        
        "uvx",
        "freecad-mcp"
      ]
    }
  }
}
```

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

#### Terminal 2:
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

---
### Interior-Design (室內設計)
`Krita` `模型:Z-Image Turbo`

[Krita 下載](https://krita.org/zh-tw/download/)<br>

#### Krita 設定
[ai-diffusion python plugin](https://github.com/Acly/krita-ai-diffusion)<br>

Tools > Scripts > Import Python Plugin from File : [Download krita_ai_diffusion.zip](https://github.com/Acly/krita-ai-diffusion/releases)<br>
Settings > Configure Krita > Python Plugin Manager : pick [AI Image Diffusion], click [OK]<br>
Restart Krita<br>
File > New > Custom_Document : click [Create]<br>

#### Prompt
```
Modern double-height luxury living room with floor-to-ceiling windows and city views. Large grey L-shaped sectional sofa, round coffee table, and light rug on hardwood floors. Tall tropical plants, abstract wall art, and minimalist lighting. Bright daylight with sharp shadows.
```
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/interior-design/interior_design.png)

---
### Digital-Art
`Krita` `模型:Z-Image Turbo`

#### [美女咒語](https://github.com/rkuo2000/AgenticCoding/blob/main/digital-art/beauty_prompt.md)

#### Prompt
```
3:4豎版全身寫真:年輕亞洲女性，20歲，身材傲人(胸部豐滿高挺巨大:1.5)，(腰部纖細:1.5)，身高170CM，體型修長勻稱，一比一點五修長柔美雙腿，鵝蛋臉輪廓柔和，肌膚白皙透亮。
深棕瞳孔大眼，自然淡妝配細長睫毛，鼻樑小巧唇形飽滿，淡玫瑰色水潤唇彩。烏黑柔亮長直發+空氣瀏海，部分髮絲垂至肩部，髮尾微捲。
灰色V領吊帶長版背心，柔質面料勾勒優雅線條。同色高腰迷你包臀裙。腳穿暗灰色低跟涼鞋。
1/4側身站立，含蓄微笑眼神溫柔。
米色背景窗邊柔光，側逆光勾勒髮絲與臉頰高光。
使用 28mm f/1.4 鏡頭，遠景拍攝全身入鏡，淺景深效果，電影感寫實主義。精緻皮膚紋理，8K超清畫質。溫暖低飽和色調，營造靜謐療癒氛圍。
```
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/digital-art/digital_girl.png)

---
### Blender-3D
`Blender`

[Blender download](https://www.blender.org/download/)<br>
[Blender MCP](https://github.com/ahujasid/blender-mcp)<br>
* Run Blender <br>
Edit > Preference > Addons > Install from Disk..<br>
import ~/AgenticCoding/blender-3d/blender-mcp/addon.py<br>
press N, and click `Connect to MCP Server` <br>

```
cd ~/AgenticCoding/blender-3d
opencode
```
/models Big Pickle `OpenCode Zen`<br>

### prompt
```
create a Wall-E robot in 3D obj, then build it in blender
```
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/blender-3d/blender_robot.png)




