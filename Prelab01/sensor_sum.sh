#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-15 17:24:44 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/sensor_sum.sh $
#$Revision: 85137 $

if [[ $# == 0 ]]
then
echo "Usage: ./sensor_sum.sh <filename>"
exit 0
elif [[ $# != 1 ]]
then
    echo "Wrong Number of arguments given"
    exit 9
fi

if [[ ! -r $1 ]]
then
    printf "error: %s is not a readable file!\n" $1
fi

while read -r line
do
    sen=$(echo $line | cut  -d '-' -f 1)
    fir=$(echo $line | cut  -d ' ' -f 2)
    sec=$(echo $line | cut  -d ' ' -f 3)
    thi=$(echo $line | cut  -d ' ' -f 4)
    let sum=($fir+$sec+$thi)
    printf "%s %d\n" $sen $sum
done < $1