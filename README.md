# Big-Data-Toolbox
A microservice-based application that allows users to run Apache Hadoop, Spark, Jupyter Notebooks, SonarQube and SonarScanner without having to install any of them.

## Terminal Application Docker Image
https://hub.docker.com/r/mohanito/big-data-toolbox

## Docker Images
Hadoop: https://hub.docker.com/r/sequenceiq/hadoop-docker \
Spark: https://hub.docker.com/r/bitnami/spark \
Jupyter Notebook: https://hub.docker.com/r/jupyter/base-notebook \
Sonarqube: https://hub.docker.com/_/sonarqube \
SonarScanner: https://hub.docker.com/r/sonarsource/sonar-scanner-cli

## Deploying docker images to GCP and GKE
    docker pull dockerHubId/dockerImage
    docker tag dockerHubId/dockerImage gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version
    docker push gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version

In Container Registry, go to the image and "Deploy to GKE".

## External Endpoints for Kubernetes Services
Jupyter Notebook: http://34.123.215.223:8888
Spark: http://35.224.111.226:8080

## Running Docker images on (local) Kubernetes Engine
1. Install kubernetes and minikube
2. start a cluster by doing:
        `minikube start`
3. Start a server:
        `kubectl create deployment big-data-toolbox --image=mohanito/big-data-toolbox`
4. Expose a service as a NodePort:
        `kubectl expose deployment big-data-toolbox --type=NodePort --port=8080`
5. Run `kubectl get pods` to check deployment status. 

Then, use similar commands to run the other docker container images. \

For checkpoint 1, **screenshot_toolbox.png** shows the main container running on Kubernetes locally. \
**screenshot_containers.png** shows all 5 containers running on Kubernetes locally without any error.

### References:
https://minikube.sigs.k8s.io/docs/handbook/controls/
