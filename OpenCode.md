## [OpenCode](https://github.com/anomalyco/opencode)

### Install
For Linux, `curl -fsSL https://opencode.ai/install | bash` <br>

For Windows, run [NodeJS .msi](https://nodejs.org/dist/v25.8.1/node-v25.8.1-x64.msi)<br>
Open Powershell with adminstrator(管理員權限)<br>
```
Powershell> `node -v`
Powershell> `npm -v`
```
```
Powershell> `Set-ExecutionPolicy RemoteSigned`
```
```
Powershell> `npm i -g opencode-ai@latest`
Powershell> `opencode -v`<br>
```

![](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)

---
### Configuration

`~/.config/opencode/opencode.json`<br>
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
    },
    "blender": {
      "type": "local",
      "command": [        
        "uvx",
        "blender-mcp"
      ]
    }
  }
}
```

---
### 教學影片
* [OpenCode setup: Beginner’s Crash course](https://www.youtube.com/watch?v=8toBNmRDO90)
* [OpenCode详细攻略](https://www.youtube.com/watch?v=JYVTUU9ClUA)
