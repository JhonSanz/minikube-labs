## Parte 1

Instalar helm

- `choco install kubernetes-helm` en Windows
- `helm version`


## Parte 2

kind create cluster --name prometheus-cluster
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install prometheus prometheus-community/prometheus --namespace monitoring
kubectl get all -n monitoring

utilizar port-forward o cambiar a nodeport
kubectl port-forward -n monitoring svc/prometheus-server 9090:80

---
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext -n monitoring
kubectl get svc -n monitoring    
---


## Parte 3

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install grafana grafana/grafana --namespace monitoring
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}"


kubectl port-forward --namespace monitoring svc/grafana 3000:80 --address=0.0.0.0

--- 

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tutorial-control-plane


kubectl logs -n monitoring grafana-6c59b65d98-q8kwz