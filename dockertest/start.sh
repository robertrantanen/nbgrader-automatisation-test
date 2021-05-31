#!/bin/sh

(curl --silent --retry 30 --retry-delay 1 --retry-connrefused \
http://localhost:8888 ; \
python3 -m webbrowser http://localhost:8888) &

docker run -p 8888:8888 -v $(pwd):/work jupyter
