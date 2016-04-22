#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-14 15:24:51 -0500 (Thu, 14 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/exist.bash $
#$Revision: 85011 $

while(($# > 0))
do
    if [[ -r $1 ]]
then
printf "File %s is readable!\n" $1
elif [[ ! -e $1 ]]
then
touch $1

fi
    shift
done


exit 0