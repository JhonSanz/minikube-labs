como ya tenía servicios creados del ejercicio project1 debo borrar esas cosas que creé, entonces

1. Ver los elementos de mi cluster con `kubectl get all --all-namespaces`. Aquí me mostrará todo, entonces es importante tener en cuenta que hay recursos creados por kubernetes para su funcionamiento y por lo tanto debo identificar lo que realmente queremos administrar
2. Retomando el ejercicio anterior creamos un **deployment y un service** entonces `kubectl get deployment` y `kubectl get svc` funcionarán
3. Ahora solo basta con eliminar ambos con `kubectl delete deployment nginx-deployment` y `kubectl delete service nginx-service`
