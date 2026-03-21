# Agentic Coding
**Paper**: [Vibe Coding vs Agentic Coding](https://arxiv.org/html/2505.19443v1)<br>
<img width="50%" height="50%" src="https://arxiv.org/html/2505.19443v1/x3.png">

## Coder

### [OpenCode](https://github.com/anomalyco/opencode)
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

<p>
<iframe width="320" height="240" src="https://www.youtube.com/embed/8toBNmRDO90" title="OpenCode setup: Beginner’s Crash course" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<iframe width="320" height="240" src="https://www.youtube.com/embed/JYVTUU9ClUA" title="OpenCode详细攻略，开源版Claude Code，免费模型与神级插件  #ai #科技 #计算机 #编程 #coding" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</p>

---
## Use-Cases

### Depth-Camera (深度相機)
`pretrained-model`<br>

**Prompt**:<br>
```
use Depth-Anything-V2 to create a webcam app for depth image, and point-cloud image generation
```

`python main.py`<br>
用電腦打開瀏覽器`localhost:7860`<br>
![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/assets/depth-camera.png)

---
### PMSM-Current-Control (永磁同步馬達之電流控制)
[MATLAB MCP-Core-Server](https://github.com/matlab/matlab-mcp-core-server)<br>


**Prompt:**<br>
```
create MATLAB mcp server for my current-control project use
```

```
create a PMSM current-control circuit, and call Matlab/Octave to simulate the circuit to provide result
```

![](https://raw.githubusercontent.com/rkuo2000/AgenticCoding/refs/heads/main/assets/pmsm-current-control.png)

---


