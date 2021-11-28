FROM sonarqube:8.9-community
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip && \
    unzip sonar-scanner-cli-4.0.0.1744.zip
ENV PATH $PATH:/opt/sonarqube/sonar-scanner-4.0.0.1744/bin
RUN echo "export PATH=$PATH:/opt/sonarqube/sonar-scanner-4.0.0.1744/bin" >> /root/.bashrc
