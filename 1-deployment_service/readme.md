Para iniciar nuestro cluster ejecutamos `kind create cluster`

probemos que todo funcione con `kubectl get po -A`

Después de crear nuestros archivos de configuración corremos

- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`


Debido a que Kind utiliza un contenedor Docker para el clúster, deberás usar kubectl port-forward para acceder a los servicios desde el navegador, o configurar un Ingress. Por ejemplo:

`kubectl port-forward service/nginx-service 8080:80`

Esto reenviará el puerto 80 del servicio nginx-service al puerto 8080 de tu máquina local, permitiéndote acceder a la aplicación en `http://localhost:8080.`

Para el diagnóstico de problemas con los pods:

1. `kubectl get po -A` para ver todos los pods y me di cuenta que había uno en estado **ContainerCreating**
2. `kubectl describe pod nginx-deployment-576c6b7b6-qqvhk` con este comando vi el detalle del pod y encontré que al final aparecía **Pulling image "nginx:latest**

---

Para detener el cluster corremos `kind delete cluster`
