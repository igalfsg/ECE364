#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-14 16:06:27 -0500 (Thu, 14 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/line_num.bash $
#$Revision: 85018 $

sum=0

if [[ $# != 1 ]]
then
    echo "Wrong Number of arguments given"
    exit 9
fi

if [[ ! -r $1 ]]
then
    printf "Cannot read %s\n" $1
    exit 9
fi

while read -r
do
    let sum=$sum+1
    printf "%d:%s\n" $sum  "$REPLY"
done < $1

exit 0