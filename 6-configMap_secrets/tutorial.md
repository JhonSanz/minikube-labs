docker build -t fastapi-configmap .

kind create cluster --config kind.config
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
kind load docker-image fastapi-configmap:latest

docker exec -it kind-control-plane crictl images


```yml
envFrom:
- configMapRef:
    name: my-config
- secretRef:
    name: my-secret
```


```yml
spec:
    containers:
        # ...
        imagePullPolicy: IfNotPresent
```


kubectl apply -f configMap.yml
kubectl apply -f secrets.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml