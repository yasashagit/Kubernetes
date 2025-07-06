## Create Deployment

Apply the deployment manifest:

```sh
kubectl apply -f manifest/deployment.yaml
```

## Set Up Port Forwarding

Forward local port 8000 to the deployment's port 8080:

```sh
kubectl port-forward deployment/<deployment-name> 8000:8080
```

## Access the Web Page

Open [http://localhost:8000/](http://localhost:8000/) in your browser.
