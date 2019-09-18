FROM ubuntu:16.04

ENV MLSERVER_VERSION=9.4.7
ENV MICROSOFT_KEYS=52E16F86FEE04B979B07E28DB02C46DF417A0893

RUN apt-get -y update && \
    apt-get install -y fakechroot sudo apt-transport-https wget curl lsb-release python vim jq tzdata iptables software-properties-common && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/azure-cli.list && \
    wget https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb && \
    dpkg -i /tmp/packages-microsoft-prod.deb && rm -f /tmp/packages-microsoft-prod.deb && \
    apt-key adv --keyserver packages.microsoft.com --recv-keys $MICROSOFT_KEYS && \
    apt-get -y update && \
    apt-get install -y microsoft-mlserver-all-$MLSERVER_VERSION && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    /opt/microsoft/mlserver/$MLSERVER_VERSION/bin/R/activate.sh -a -l

COPY config_web_node.py /
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]
