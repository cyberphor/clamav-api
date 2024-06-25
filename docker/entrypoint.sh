#!/bin/bash

# start ClamAV
clamd 
tail -f /var/log/clamav/clamav.log &

# start the API
python -m uvicorn api:app --host 0.0.0.0 --port 8000