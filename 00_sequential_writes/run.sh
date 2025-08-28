#!/bin/bash

TIMESTAMP=$(date +%s)

hyperfine \
    --parameter-list FS fusion,ext4 \
    --parameter-list TX 512,1048576 \
    --command-name 'fs={FS},tx={TX}' \
    --setup ./conclude-fusion.sh \
    --cleanup ./conclude-fusion.sh \
    --prepare ./prepare-{FS}.sh \
    --conclude ./conclude-{FS}.sh \
    --export-markdown ./results/bench-${TIMESTAMP}.md \
    './test.py --keep --transfer-size {TX} /{FS}/s3/fusion-develop/scratch/amiranda/bugs/toomanytruncates/data_${TIMESTAMP}.bin'

