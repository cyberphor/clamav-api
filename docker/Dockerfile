# Dockerfile metadata
FROM python:3.11
LABEL Author="Victor Fernandez III, @cyberphor"

# install ClamAV
RUN apt-get update && \
    apt-get install -y clamav clamav-daemon

# copy the ClamAV configuration file
COPY clamd.conf /etc/clamav/clamd.conf

# set permissions on ClamAV directories
WORKDIR /var/run/clamav
COPY api.py api.py
COPY entrypoint.sh entrypoint.sh
RUN chown -R clamav:clamav /var/run/clamav &&\
    chown -R clamav:clamav /var/lib/clamav &&\
    chmod ug+x entrypoint.sh

# install the API's Python dependencies
RUN python -m pip install fastapi uvicorn opentelemetry-instrumentation-fastapi

# update the ClamAV signature database
RUN freshclam

# start the container
CMD [ "./entrypoint.sh" ]