## Parte 1

Instalar helm. Esta herramienta es la luz, ya que facilita la vida cuando necesitamos instalar algo que tiene muchos componentes separados. En este caso prometheus + grafana son **dos piezas separadas** que funcionan en conjunto, la primera se encarga de recolectar métricas de nuestro cluster y ofrecer una interfaz de consultas, y la otra se encarga de tomar las métricas y mostrar gráficos interactivos, dashboards etc.

Entonces helm nos permite **utilizar configuraciones que otras personas ya hicieron** y que funcionan bien, de lo contrario tendríamos que instalar todo desde cero. Por ejemplo, crear un deployment para prometheus y otro para grafana, crear configMaps para cada uno, services, almacenamiento persistente, también comincar ambos etc. Todo eso es difícil, pero al ser algo tan común el helm ya tiene todo listo y creará los recursos funcionales en nuestro cluster. Así que

- `choco install kubernetes-helm` en Windows
- `helm version`


## Parte 2

1. kind create cluster --name prometheus-cluster
2. Agregamos el repositorio de helm charts de prometheus con `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
3. helm repo update
4. kubectl create namespace monitoring
5. Instalamos un helm chart específico del repositorio que agregamos en el paso 2. `helm upgrade --install prom prometheus-community/kube-prometheus-stack -n monitoring --values values.yaml`
    - **prom**: es el nombre de nuestro release
    - **prometheus-community/kube-prometheus-stack**: indica que el chart kube-prometheus-stack se encuentra en el repositorio prometheus-community
6. Verificamos que todos los pods suban y todo funcione `kubectl get all -n monitoring`
7. Hacemos un par de port forwarding para poder acceder a las UI de prometheus y grafana.
   1. kubectl port-forward service/prometheus-operated -n monitoring 9090:9090
   2. kubectl port-forward service/prom-grafana -n monitoring 3000:80

## Parte 3

Finalmente vamos a recolectar algunas métricas y crear un dasboard básico. Para esto nos remitiremos al comando de **stress** para evidenciar gráficamente el uso de CPU de nuestros pods. Así que utilizaremos el `cluster/deployment.yml` y realizaremos


1. `kubectl exec -it $(kubectl get pods -l app=demo-app -n monitoring -o jsonpath='{.items[0].metadata.name}') -n monitoring -- /bin/bash`
2. `apt-get update && apt-get install -y stress`
3. `stress --cpu 4`

Podemos correr la query en prometheus 

- rate(container_cpu_usage_seconds_total{namespace="monitoring", pod=~"demo-deployment-.*"}[5m])

Y ver el gráfico que creamos en grafana, evidenciando el consumo de CPU. Para esto importaremos el archivo json el cual crea automáticamente el dashboard en grafana 🙂
