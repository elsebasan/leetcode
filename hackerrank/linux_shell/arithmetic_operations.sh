#!/bin/bash
read EXPRESION
echo "scale=3; $EXPRESION" | bc
