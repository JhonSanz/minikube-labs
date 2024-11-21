kind create cluster --config kind.config

ver en [la web oficial](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)

kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml

se puede demorar subiendo calico
kubectl get pods -n kube-system
kubectl get networkpolicy


kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
kubectl apply -f networkPolicy.yml


pod temporal

kubectl run curlpod --image=curlimages/curl -i --tty --rm

pruebas de conectividad

curl service-a.default.svc.cluster.local
curl service-b.default.svc.cluster.local
curl service-c.default.svc.cluster.local
