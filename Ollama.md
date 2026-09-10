## [Ollama](https://github.com/ollama/ollama)

### Install
`curl -fsSL https://ollama.com/install.sh | sh` <br>

#### Commands
```
ollama -h
ollama -v
```

---
### Commands
#### download a model
`ollama pull gemma4:e2b` <br>

#### list installed models
`ollama list` <br>

#### Remove a model
`ollama rm gemma4:e2b` <br>

#### check the running models 
`ollama ps` <br>
```
NAME          ID              SIZE      PROCESSOR    CONTEXT    UNTIL              
gemma4:e2b    7fbdbf8f5e45    1.9 GB    100% GPU     32768      4 minutes from now 
```

---
### Run Model
#### Terminal #2: run a model
`ollama run gemma4:e2b --verbose` <br>

#### Launch from IDE
`ollama launch opencode --model gemma4:e2b` <br>

`ollama launch claude` <br>

---
### Create Model

#### adjust Context-Size
edit Modelfile <br>
```
FROM gemma4:e2b
PARAMETER num_ctx 131072
```

#### create a model
`ollama create gemma4-128K:e2b -f Modelfile`<br>

#### run a model
`ollama run gemm4-128k:e2b --verbose`<br>

ollama ps
```
