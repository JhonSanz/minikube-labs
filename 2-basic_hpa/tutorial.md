como ya tenía servicios creados del ejercicio project1 debo borrar esas cosas que creé, entonces

1. Ver los elementos de mi cluster con `kubectl get all --all-namespaces`. Aquí me mostrará todo, entonces es importante tener en cuenta que hay recursos creados por kubernetes para su funcionamiento y por lo tanto debo identificar lo que realmente queremos administrar
2. Retomando el ejercicio anterior creamos un **deployment y un service** entonces `kubectl get deployment` y `kubectl get svc` funcionarán
3. Ahora solo basta con eliminar ambos con `kubectl delete deployment nginx-deployment` y `kubectl delete service nginx-service`

---

1. Crear nuestros recursos deployment.yaml, service.yaml y hpa.yaml
2. HPA necesita del metrics-server entonces correr `minikube addons enable metrics-server`, con `kubectl get pods -n kube-system` podemos verificar que existe un pod para el metrics-server en estado running
3. Ahora vamos a observar como el HPA de alguna manera sobreescribe la configuración `replicas: 1` de deployment.yaml y crea replicas basado en el uso de CPU de nuestros pods. así que
   1. Corremnos `kubectl exec -it $(kubectl get pods -l app=my-app -o jsonpath='{.items[0].metadata.name}') -- /bin/bash` para entrar a nuestros pods
   2. Instalamos el paquete stress para simular consumo de CPU `apt-get update && apt-get install -y stress`
   3. Ejecutamos el comando `stress --cpu 4`
4. En este punto se empezará a simular el consumo de recursos de nuestros pods, entonces para ver en vivo actuar al HPA corremos `kubectl get hpa -w` y `kubectl get pod -w`

```sh
kubectl get hpa -w
NAME         REFERENCE           TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
my-app-hpa   Deployment/my-app   cpu: 23%/50%   1         5         1          10m
my-app-hpa   Deployment/my-app   cpu: 110%/50%   1         5         1          11m
my-app-hpa   Deployment/my-app   cpu: 137%/50%   1         5         1          11m
my-app-hpa   Deployment/my-app   cpu: 137%/50%   1         5         3          12m
my-app-hpa   Deployment/my-app   cpu: 145%/50%   1         5         3          12m
my-app-hpa   Deployment/my-app   cpu: 50%/50%    1         5         3          13m


kubectl get pod -w
NAME                      READY   STATUS    RESTARTS   AGE
my-app-75d668c5db-zvpl9   1/1     Running   0          12m
my-app-75d668c5db-p85zs   0/1     Pending   0          0s
NAME                      READY   STATUS    RESTARTS   AGE
my-app-75d668c5db-zvpl9   1/1     Running   0          12m
my-app-75d668c5db-zvpl9   1/1     Running   0          12m
my-app-75d668c5db-p85zs   0/1     Pending   0          0s
my-app-75d668c5db-khgmb   0/1     Pending   0          0s
my-app-75d668c5db-p85zs   0/1     Pending   0          0s
my-app-75d668c5db-khgmb   0/1     Pending   0          0s
my-app-75d668c5db-p85zs   0/1     ContainerCreating   0          0s
my-app-75d668c5db-khgmb   0/1     ContainerCreating   0          0s
my-app-75d668c5db-khgmb   1/1     Running             0          7s
my-app-75d668c5db-p85zs   1/1     Running             0          9s
```

Lo que estás viendo es el comportamiento esperado de un Horizontal Pod Autoscaler (HPA) en acción. Aquí te explico lo que ocurre paso a paso:

### Inicio del stress test:

- Ejecutaste stress --cpu 4, lo cual hace que el contenedor de Nginx en el Pod use significativamente más CPU.

### Monitorización del HPA:

- El HPA está configurado para monitorear la utilización de la CPU y ajustar el número de réplicas de Pods según la carga.
-El HPA comienza con una sola réplica (un Pod).

### Incremento de la carga de CPU:

- Inicialmente, el HPA muestra que la utilización de la CPU es del 23%, lo que está por debajo del umbral del 50%, por lo que no escala.
- Después, la CPU sube al 110%, superando el umbral del 50%, pero aún no escala de inmediato.
- Cuando la CPU llega al 137%, el HPA decide que es necesario escalar y comienza a crear más Pods.

### Escalado de Pods:

- Al detectar que la CPU está por encima del umbral, el HPA escala el número de réplicas de 1 a 3. Esto es visible en el cambio de la columna "REPLICAS" en el comando kubectl get hpa -w.
- Los nuevos Pods (my-app-75d668c5db-p85zs y my-app-75d668c5db-khgmb) comienzan en estado Pending porque están esperando recursos del clúster (CPU, memoria, etc.) para ser asignados.
- Luego, pasan a ContainerCreating, lo que significa que el contenedor dentro del Pod se está iniciando.
- Finalmente, los nuevos Pods alcanzan el estado Running, lo que indica que están activos y procesando tráfico.
Normalización de la carga:

Una vez que se han lanzado los nuevos Pods, la carga de CPU promedio disminuye, acercándose al 50%, lo que está dentro del objetivo deseado.