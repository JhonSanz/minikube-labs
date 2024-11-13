El objetivo de este laboratorio es hacer consciencia de los rollback que se pueden ejecutar con los deployment. Para ello

1. Aplicamos el archivo `kubectl apply -f deployment_v1.yml` con una versión cualquiera de nginx (descomentamos una de las lineas en el archivo)
2. Verificamos que todo se haya creado correctamente `kubectl get deployments`, y vemos también los pods `kubectl get pods`
3. Para ver el historial de versiones ejecutamos `kubectl rollout history deployment/nginx-deployment` y veremos que solo hay una revisión
```
REVISION  CHANGE-CAUSE
1         <none>
```
4. Ahora viene lo interesante, modificaremos el archivo `deployment_v1.yml` descomentando la linea que tiene la versión `nginx:latest`. Otra cosa muy importante es agregar `kubernetes.io/change-cause: "Updated image to nginx:latest"` para que quede registrado un mensaje de ayuda para saber que fue lo que hicimos
5. Y aplicamos el mismo archivo con el mismo comando `kubectl apply -f deployment_v1.yml`
6. Como se aplicó el mismo archivo kubernetes hará el rolling update. Verifiquemos de nuevo que todo esté creado correctamente
7. Ahora vamos al historial de versiones de nuevo y vemos que se creó una revisión nueva con el mensaje que configuramos en el archivo de deployment.
```
REVISION  CHANGE-CAUSE
1         <none>
2         Updated image to nginx:latest
```

Ahora **vamos a realizar el rollback** a la revisión anterior, asi que:

1. ejecutamos `kubectl rollout undo deployment/nginx-deployment`
2. verificamos que todo esté corriendo `kubectl get deployments`, `kubectl get pods`
3. y vemos de nuevo el historial `kubectl rollout history deployment/nginx-deployment`
```
REVISION  CHANGE-CAUSE
2         Updated image to nginx:latest
3         <none>
```

Aqui podemos observar varias cosas:

1. La versión actual del deployment es la última que aparece en la lista
2. a medida que vamos haciendo cambios estos quedan registrados y podremos volver a una revisión en específico con la bandera **--to-revision** asi: `kubectl rollout undo deployment/nginx-deployment --to-revision=3`

finalmente ejecutamos `kubectl rollout status deployment/nginx-deployment` para ver detalles del rollback