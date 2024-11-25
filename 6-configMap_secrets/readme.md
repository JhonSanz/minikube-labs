## Parte 1

Para este tutorial se crearon dos directorios, cluster y app. En app tenemos una app básica con FastApi, la cual se encarga de retornar los valores que vamos a obtener desde variables de entorno. También encontraremos un dockerfile para generar la imagen con nuestro código y pueda ser ejecutada en el cluster, entonces:

- Ejecutamos `docker build -t fastapi-configmap .`

## Parte 2

Como vimos en el tutorial anterior vamos a crear todo lo necesario para que nuestro ingress funcione, así que

```sh

kind create cluster --config kind.config
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
```

Y aqui viene algo **importante**. Debido a que kind corre sobre docker mismo, debemos importar nuestra imagen de fastapi generada en la parte 1, así:

- Ejecutamos `kind load docker-image fastapi-configmap:latest`

Evidentemente podríamos subirla a algún repositorio público de imágenes, pero somos perezosos y esto es solo para pruebas. Asi que verifiquemos que la imagen está disponible en el cluster así:

- `docker exec -it kind-control-plane crictl images`

Finalmente hay que agregar una configuración adicional en el deployment para que busque la imagen dentro del cluster:

```yml
spec:
    containers:
        # ...
        imagePullPolicy: IfNotPresent
```

## Parte 3

Ya tenemos nuestra imagen disponible, ahora configuremos el configMap y el secret de la siguiente manera

```yml
envFrom:
- configMapRef:
    name: my-config
- secretRef:
    name: my-secret
```

Ahora nuestro cluster inyectará en todos los pods de nuestro deployment estas variables de entorno, y podrán ser accedidas en nuestro endpoint de fastapi.

Finalmente aplicamos todo:

```sh
kubectl apply -f configMap.yml
kubectl apply -f secrets.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
kubectl apply -f ingress.yml
```

