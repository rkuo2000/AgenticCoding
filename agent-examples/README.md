## AgentCoding Examples

### Add Plugins
#### [rtk](https://github.com/rtk-ai/rtk) (reduce tokens)
`curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh`<br>
```
rtk init -g                     # Claude Code / Copilot (default)
rtk init -g --gemini            # Gemini CLI
rtk init -g --codex             # Codex (OpenAI)
rtk init -g --opencode          # OpenCode
rtk init -g --agent cursor      # Cursor
rtk init -g --agent windsurf    # Windsurf
rtk init --agent cline          # Cline / Roo Code
rtk init --agent kilocode       # Kilo Code
rtk init --agent antigravity    # Google Antigravity
rtk init -g --agent pi          # Pi
rtk init --agent hermes         # Hermes
```

---
### Add Skills

#### Prompt: *add WebWright skill*
```
study https://github.com/microsoft/webwright and install WebWright skill
```

---
#### Prompt: *use WebWright skill*
```
WebWright search NBA games and results
```

---
#### Prompt: *use WebWright skill*
```
WebWright search Google Flight to find a ticket from SEA to JFK on 2026/8/15
```

---
### Gif Generation
#### Prompt:
```
Create a gif of NVIDIA-green-dots on black scatter, form Taipei 101 building, morph to "GTC TAIPEI 2026" , morph to the NVIDIA eye logo, then scatter and repeat
```

#### [generate_gtc_gif.py](https://github.com/rkuo2000/AgenticCoding/blob/main/agent-examples/generate_gtc_gif.py) by Ollama-local *Gemma4-31b-ctx64*
![](https://github.com/rkuo2000/AgenticCoding/blob/main/agent-examples/nvidia_gtc.gif?raw=true)

