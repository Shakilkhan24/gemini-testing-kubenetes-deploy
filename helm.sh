# Update Chart.yaml (helm addons charts) and Install the Addons mentioned there with specific versions
helm dependency update path[Chart.yaml]

# Go inside the folder Chart.yaml is in. Then helm dependency update .
# It keeps only addons is included in the Chart.yaml or not
# Since it is update operation, also delete all previous versions 
