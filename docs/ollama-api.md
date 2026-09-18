# Ollama API

Ollama provides a local HTTP API for model operations and inference.

## Check Models

```bash
curl http://127.0.0.1:11434/api/tags
```

## Chat Request

```bash
curl http://127.0.0.1:11434/api/chat -H 'Content-Type: application/json' -d '{"model":"MODEL","messages":[{"role":"user","content":"Explain DNS in three sentences."}],"stream":false}'
```

For production applications, add authentication and network controls outside the basic local API.

Do not put API credentials directly into source code.