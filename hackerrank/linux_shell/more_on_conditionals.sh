#!/bin/bash

read X
read Y
read Z
if [ "$X" -eq "$Y" ] && [ "$X" -eq "$Z" ]
then
    echo "EQUILATERAL"
elif [ ! "$X" -eq "$Y" ] && [ ! "$Y" -eq "$Z" ] && [ ! "$Z" -eq "$X" ]
then 
    echo "SCALENE"
else
    echo "ISOSCELES"
fi
