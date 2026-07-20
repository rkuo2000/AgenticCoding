## [OpenCode](https://github.com/anomalyco/opencode)

### NodeJS 

#### Windows
Download [NodeJS .msi](https://nodejs.org/dist/v26.3.0/node-v26.3.0-x64.msi)<br>
Open Powershell with adminstrator(管理員權限)<br>
```
Powershell> Set-ExecutionPolicy RemoteSigned
```
run NodeJS.msi<br>
```
Powershell> node -v
Powershell> npm -v
```

---
#### Linux
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 26

node -v
npm -v
```

---
### OpenCode 
```
npm config set allow-scripts=opencode-ai --location=user
npm install -g opencode-ai@latest
```

#### to working directory
```
cd ~/AgenticCoding
opencode
```

#### configuration
[~/.opencode/opencode.json](https://github.com/rkuo2000/AgenticCoding/blob/main/opencode.json)<br>
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
        "gemma4:e2b": {
          "name": "Gemma4:E2B",
          "modalities": { "input": ["text", "image"], "output": ["text"] },
          "tools": true,
          "reasoning": true
        }
      }
    }
  },
  "model": "ollama/gemma4:e2b",
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
