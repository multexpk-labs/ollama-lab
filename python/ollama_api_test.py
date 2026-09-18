#!/usr/bin/env python3
import json, sys, time, urllib.request, urllib.error

base = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else 'http://127.0.0.1:11434'
model = sys.argv[2] if len(sys.argv) > 2 else 'MODEL'
payload = {'model': model, 'messages': [{'role':'user','content':'Reply with exactly: OLLAMA_OK'}], 'stream': False}
request = urllib.request.Request(base + '/api/chat', data=json.dumps(payload).encode(), headers={'Content-Type':'application/json'})
started = time.monotonic()
try:
    with urllib.request.urlopen(request, timeout=120) as response:
        body = response.read().decode()
        print(json.dumps({'status': response.status, 'elapsed_seconds': round(time.monotonic()-started,3), 'response': json.loads(body)}, indent=2))
except urllib.error.HTTPError as exc:
    print(json.dumps({'status': exc.code, 'error': exc.read().decode(errors='replace')}, indent=2))
    raise SystemExit(1)
except Exception as exc:
    print(json.dumps({'error': str(exc)}, indent=2))
    raise SystemExit(1)