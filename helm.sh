# Update Chart.yaml (helm addons charts) and Install the Addons mentioned there with specific versions
helm dependency update path[Chart.yaml]

# Go inside the folder Chart.yaml is in. Then helm dependency update .
# It keeps only addons is included in the Chart.yaml or not
# Since it is update operation, also delete all previous versions 

# ... for installation helm chart ...
helm install release1 ./project_manager



# We can install or upgrade an entire helm chart with our custom values for the resources of 
# .......... Chart.yaml ...........
# helm install or update 


# helm repo add grafana https://grafana.github.io/helm-charts
# helm show values grafana/grafana > grafana-values.yaml

# ----------------------------------------------------------- #
helm install my-releasex ./project_manager \
  -f values.yaml \
  -f ./project_manager/Values/grafana-values.yaml \
  -f ./project_manager/Values/prometheus-values.yaml \
  -f ./project_manager/Values/ingress-nginx-values.yaml 

# Find helm charts in here [https://artifacthub.io/packages/search?kind=0]

# ---- If you want, you can directly add some customization , but through values.yaml is more flexible...
helm install jaeger jaegertracing/jaeger \
  --set provisionDataStore.cassandra=false \
  --set storage.type=elasticsearch \
  --set storage.elasticsearch.host=<HOST> \
  --set storage.elasticsearch.port=<PORT> \
  --set storage.elasticsearch.user=<USER> \
  --set storage.elasticsearch.password=<password>
