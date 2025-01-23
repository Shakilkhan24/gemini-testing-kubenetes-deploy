# Project Manager Helm Chart

## Overview

The Project Manager Helm Chart is designed to deploy the Project Manager application efficiently using Helm. The `Chart.yaml` file specifies all dependencies for various addons and their respective versions, ensuring streamlined configuration and installation.

---

## Prerequisites

Before deploying, ensure the following:

- A running Kubernetes cluster (minimum 1 node).
- Helm installed on your local machine.
- Google API Key configured in the `values.yaml` file.

---

## Installation Steps

### 1. Configure Google API Key

Add your Google API key in the `values.yaml` file under the `google` section:

```yaml
data:
  GOOGLE_API_KEY: "your-google-api-key-here"  
```

> Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual Google API key.

---

### 2. Update Dependencies

To update the dependencies specified in the `Chart.yaml` file:

1. Navigate to the directory containing the `Chart.yaml` file.
2. Run the following command:

   ```sh
   helm dependency update ./project_manager
   ```

This will download and update all the addons listed in the `Chart.yaml` file.

---

### 3. Install the Chart

Once dependencies are updated, install the Helm chart:

1. Navigate to the directory containing the `Chart.yaml` file.
2. Run the following command:

   ```sh
   helm install release1 ./project_manager
   ```

---

### 4. Start and Access the Cluster

After deployment, access the Project Manager application:

1. Retrieve the exposed port for the service:

   ```sh
   kubectl get svc release1-gemini-service -o jsonpath="{.spec.ports[0].nodePort}"
   ```

2. Open your web browser and navigate to the application:

   - Localhost: `http://localhost:30001`
   - Node IP: `http://<your-node-ip>:30001`

---

## Remember

If you customize `values.yaml` or add specific configurations for addons, include the respective values files during installation. For example:

```sh
helm install my-releasex ./project_manager \
  -f values.yaml \
  -f ./project_manager/Values/grafana-values.yaml \
  -f ./project_manager/Values/prometheus-values.yaml \
  -f ./project_manager/Values/ingress-nginx-values.yaml
```

---

## Notes

- Ensure all required dependencies and configurations are properly set up in the `values.yaml` file before installation.
- Always update the dependencies using `helm dependency update` after modifying `Chart.yaml`.

With these steps, you can successfully deploy and access the Project Manager application using Helm. Enjoy managing your projects efficiently!

