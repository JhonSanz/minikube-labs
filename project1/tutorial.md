Para iniciar nuestro cluster corremos `minikube start --driver=docker` y esto creará un contenedor de docker. Hay mas configuraciones, pero para efectos prácticos esta es la mas facil.

podemos acceder a `minikube dashboard` para tener una interfaz gráfica bonita, pero lo ideal es manejar todo desde `kubectl`

Después de crear nuestros archivos de configuración corremos

- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`


esto funciona, sin embargo debido a las limitaciones de red de correr minikube con docker es necesario hacer un port-forwarding `kubectl port-forward service/nginx-service 8080:80` o bien correr `minikube service nginx-service` para poder acceder mediante nuestro navegador. De todos modos exiten opciones como crear un ingress, lo cual exploraremos mas adelante

---

Para detener el cluster corremos `minikube stop` y luego `minikube delete`


minikube start --driver=virtualbox