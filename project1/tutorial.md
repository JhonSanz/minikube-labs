Para iniciar nuestro cluster corremos `minikube start --driver=docker` y esto creará un contenedor de docker. Hay mas configuraciones, por ejuemplo es posible utilizar el driver virtualbox `minikube start --driver=virtualbox --no-vtx-check`

probemos que todo funcione con `kubectl get po -A`

podemos acceder a `minikube dashboard` para tener una interfaz gráfica bonita, pero lo ideal es manejar todo desde `kubectl`

Después de crear nuestros archivos de configuración corremos

- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`


esto funciona, sin embargo debido a las limitaciones de red de correr minikube con docker es necesario hacer un port-forwarding `kubectl port-forward service/nginx-service 8080:80` o bien correr `minikube service nginx-service` para poder acceder mediante nuestro navegador. De todos modos exiten opciones como crear un ingress, lo cual exploraremos mas adelante

En este punto estoy corriendo con el dirver de virtualbox y tuve un inconveniente de red entocnes corrí 

1. `kubectl get po -A` para ver todos los pods y me di cuenta que había uno en estado **ContainerCreating**
2. `kubectl describe pod nginx-deployment-576c6b7b6-qqvhk` con este comando vi el detalle del pod y encontré que al final aparecía **Pulling image "nginx:latest**
3. Por lo cual dudé de si mi VM tenía acceso a internet y corrí `minikube ssh` y luego `curl -I https://registry.hub.docker.com` para ver si respondía y obtuve 200, entonces me di cuenta que era tema de velocidad en la conexión
4. Finalmente corrí `kubectl get po -A` y estaba en **STATUS running**

ahora que todo está arriba lo que hay que hacer es 
1. `minikube ip` para obtener la IP de nuestro cluster
2. Acceder al navegador con la anterior IP y el puerto de nuestro servicio `http://192.168.59.100:30008`

---

Para detener el cluster corremos `minikube stop` y luego `minikube delete`


minikube start --driver=virtualbox