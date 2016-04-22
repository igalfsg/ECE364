#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-19 14:58:41 -0500 (Tue, 19 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Lab01/getCourseStats.bash $
#$Revision: 86170 $

if [[ $# != 1 ]]
then
echo "Usage: ./getCourseStats.bash <course name>"
exit 1
fi

if [[ $1 == "ece364" || $1 == "ece337" || $1 == "ece468" ]]
then

for var in $(ls gradebooks/$1*.txt)
do
getFinalScores.bash $var
if [[ $? != 0 ]]
then
echo Error while running getFinalScores.bash
exit 3
fi
done
max=0
sum=0
count=0

for var in $(ls gradebooks/$1*.out)
do
while read -r line
do
    nam=$(echo $line | cut  -d ',' -f 1)
    fir=$(echo $line | cut  -d ',' -f 2)
    let sum=($fir+$sum)
   if (( $fir > $max ))
   then
       max=$fir
       nombre=$nam
   fi
   let count=($count + 1)
done < $var
done
let total=$sum/$count
echo Total students: $count
echo Average score: $total
echo $nombre had the highest score of $max 
exit 0
else 
echo "Error: course $1 is not a valid option."
exit 5
fi