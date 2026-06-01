## [OpenCode](https://github.com/anomalyco/opencode)

### Install NodeJS
[Download NodeJS](https://nodejs.org/en/download/current)<br>
For Linux,<br>
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 25
```

For Windows, <br>
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

---
### Install OpenCode
For Linux, `curl -fsSL https://opencode.ai/install | bash` <br>
For Windows, <br>
```
Powershell> `npm i -g opencode-ai@latest`
Powershell> `opencode -v`<br>
```

![](https://github.com/anomalyco/opencode/raw/dev/packages/web/src/assets/lander/screenshot.png)

---
### Configuration
~/.config/opencode/[opencode.json](https://github.com/rkuo2000/AgenticCoding/blob/main/opencode.json)<br>


---
### 教學影片
* [OpenCode setup: Beginner’s Crash course](https://www.youtube.com/watch?v=8toBNmRDO90)
* [OpenCode详细攻略](https://www.youtube.com/watch?v=JYVTUU9ClUA)
