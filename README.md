# Agentic Coding

## Overview
* [AI-brief](https://rkuo2000.github.io/AI-course/lecture/2026/06/01/AI-Brief.html)
* [AI-Hardwares](https://rkuo2000.github.io/AI-course/lecture/2026/06/01/AI-Hardwares.html)
* [Agent-intro](https://rkuo2000.github.io/AI-course/lecture/2026/06/08/Agent.html)

---
### AI Engineering
* 第一代：Prompt Engineering（2022-2024）
* 第二代：[Context Engineering](https://ihower.tw/blog/12817-context-engineering)（2025）
* 第三代：[Harness Engineering](https://hackmd.io/@BASHCAT/SkQEW0F2bg)（2026）

#### Anthropic Claude Code：三代理 Harness 架構
| Agent	    | 角色   |	 職責                          |
|-----------|-------|--------------------------------|
| Planner	  | 規劃者 |	把產品規格分解為可執行的任務列表    |
| Generator	| 生成者	| 一次實作一個 feature，保持增量開發 |
| Evaluator	| 評估者	| 驗證生成結果，回饋修正指令         |

[![](https://markdown-videos-api.jorgenkh.no/youtube/R6fZR_9kmIw)](https://youtu.be/R6fZR_9kmIw)

---
### Local LLMs

### [Ollama](https://github.com/rkuo2000/AgenticCoding/blob/main/Ollama.md) ~  [*library*](https://ollama.com/library)
`ollama launch opencode`<br>

### [LM Studio](https://github.com/rkuo2000/AgenticCoding/blob/main/LMstudio.md) ~  [*models*](https://lmstudio.ai/models)

---
### Agentic IDEs

* [Claude-Code](https://github.com/anthropics/claude-code) - Anthropic AI Coding IDE
* [Codex](https://github.com/openai/codex) - OpenAI AI Coding Partner
* [AntiGravity](https://antigravity.google/) - Google Agentic Development Platform
* [OpenCode](https://github.com/anomalyco/opencode) - AI Coding Agent

### [OpenCode 安裝](https://github.com/rkuo2000/AgenticCoding/blob/main/OpenCode.md)

---
## Examples

### [Agent-basic](https://github.com/rkuo2000/AgenticCoding/tree/main/agent-examples)

---
### [AI-Stock（台灣股票分析）](https://github.com/rkuo2000/AgenticCoding/tree/main/ai-stock)
`LLM：Gemina-2.5-Flash`<br>

---
### [Financial-Report（社區財報）](https://github.com/rkuo2000/AgenticCoding/tree/main/financial-report)
`LLM：Gemina-2.5-Flash`<br>

---
### [Floor-Planner（平面設計圖）](https://github.com/rkuo2000/AgenticCoding/tree/main/floor-planner)
`LLM：Gemina-2.5-Flash`<br>

---
### [Depth-Camera (深度相機)](https://github.com/rkuo2000/AgenticCoding/tree/main/depth-camera)
`模型：Depth-Anything-V2`<br>

---
### [PMSM-Current-Control (永磁同步馬達之電流控制)](https://github.com/rkuo2000/AgenticCoding/tree/main/pmsm-sim)
`MATLAB/Octave`<br>

[MATLAB MCP-Core-Server](https://github.com/matlab/matlab-mcp-core-server)<br>

---
### [LTspice simulation（類比電路模擬）](https://github.com/rkuo2000/AgenticCoding/tree/main/ltspice-sim)
`LTspice`<br>

---
### [Navbot-CAD (兩腿輪機器人）](https://github.com/rkuo2000/AgenticCoding/tree/main/robot-cad)
`FreeCAD`<br>

[FreeCAD 下載](https://www.freecad.org/downloads.php)<br>
[FreeCAD MCP](https://github.com/neka-nat/freecad-mcp)<br>

---
### [Architect-CAD (建築設計）](https://github.com/rkuo2000/AgenticCoding/tree/main/architect-cad)
`FreeCAD`<br>

[FreeCAD 下載](https://www.freecad.org/downloads.php)<br>
[FreeCAD MCP](https://github.com/neka-nat/freecad-mcp)<br>

---
### [Interior-Design (室內設計)](https://github.com/rkuo2000/AgenticCoding/tree/main/interior-design)
`Krita` `模型:Z-Image Turbo`

[Krita 下載](https://krita.org/zh-tw/download/)<br>
[Krita AI-diffusion 插件](https://github.com/Acly/krita-ai-diffusion)<br>

---
### [Digital-Art（數位藝術）](https://github.com/rkuo2000/AgenticCoding/tree/main/digital-art)
`Krita` `模型:Z-Image Turbo`

[Krita 下載](https://krita.org/zh-tw/download/)<br>
[Krita AI-diffusion 插件](https://github.com/Acly/krita-ai-diffusion)<br>

---
### [Blender-3D (3D模型)](https://github.com/rkuo2000/AgenticCoding/tree/main/blender-3d)
`Blender`<br>

[Blender 下載](https://www.blender.org/download/)<br>
[BlenderMCP](https://github.com/ahujasid/blender-mcp)<br>

---
### [Unity-Gym (3D場景)](https://github.com/rkuo2000/AgenticCoding/tree/main/unity-gym)
`Unity`<br>

[Unity-Hub 下載](https://unity.com/download)<br>
[MCP for Unity](https://github.com/CoplayDev/unity-mcp)<br>

---
### [Game-GoDot (遊戲設計)](https://github.com/rkuo2000/AgenticCoding/tree/main/game-godot)
`GoDot`<br>

[GoDot 下載](https://godotengine.org/download/)<br>
[GoDot MCP](https://github.com/ee0pdt/Godot-MCP/)<br>

---
## AI Assistant

### [OpenClaw](https://github.com/rkuo2000/AgenticCoding/blob/main/OpenClaw.md) - Personal AI Assistant
```
sudo npm install -g openclaw@latest
```
```
openclaw onboard --install-daemon
openclaw dashboard
```

`ollama launch openclaw --model gemma4:e2b`<br>

---
### [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) - VTuber AI Assistant
![](https://github.com/rkuo2000/AI-course/blob/main/assets/images/Open-LLM-VTuber.png?raw=true)

#### Download [Release v1.2.1-en](https://pub-17317087be374bc68161ac63de2022a5.r2.dev/v1.2.1/Open-LLM-VTuber-v1.2.1-en.zip)
```
cd ~/Downloads
unzip Open-LLM-VTuber-v1.2.1-en.zip
mv Open-LLM-VTuber-v1.2.1-en Open-LLM-VTuber
mv Open-LLM-VTuber ..
cd ~/Open-LLM-VTuber
```

#### modify ollama_llm in conf.yaml
```
      llm_provider: 'ollama_llm'
      ollama_llm:
        base_url: 'http://localhost:11434/v1'
        model: 'gemma4-it-128k:e2b'
        temperature: 1.0 # value between 0 to 2
        # seconds to keep the model in memory after inactivity.
        # set to -1 to keep the model in memory forever (even after exiting open llm vtuber)
        keep_alive: -1
        unload_at_exit: True # unload the model from memory at exit
```

#### upgrade edge-tts
```
uv sync
source .venv/bin/activate
uv pip install edge-tts --upgrade
python run_server.py
```

---
## AI Agents

### [Hermes-Agent](https://github.com/nousresearch/hermes-agent) - AI Agents
#### Linux / macOS / WSL2 / Android (Termux)
```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```
#### Windows <Powershell>
```
iex (irm https://hermes-agent.nousresearch.com/install.ps1) 
```
#### Herems setup / dashboard
```
hermes setup
hermes dashboard
```
#### ollama launch
`ollama launch hermes`<br>
`ollama launch hermes-desktop --model gemma4:e2b`<br>

#### Hermes Desktop
```
hermes desktop
```
[![](https://markdown-videos-api.jorgenkh.no/youtube/-EivK7vpOXY)](https://youtu.be/-EivK7vpOXY)

#### Hermes + [JARVIS](https://github.com/eadmin2/jarvis_ai)
[![](https://markdown-videos-api.jorgenkh.no/youtube/pfsGO14eTe4)](https://youtu.be/pfsGO14eTe4)

---
### [OpenFang](https://github.com/RightNow-AI/openfang) - Agent OS
```
curl -fsSL https://openfang.sh/install | sh
openfang init
openfang start
# Dashboard live at http://localhost:4200
```
