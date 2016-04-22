#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-02-16 14:52:04 -0500 (Tue, 16 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Lab05/scheduler.bash $
#$Revision: 88217 $

if [[ $# != 1 ]]
then
    echo "wrong number of inputs please put only 1 input"
    exit 1
fi
if [[ ! -e $1 ]]
then
    echo "Error: $1 does not exist."
    exit 2
fi
if [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable."
    exit 2
fi

if [[  -e schedule.out ]]
then
    echo "Error: schedule.out does exist."
    exit 3
fi

while read -r line
do
    nam=$(echo $line | cut  -d ' ' -f 1)
    
done < $1

exit 0