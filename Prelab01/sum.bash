#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-13 18:53:28 -0500 (Wed, 13 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/sum.bash $
#$Revision: 84749 $

Num_Of_Param=$#
sum_param=0
while(($# > 0))
do
    let sum_param=$sum_param+$1
    shift
done
echo "$sum_param"
exit 0