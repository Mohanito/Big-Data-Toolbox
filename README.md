<h1 align="center">
  Big-Data-Toolbox
</h1>
<p align="center">
  A microservice-based application that allows users to run Apache Hadoop, Spark, Jupyter Notebooks, SonarQube and SonarScanner without having to install any of them.
</p>
<p align="center">
  http://34.74.245.70:3000
</p>

## Video Code Walkthrough & Demo
https://cmu.box.com/s/pfc8jdz86unpm12ixead72qvq0x0j1wf

## Usage
The project is deployed on Kubernetes Engine on Google Cloud Platform. You may visit the service endpoint at http://34.74.245.70:3000.

## Structure
| Files      | Description |
| ----------- | ----------- |
| archive | Files used for project checkpoint, including a command-line interface |
| hadoop   | Link to Docker images and environment variables used for deploying Hadoop |
| jupyter   | Link to the Docker image used for deploying Jupyter Notebook  |
| screenshots | Screenshots of GCP Kubernetes Engine and exposed services |
| sonar | Dockerfile used to build a custom image of SonarQube with SonarScanner installed |
| spark   | Link to the Docker image used for deploying Spark |
| Dockerfile   | Dockerfile used for building the node.js based user interface |
| index.html   | Main webpage for the user interface |
| server.js   | An express.js server for the user interface |

## Docker Images
User Interface: https://hub.docker.com/r/mohanito/big-data-toolbox \
Hadoop Namenode: https://hub.docker.com/r/bde2020/hadoop-namenode \
Hadoop Datanode: https://hub.docker.com/r/bde2020/hadoop-datanode \
Spark: https://hub.docker.com/r/bitnami/spark \
Jupyter Notebook: https://hub.docker.com/r/jupyter/base-notebook \
Sonarqube (with SonarScanner installed): https://hub.docker.com/r/mohanito/sonar 

## External Endpoints for Kubernetes Services
User Interface: http://34.74.245.70:3000 \
Jupyter Notebook: http://34.123.215.223:8888 \
Spark: http://35.224.111.226:8080 \
Sonarqube: http://34.74.74.68:9000 \
Hadoop: http://34.85.228.99:9870

## Deploying docker images to GCP and GKE
In Container Registry:
    docker pull dockerHubId/dockerImage
    docker tag dockerHubId/dockerImage gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version
    docker push gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version
Then find the image and "Deploy to GKE".

## Installing SonarScanner in the official SonarQube image
Build an image with a Dockerfile containing:
```
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip && \
unzip sonar-scanner-cli-4.0.0.1744.zip
ENV PATH $PATH:/opt/sonarqube/sonar-scanner-4.0.0.1744/bin
RUN echo "export PATH=$PATH:/opt/sonarqube/sonar-scanner-4.0.0.1744/bin" >> /root/.bashrc
```
This downloads SonarScanner, unzips the file, and adds the directory to the PATH environment variable. \
Reference: https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/ 

## Environment Variables for Deploying Hadoop on GKE
```
CLUSTER_NAME=test (for namenode only)

CORE_CONF_fs_defaultFS=hdfs://namenode:9000
CORE_CONF_hadoop_http_staticuser_user=root
CORE_CONF_hadoop_proxyuser_hue_hosts=*
CORE_CONF_hadoop_proxyuser_hue_groups=*
CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec

HDFS_CONF_dfs_webhdfs_enabled=true
HDFS_CONF_dfs_permissions_enabled=false
HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
```
Reference: \
https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env \
https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml \
The Hadoop namenode should be exposed to port 9870 and 9000. \
For the datanode, set SERVICE_PRECONDITION as hadoop-namenode-service:9000, and CORE_CONF_fs_defaultFS as hdfs://hadoop-namenode-service:9000. In this project, it is hardcoded as 34.85.228.99:9000 (namenode endpoint).

## Preview
#### Graphical User Interface
![GUI Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/User_interface.png)
#### Hadoop
![Hadoop Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/Hadoop_datanode.png)
#### Spark
![Spark Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/Spark.png)
#### Jupyter Notebook
![Jupyter Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/Jupyter_notebook.png)
#### SonarQube with SonarScanner
![Sonar Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/SonarQube.png)
#### Kubernetes Engine Workloads
![GKE Image](https://github.com/Mohanito/Big-Data-Toolbox/blob/main/screenshots/GKE_workloads.png)
