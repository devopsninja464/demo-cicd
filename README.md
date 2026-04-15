# demo-cicd
demo-cicd


Sample Python web app used in the Jenkins CI/CD Lab

Students clone this repo inside a Jenkins pipeline and run it through automated Test → Build → Deploy stages.

## Files

| File | Purpose |
|---|---|
| `app.py` | Python HTTP server serving the AvantiIQ demo page |
| `Dockerfile` | Packages the app into a container image |

## How it's used

The Jenkins pipeline checks out this repo, runs tests against `app.py`, builds a Docker image, and deploys a live container — all automatically.

```
Checkout → Test → Build Docker Image → Deploy
```

## Run locally

```bash
python app.py
# open http://localhost:8000
```

## Run with Docker

```bash
docker build -t cicd-demo .
docker run -p 8000:8000 cicd-demo
# open http://localhost:8000
```

---

