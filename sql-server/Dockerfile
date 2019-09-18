FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y supervisor \
                       fakechroot \
                       locales \
                       iptables \
                       sudo \
                       wget \
                       curl \
                       zip \
                       unzip \
                       make \ 
                       bzip2 \ 
                       m4 \
                       apt-transport-https \
                       tzdata \
                       libnuma-dev \
                       libsss-nss-idmap-dev \
                       software-properties-common 

RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add - && \
    add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-preview.list)" && \
    apt-get update && \
    apt-get install -y mssql-server && \
    apt-get install -y mssql-mlservices-packages-r  mssql-mlservices-packages-py
RUN opt/mssql/bin/checkinstallextensibility.sh && \
    chown -R root:root /opt/mssql/bin/launchpadd && \
    chown -R root:root /opt/mssql/bin/setnetbr && \
    mkdir -p /var/opt/mssql-extensibility/data && \
    mkdir -p /var/opt/mssql-extensibility/log
    
RUN apt-get clean && rm -rf /var/apt/cache/* /tmp/* /var/tmp/*

COPY ./supervisord.conf /usr/local/etc/supervisord.conf

RUN locale-gen en_US.UTF-8

EXPOSE 1433

CMD /usr/bin/supervisord -n -c /usr/local/etc/supervisord.conf