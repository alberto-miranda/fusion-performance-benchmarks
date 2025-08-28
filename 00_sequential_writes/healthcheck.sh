#!/usr/bin/env bash

for _ in {1..5}; do
  if grep fuse.fusion /proc/mounts | grep -q /fusion; then
    exit 0
  else
    sleep 2s
  fi
done
exit 1
