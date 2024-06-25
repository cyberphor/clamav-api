# Dockerfile metadata
FROM python:3.11
LABEL Author="Victor Fernandez III, @cyberphor"

# install dependencies 
RUN apt-get update && \
    apt-get install -y clamav clamav-daemon &&\
    python -m pip install fastapi uvicorn opentelemetry-instrumentation-fastapi

# copy files needed to run ClamAV and the API
COPY clamd.conf /etc/clamav/clamd.conf
COPY api.py api.py
COPY entrypoint.sh entrypoint.sh

# set permissions and update the ClamAV database
RUN mkdir /var/run/clamav &&\
    chown -R clamav:clamav /var/run/clamav &&\    
    chown -R clamav:clamav /var/lib/clamav &&\
    chmod u+x entrypoint.sh &&\
    freshclam

# start the container as the ClamAV service account (a non-root user)
USER clamav
CMD [ "./entrypoint.sh" ]