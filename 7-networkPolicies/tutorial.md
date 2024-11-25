kind create cluster --config kind.config


ver en [la web oficial](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)

kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml

se puede demorar subiendo calico
kubectl get pods -n kube-system
kubectl get networkpolicy


kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
kubectl get pods -n ingress-nginx


```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
kubectl apply -f networkPolicy.yml
```


## Pruebas de conectividad

kubectl exec -it app-a-b4894b674-fz6f9 -- curl http://192.168.239.201:80
kubectl exec -it app-b-69b87796c8-wqcsp -- curl http://192.168.239.200:80
