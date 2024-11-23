kind create cluster --config kind.config

ver en [la web oficial](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)

kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml

se puede demorar subiendo calico
kubectl get pods -n kube-system
kubectl get networkpolicy

```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
kubectl apply -f networkPolicy.yml
```


## Pod temporal y Pruebas de conectividad

- `kubectl run curlpod --image=curlimages/curl --restart=Never --labels="app=curlpod" -i --tty --rm --command -- curl http://service-a:80`

- `kubectl exec -it app-b-69b87796c8-8trzd -- curl http://service-a:80`
