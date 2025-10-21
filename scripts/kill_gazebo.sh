#!/bin/bash

pids=$(ps aux | grep -E "[i]gn|[g]z" | awk "{print \$2}"); [ -n "$pids" ] && echo "$pids" | xargs sudo kill -9