#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-22 19:04:25 -0500 (Fri, 22 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab02/yards.bash $
#$Revision: 86515 $

sumlin=0;
avg=0
max=0
while read -r line
do
    var=0
    sumlin=0
    arrayuno=($line)
    for (( I=1; I < ${#arrayuno[*]}; I++ ))
    do
	let sumlin=$sumlin+${arrayuno[I]}
	#echo yardds ${arrayuno[I]}
    done
    let den=${#arrayuno[*]}-1
    let avg=$sumlin/den
    mul=0
    for (( I=1; I < ${#arrayuno[*]}; I++ ))
    do
	let mul=${arrayuno[I]}-$avg
	let mul=$mul*$mul
	let var=$var+$mul
    done
     if (( $avg > $max ))
     then
	 max=$avg
     fi
    let var=$var/den
    echo ${arrayuno[0]} schools averaged $avg yards recieving with a variance of $var
done < "stats.txt"
echo The largest average yardage was $max

