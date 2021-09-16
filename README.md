## GitOps with Argo Project

Create a cluster:
```
minikube start
```

Install argo cli (optional):
```
# Download the binary
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.1.9/argo-darwin-amd64.gz

# Unzip
gunzip argo-darwin-amd64.gz

# Make binary executable
chmod +x argo-darwin-amd64

# Move binary to path
mv ./argo-darwin-amd64 /usr/local/bin/argo

# Test installation
argo version
```

## Install Argo Events + Workflows

Resources:
- https://argoproj.github.io/argo-events/installation/
- https://argoproj.github.io/argo-workflows/quick-start/

Create k8s resources:
```
kubectl create namespace argo-events
```

```
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/namespace-install.yaml
```

```
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml
```

```
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-workflows/stable/manifests/quick-start-postgres.yaml
```


Expose the service on localhost:
```
kubectl -n argo-events port-forward deployment/argo-server 2746:2746
```

Check http://localhost:2746 for ArgoWorkflows UI.

## Create an example gitops push-based pipeline

Create dockerhub credentials:

```
export REGISTRY_SERVER=https://index.docker.io/v1/
export REGISTRY_USER=YOUR_DOCKER_HUB_USERNAME
export REGISTRY_PASS=YOUR_DOCKER_HUB_PASSWORD
export REGISTRY_EMAIL=YOUR_DOCKER_HUB_EMAIL
```

```
kubectl --namespace argo-events \
    create secret \
    docker-registry docker-registry-credentials \
    --docker-server=$REGISTRY_SERVER \
    --docker-username=$REGISTRY_USER \
    --docker-password=$REGISTRY_PASS \
    --docker-email=$REGISTRY_EMAIL
```

```
kubectl -n argo-events apply -f deployment/*
```