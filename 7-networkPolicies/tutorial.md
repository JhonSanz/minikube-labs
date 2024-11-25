## Parte 1

Retomamos el comando para crear el cluster con configuración personalizada, en donde agregamos:

```yml
networking:
  disableDefaultCNI: true # Deshabilitamos el CNI predeterminado para usar Calico
  podSubnet: "192.168.0.0/16" # Subred para los pods
```

y luego como antes ejecutamos

- `kind create cluster --config kind.config`

## Parte 2

Vamos a instalar Calico, el cual es un gestor de red para kubernetes. Como vimos anteriormente deshabilitamos el que viene por defecto e instalamos Calico con:

> Ver en [la web oficial](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises#install-calico)

- `kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml`

Se puede demorar un poco subiendo Calico, así que vamos a monitorear la creación de los pods encargados de gestionar Calico.

- `kubectl get pods -n kube-system -w`

## Parte 3

Es muyyyy importante seguir el orden de instalación ya que vamos a utilizar también el ingress, si instalamos este antes de Calico y con `disableDefaultCNI: true` es posible que tengamos errores y no funcione.... Así que siguiendo el orden ejecutamos:

- `kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml`
- `kubectl get pods -n ingress-nginx -w`

como vimos en el tutorial de ingress.

## Parte 4

Ejecutamos el resto de comandos a los que estamos acostumbrados, adicionando `kubectl apply -f networkPolicy.yml` para crear las networPolicies

```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
kubectl apply -f networkPolicy.yml
```

## Pruebas de conectividad

El comportamiento esperado es que nos podamos comunicar desde el servicio A a B, pero no desde el servicio B a A. Verifiquemos esto con los siguientes comandos:

1. `kubectl exec -it app-a-b4894b674-fz6f9 -- curl http://192.168.239.201:80`
2. `kubectl exec -it app-b-69b87796c8-wqcsp -- curl http://192.168.239.200:80`

Deberíamos tener respuesta en 1. pero no en 2. donde deberíamos ver un timeout
