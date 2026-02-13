APP_NAME=platform-demo
NAMESPACE=platform-demo
IMAGE=$(APP_NAME):local

.PHONY: venv
venv:
	uv venv

.PHONY: sync
sync:
	uv sync --all-extras

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: test
test:
	uv run pytest -q

.PHONY: build
build:
	docker build -t $(IMAGE) .

.PHONY: kind-up
kind-up:
	kind create cluster --config k8s/kind-config.yaml

.PHONY: kind-down
kind-down:
	kind delete cluster --name platform-demo

.PHONY: namespace
namespace:
	kubectl apply -f k8s/namespace.yaml

.PHONY: load-image
load-image:
	kind load docker-image $(IMAGE) --name platform-demo

.PHONY: deploy-dev
deploy-dev: namespace
	helm upgrade --install $(APP_NAME) helm/platform-demo -n $(NAMESPACE) \
		-f helm/platform-demo/values.yaml \
		-f helm/platform-demo/values-dev.yaml \
		--set image.repository=$(APP_NAME) \
		--set image.tag=local

.PHONY: port-forward
port-forward:
	kubectl -n $(NAMESPACE) port-forward svc/$(APP_NAME) 8080:80