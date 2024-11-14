
## Parte 1

Debido al uso de kind tenemos que considerar que **kind corre los contenedores en docker** y eso es determinante en terminos de red. Conceptualmente hablando un Ingress se ocupa de recibir el tráfico desde fuera de kubernetes hacia dentro del cluster, y si el cluster está en una red de docker dentro de nuestro host, de alguna manera tenemos que habilitar el portMapping (algo similar a lo que ocurre con docker compose)

Para esto tenemos que crear una versión personalizada para nuestro cluster create así

```config
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
```

Aqui podemos ver que estamos recibiendo tráfico desde "fuera" es decir, **desde nuestro host**.

Entonces ejecutamos el comando `kind create cluster --config kind.config` para crear nuestro cluster con esa configuración

## Parte 2

La segunda cosa importante es que kind no tiene el ingress controller instalado por defecto, así que hay que instalarlo. Importante referirse a la [documentación oficial](https://kind.sigs.k8s.io/docs/user/ingress/#ingress-nginx)

- `kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml`

Esto levantará 3 pods que podemos ver con `kubectl get pods -n ingress-nginx`

```
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-lpfhx        0/1     Completed   0          28m
ingress-nginx-admission-patch-vshxj         0/1     Completed   0          28m
ingress-nginx-controller-5f4f4d9787-gq9g7   1/1     Running     0          28m
```

El importante es `ingress-nginx-controller` ya que los otros dos son para inicializar.


Finalmente podemos aplicar nuestros bellos archivos de configuración en este orden

1. kubectl apply -f deployment.yml
2. kubectl apply -f service.yml
3. kubectl apply -f ingress.yml


## Parte 3

Tenemos en nuestro `ingress.yml` la linea 

- `- host: apache.example.com`

Para que esto funcione debemos agregar una configuración en nuestro host (o nuestro pc). Debemos ir a nuestro archivos `C:\Windows\System32\drivers\etc\hosts` o `/etc/hosts` y agregar al final

- `127.0.0.1 apache.example.com`

Esto hará que se mapeé la direccion apache.example.com a localhost
