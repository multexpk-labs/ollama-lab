# Ollama Lab

Practical experiments with Ollama for local and remote large-language-model serving.

## Focus
- Installing and operating Ollama
- Model lifecycle and storage
- Local and remote API usage
- GPU and CPU inference
- Model selection and quantization
- API integration and automation
- Health checks and monitoring
- Resource planning and troubleshooting

## Basic Workflow

```text
Install -> Verify Runtime -> Pull Model -> Test Locally -> Measure Resources -> Integrate API -> Secure Remote Access -> Monitor -> Document
```

## First Checks

```bash
ollama --version
ollama list
ollama ps
systemctl status ollama
```

Local API:
```bash
curl http://127.0.0.1:11434/api/tags
```

## Model Lifecycle

```bash
ollama pull MODEL
ollama list
ollama show MODEL
ollama run MODEL
ollama rm MODEL
```

## Remote Ollama

```text
Application -> HTTPS / Authentication -> Reverse Proxy -> Private Network -> Ollama :11434 -> Model
```

Avoid exposing port 11434 directly to the public Internet without an explicit security design.

## API Example

```bash
curl http://127.0.0.1:11434/api/chat -H 'Content-Type: application/json' -d '{"model":"MODEL","messages":[{"role":"user","content":"Hello"}],"stream":false}'
```

## GPU Monitoring

```bash
nvidia-smi
watch -n 1 nvidia-smi
```

## Experiment Record
Record Ollama version, model/tag, quantization, CPU, RAM, GPU, VRAM, context, request type, latency, and observations.

## Troubleshooting

```bash
systemctl status ollama
journalctl -u ollama -n 100 --no-pager
ss -lntup | grep 11434
```

Remote failures should be isolated layer by layer: DNS -> TLS -> Reverse Proxy -> Firewall -> Ollama Listener -> Model.

## Research & Reimplementation
Find -> Clone -> Inspect -> Understand -> Document -> Reimplement -> Test -> Improve.

Public code is not automatically free to copy. Reuse must follow the original license and attribution requirements.

## Related MULTEXPK LABS
- llm-infrastructure
- ai-llm-research
- ai-agents-automation
- coding-agent-lab
- vps-automation
- cloud-infrastructure

## About
Maintained by **Zain Ul Abddin**, Founder of **MULTEXPK LTD ®™**.

**MULTEXPK LTD ®™ — Secure Cloud • VPS • Hosting • Automation**
https://webvpsserver.com
WhatsApp: +92 312 6565434

Never publish API tokens, private keys, customer prompts, production credentials, or private infrastructure details.

© MULTEXPK LTD ®™