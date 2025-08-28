#!/bin/bash

FUSION=fusion

# mount fusion
export FUSION_LOG_LEVEL=error
trap '' SIGIO && ${FUSION} --foreground &

# wait till mounted
./healthcheck.sh || exit 1
