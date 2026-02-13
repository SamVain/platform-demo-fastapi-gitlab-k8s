# platform-demo-fastapi-gitlab-k8s

A small, production-style demo service showing:
- FastAPI service with health/version endpoints
- GitLab CI pipeline: lint → test → build → scan → publish
- Helm chart for Kubernetes deployments
- Local Kubernetes deployment via kind

## Endpoints
- `GET /healthz`  -> liveness
- `GET /readyz`   -> readiness
- `GET /version`  -> build metadata (commit, build time)

## Architecture (simple)
Developer push → GitLab CI runs lint/test/build/scan → image published (main branch) → deploy via Helm.

## Local quickstart (kind)
### Prereqs
- Docker
- kubectl
- helm
- kind

### Run
```bash
make lint
make test
make build

make kind-up
make load-image
make deploy-dev

make status
make port-forward
```

Then
```
curl http://localhost:8080/healthz
curl http://localhost:8080/readyz
curl http://localhost:8080/version
```

## GitLab CI Overview
Stages:
1. **Lint**: Lint with ruff
2. **Pytest**: Run tests with pytest
3. **Build**: Build Docker image
4. **Scan**: Scan image with trivy (fails pipeline on HIGH/CRITICAL)
5. **Publish**: Publish to GitLab Container Registry (main branch only)

##Notes
- Local deployments use a locally-built image loaded into kind.
- In GitLab, publishing uses CI_REGISTRY_IMAGE automatically.

---

## What you do next (exact steps)

1) Create the repo folder and files locally (copy/paste from above).
2) Commit and push to GitHub:
```bash
git init
git add .
git commit -m "Initial platform demo: FastAPI + Helm + kind"
git branch -M main
git remote add origin git@github.com:SamVain/platform-demo-fastapi-gitlab-k8s.git
git push -u origin main
```