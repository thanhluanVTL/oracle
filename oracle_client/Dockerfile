FROM python:3.9.5-buster

# INSTALL TOOLS
RUN apt-get update \
&& apt-get install -yq --no-install-recommends curl graphviz unzip libaio-dev nano \
&& apt-get clean \
&& mkdir -p /opt/data \
&& rm -rf /var/lib/apt/lists/*

ADD ./oracle-instantclient/ /opt/data
ADD ./install-instantclient.sh /opt/data

WORKDIR /opt/data

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

ENV OCI_HOME=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

# COPY ./pip.conf /etc/pip.conf

# INSTALL INSTANTCLIENT AND DEPENDENCIES
COPY install-instantclient.sh ./install-instantclient.sh
RUN chmod +x ./install-instantclient.sh \
&& ./install-instantclient.sh