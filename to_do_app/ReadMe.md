## Create kubectl cluster with

```
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```

## Deploy with

```
kubectl apply -f manifest/deployment.yaml
kubectl apply -f manifest/service.yaml
```

## Access Flask Server

Open [http://localhost:8082/](http://localhost:8082/) in your browser.
