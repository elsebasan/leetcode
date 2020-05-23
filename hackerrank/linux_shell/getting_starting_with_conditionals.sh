#!/bin/bash

read CHAR
re='y|Y'
re2='n|N'
if [[ "$CHAR" =~ $re ]]
then 
   echo "YES"
elif [[ "$CHAR" =~ $re2 ]]
then
   echo "NO" 
fi
