# Big-Data-Toolbox
A microservice-based application that allows users to run Apache Hadoop, Spark, Jupyter Notebooks, SonarQube and SonarScanner without having to install any of them.

## Terminal Application Docker Image
https://hub.docker.com/r/mohanito/big-data-toolbox

## Docker Images
Hadoop Namenode: https://hub.docker.com/r/bde2020/hadoop-namenode \
Hadoop Datanode: https://hub.docker.com/r/bde2020/hadoop-datanode \
Spark: https://hub.docker.com/r/bitnami/spark \
Jupyter Notebook: https://hub.docker.com/r/jupyter/base-notebook \
Sonarqube (with SonarScanner installed): https://hub.docker.com/r/mohanito/sonar 

## Deploying docker images to GCP and GKE
    docker pull dockerHubId/dockerImage
    docker tag dockerHubId/dockerImage gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version
    docker push gcr.io/<PROJECT_ID>/dockerHubId/dockerImage:version

In Container Registry, go to the image and "Deploy to GKE".

## External Endpoints for Kubernetes Services
Jupyter Notebook: http://34.123.215.223:8888 \
Spark: http://35.224.111.226:8080 \
Sonarqube: http://34.74.74.68:9000 \
Hadoop: http://34.85.228.99:9870/

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
CLUSTER_NAME=test

CORE_CONF_fs_defaultFS=hdfs://namenode:9000
CORE_CONF_hadoop_http_staticuser_user=root
CORE_CONF_hadoop_proxyuser_hue_hosts=*
CORE_CONF_hadoop_proxyuser_hue_groups=*
CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec

HDFS_CONF_dfs_webhdfs_enabled=true
HDFS_CONF_dfs_permissions_enabled=false
HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
```
https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env \
The Hadoop namenode should be exposed to port 9870 and 9000. \
For the datanode, set SERVICE_PRECONDITION as hadoop-namenode-service:9000, and CORE_CONF_fs_defaultFS as hdfs://hadoop-namenode-service:9000
