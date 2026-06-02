## [OpenCode](https://github.com/anomalyco/opencode)
`cd ~`<br>

### Linux
#### install NodeJS
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 25

node -v
npm -v
```
#### install OpenCode
```
curl -fsSL https://opencode.ai/install | bash
```

---
### Windows
Download [NodeJS .msi](https://nodejs.org/dist/v25.9.0/node-v25.9.0-x64.msi)<br>
Open Powershell with adminstrator(管理員權限)<br>
```
Powershell> Set-ExecutionPolicy RemoteSigned
```
run NodeJS.msi<br>
```
Powershell> node -v
Powershell> npm -v
```

#### install opencode
```
Powershell> `npm i -g opencode-ai@latest`
Powershell> `opencode -v`<br>
```

---
### to project directory
```
cd AgenticCoding
opencode web
```

#### configuration
[~/.opencode/[opencode.json](https://github.com/rkuo2000/AgenticCoding/blob/main/opencode.json)<br>
```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      },
      "models": {
        "gemma4-31b-ctx64k:latest": {
          "name": "gemma4-31b-ctx64k:latest",
          "tools": true,
          "reasoning": true
        }
      }
    }
  },
  "model": "ollama/gemma4-31b-ctx64k:latest",
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
    },
    "unityMCP": {
      "type": "remote",
      "url": "http://127.0.0.1:8080/mcp",
      "enabled": true
    },
    "godot": {
      "type": "local",
      "command": [
        "uvx",
        "godot-mcp"
      ]
    }
}    
```

---
### 教學影片
* [OpenCode setup: Beginner’s Crash course](https://www.youtube.com/watch?v=8toBNmRDO90)
* [OpenCode详细攻略](https://www.youtube.com/watch?v=JYVTUU9ClUA)
