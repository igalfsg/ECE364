#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-19 14:58:41 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Lab01/getFinalScores.bash $
#$Revision: 86170 $

if [[ $# != 1 ]]
then
echo "Usage: ./getFinalScores.bash <filename>"
exit 1
fi

if [[ ! -e $1 ]]
then
    printf "Error: reading input file: %s\n" $1
    exit 2
fi
file_n=$(echo $1 | cut -d '.' -f 1)
file_n=$file_n.out
if [[  -e $file_n ]]
then
    printf "Output file %s already exists.\n" $file_n
    exit 3
fi
touch $file_n

while read -r line
do
    nam=$(echo $line | cut  -d ',' -f 1)
    fir=$(echo $line | cut  -d ',' -f 2)
    sec=$(echo $line | cut  -d ',' -f 3)
    thi=$(echo $line | cut  -d ',' -f 4)
    fou=$(echo $line | cut  -d ',' -f 5)
    #echo $fir
    let fir=(15*$fir)/100
    #echo $fir
    let sec=(30*$sec)/100
    let thi=(30*$thi)/100
    let fou=(25*$fou)/100
    let sum=($fir+$sec+$thi+$fou)
    echo "$nam,$sum" >> $file_n
done < $1



exit 0