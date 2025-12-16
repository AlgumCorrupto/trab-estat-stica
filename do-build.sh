#!/bin/bash

LMKNAME=$(basename $1 .tex)
LMKDIR=$(dirname $0)
mkdir -p build
latexmk $1 -pdf -jobname=$LMKDIR/build/$LMKNAME
