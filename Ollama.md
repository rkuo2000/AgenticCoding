## [Ollama](https://github.com/ollama/ollama)

### Install
```
curl -fsSL https://ollama.com/install.sh | sh
```
#### commands
```
ollama -h
ollama -v
```

### Serve
Terminal #1: serve & monitor<br>
```
ollama serve
```
####

### Commands
```
ollama pull gemma4:e2b
ollama list
```

```
ollama rm gemma4:e2b
```

### Run
#### Terminal #2: run a model
```
ollama run gemma4:e2b
```

#### Launch an IDE
```
ollama launch opencode
```
```
ollama launch claude
```
```
ollama launch openclaw
```

### change Context-Size
```
ollama run gemma4:e2b
```
#### save a new model
```
/set parameter num_ctx 131072
/save gemma4-e2b-128k
```
#### run it
```
ollama run gemm4-e2b-128k
```
#### check process
```
ollama ps
```
| NAME | ID | SIZE | PROCESSOR | CONTEXT | UNTIL |
|------------------------|--------------|-------|----------|--------|--------------------|
| gemma4-e2b-128k:latest | 63f9752e8204 | 2.2GB | 100% GPU | 131072 | 4 minutes from now |
