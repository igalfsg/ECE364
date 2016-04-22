#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-31 10:43:50 -0500 (Sun, 31 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Lab02/printUsageStats.bash $
#$Revision: 87323 $
if [[ $# != 1 ]]
then
    echo "Usage: printUsageStats.bash <input file>"
    exit 1
fi
if [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist."
    exit 2
fi
count=0
nam=$(head -n 1 $1 | cut  -d ' ' -f 1)
tim=$(head -n 1 $1 | cut  -d ' ' -f 3)
usr=$(head -n 1 $1 | cut  -d ' ' -f 8)
echo "Parshing file $1. Timestamp: $tim"
echo Your choices are:
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N Highest mem usages"
echo "4) Top 3 longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"
echo -n "Please enter your choice:" 
read choice

if [[ $choice == "1" ]]
then 
    echo Total number of active user Ids: $usr
elif [[ $choice == "2" ]]
then
    echo -n "Enter a value for N: " 
    read numb
    count=0;
    let hn=$numb+7
    let numb=$numb
    #result=$
    users=$(head -n $hn $1 | tail -n $numb | cut  -d ' ' -f 2)
    array_user=($users)
    cp=$(head -n $hn $1 | tail -n $numb | cut  -d ' ' -f 9)
    array_cp=($cp)
    for (( I=0; I < ${#array_cp[*]}; I++ ))
    do
	echo "User ${array_user[I]} is utilizing CPU resources at ${array_cp[I]}%"
    done
elif [[ $choice == "3" ]]
then
    echo -n "Enter a value for N: " 
    read numb
    sort_m=($(tail -n +8 $1 | sort -k10 -r -n | head -n $numb | cut  -d ' ' -f 2))
    sort_pm=($(tail -n +8 $1 | sort -k10 -r -n | head -n $numb | cut  -d ' ' -f 10))
    for (( I=0; I < ${#sort_m[*]}; I++ ))
    do
	echo "User ${sort_m[I]} is utilizing mem resources at ${sort_pm[I]}%"
    done
elif [[ $choice == "4" ]]
then
    sort_m=($(tail -n +8 $1 | sort -k11 -r -n | head -n 3 | cut  -d ' ' -f 1))
    sort_pm=($(tail -n +8 $1 | sort -k11 -r -n | head -n 3 | cut  -d ' ' -f 12))
    for (( I=0; I < ${#sort_m[*]}; I++ ))
    do
	echo "PID: ${sort_m[I]} cmd: ${sort_pm[I]}"
    done
elif [[ $choice == "5" ]]
then
    echo -n "Please enter a Valid username: " 
    read uname
    cpup=($(grep $uname $1 | cut  -d ' ' -f 9))
    proc=($(grep $uname $1 | cut  -d ' ' -f 12))
    if [[ ${#cpup[*]} == 0 ]]
    then
	echo No match found
	exit 0
    fi
     for (( I=0; I < ${#cpup[*]}; I++ ))
    do
	echo "${cpup[I]} ${proc[I]}"
    done
else
exit 0
fi
