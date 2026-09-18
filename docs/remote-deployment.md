# Remote Ollama Deployment

A remote Ollama server should be treated as an API service.

## Recommended Pattern

```text
Client -> HTTPS -> Reverse Proxy / Gateway -> Private Network -> Ollama
```

## Checklist
- DNS configured
- TLS configured
- Authentication implemented
- Firewall reviewed
- Ollama listener verified
- Resource limits considered
- Logs available
- Health check tested
- Recovery procedure documented