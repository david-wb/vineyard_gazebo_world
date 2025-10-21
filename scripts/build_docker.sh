#!/bin/bash

DIR=$(dirname "$0")
cd $DIR/..

docker build -t exxact_traxx:latest .