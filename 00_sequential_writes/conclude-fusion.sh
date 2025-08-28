#!/bin/bash

# forcefully kill fusion because we don't want to measure synchronization time
pkill -KILL -f dist/fusion || true
fusermount -u /fusion || true
