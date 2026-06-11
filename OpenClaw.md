## OpenClaw ~ Personal Assistant

### OpenClaw Architecture
![](https://help.apiyi.com/wp-content/uploads/2026/01/clawdbot-beginner-guide-personal-ai-assistant-2026-fr-image-1.png)

**Blog**: [OpenClaw (Clawdbot) Architecture: Engineering Reliable and Controllable AI Agents](https://vertu.com/ai-tools/openclaw-clawdbot-architecture-engineering-reliable-and-controllable-ai-agents/)<br>

---
### OpenClaw setup

#### install [OpenClaw](https://github.com/openclaw/openclaw)
```
npm install -g openclaw@latest
openclaw -v
```
```
openclaw onboard --install-daemon
openclaw gateway restart
opencalw dashboard
```

[.openclaw/openclaw.json](https://github.com/rkuo2000/AgenticCoding/blob/main/openclaw.json)<br>

---
#### setup Ollama
add the following into `~/.openclaw/openclaw.json` <br>
```
  "models": {
    "mode": "merge",
    "providers": {
      "ollama": {
        "baseUrl": "http://127.0.0.1:11434/v1",
        "apiKey": "ollama",
        "api": "openai-responses",
        "models": [
          {
            "id": "gemma4-e2b:latest",
            "name": "Gemma4:e2b (Local)",
            "modalities": { "input": ["text", "image"], "output": ["text"] },
            "reasoning": false,
            "input": ["text"],
            "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },
            "contextWindow": 32768,
            "maxTokens": 4096
          }
        ]
      }
    }
```

To access a remote Ollama server: <br>
* modify openclaw.json, *replace `127.0.0.1` to `192.168.0.12` (remote ip addr)* 
* modify ufw rules on Ollama server, *`sudo ufw allow from 192.168.0.22`*

---
#### setup WhatsApp
*.openclaw/openclaw.json*<br>
```
  "channels": {
    "whatsapp": {
      "selfChatMode": true,
      "dmPolicy": "allowlist",
      "allowFrom": [
        "+886972123456"
      ]
    }
  },
```

---
#### setup Firewall
```
sudo apt install ufw -y
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow in on tailscale0 to any port 22
sudo ufw enable #Type 『y』 to confirm`
sudo ufw status
```
