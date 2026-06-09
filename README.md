# Agentic Coding

## Overview
* [AI-brief](https://rkuo2000.github.io/AI-course/lecture/2025/09/01/AI-Brief.html)
* [AI-Hardwares](https://rkuo2000.github.io/AI-course/lecture/2025/09/01/AI-Hardwares.html)
* [Agent-intro](https://rkuo2000.github.io/AI-course/lecture/2025/09/15/Agent.html)
  
**Paper**: [Vibe Coding vs Agentic Coding](https://arxiv.org/html/2505.19443v1)<br>
<img width="50%" height="50%" src="https://arxiv.org/html/2505.19443v1/x3.png">

---
## AI Engineering
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
## Local LLMs

### [Ollama](https://github.com/rkuo2000/AgenticCoding/blob/main/Ollama.md) ~  [*library*](https://ollama.com/library)
`ollama launch claude`<br>

### [LM Studio](https://github.com/rkuo2000/AgenticCoding/blob/main/LMstudio.md) ~  [*models*](https://lmstudio.ai/models)

---
## Agentic IDEs

### [OpenCode](https://github.com/rkuo2000/AgenticCoding/blob/main/OpenCode.md) - AI Coding Agent

### [Claude-Code](https://github.com/anthropics/claude-code) - Anthropic AI Coding IDE

### [Codex](https://github.com/openai/codex) - OpenAI AI Coding Partner

### [AntiGravity](https://antigravity.google/) - Google Agentic Development Platform

---
## Use-Cases

### [AgentCoding examples](https://github.com/rkuo2000/AgenticCoding/tree/main/agent-examples)

---
### [AI Stock 台灣股票分析師](https://github.com/rkuo2000/AgenticCoding/tree/main/ai-stock)

---
### [Depth-Camera (深度相機)](https://github.com/rkuo2000/AgenticCoding/tree/main/depth-camera)
`模型:Depth-Anything-V2`<br>

---
### [PMSM-Current-Control (永磁同步馬達之電流控制)](https://github.com/rkuo2000/AgenticCoding/tree/main/pmsm-sim)
`MATLAB/Octave`<br>

[MATLAB MCP-Core-Server](https://github.com/matlab/matlab-mcp-core-server)<br>

---
### [LTspice simulation（類比電路模擬）](https://github.com/rkuo2000/AgenticCoding/tree/main/ltspice-sim)

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
### [GoDot-Game (2D遊戲)](https://github.com/rkuo2000/AgenticCoding/tree/main/godot-game)
`GoDot`<br>

[GoDot 下載](https://godotengine.org/download/)<br>
[GoDot MCP](https://github.com/Coding-Solo/godot-mcp)<br>

---
## AI Assistant

### [OpenClaw](https://github.com/openclaw/openclaw) - Personal AI Assistant

### [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) - VTuber AI Assistant
```
python -m venv .venv
git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
cd Open-LLM-VTuber
uv sync
uv run --active run_server.py
```

---
## AI Agents

### [Hermes-Agent](https://github.com/nousresearch/hermes-agent) - AI Agents

### [OpenFang](https://github.com/RightNow-AI/openfang) - Agent OS

