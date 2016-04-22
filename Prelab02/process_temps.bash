#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-23 15:24:04 -0500 (Sat, 23 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab02/process_temps.bash $
#$Revision: 86537 $

if [[ $# != 1 ]]
then
    echo "Usage: process_temp.bash <input file>"
    exit 1
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi
while read -r line
do
    array=($line)
    if [[ ${array[0]} != "time" ]]
    then
	sum=0
	tamano=${#array[*]}
	for (( k=1; k < $tamano; k++ ))
	do
	    let sum=$sum+${array[k]}
	done	
	let tamano=$tamano-1
	let avg=$sum/$tamano
	echo Average temperature for time ${array[0]} was $avg C.
    fi
done < $1
exit 0