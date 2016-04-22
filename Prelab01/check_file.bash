#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-15 12:55:38 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/check_file.bash $
#$Revision: 85107 $
if [[ $# == 0 ]]
then
echo "Usage: ./check_file.bash <filename>"
exit 0
elif [[ $# != 1 ]]
then
    echo "Wrong Number of arguments given"
    exit 9
fi

if [[ -e $1 ]]
then
    printf "%s exists\n" $1
else
    printf "%s does not exist\n" $1
fi

if [[ -d $1 ]]
then
    printf "%s is a directory\n" $1
else
    printf "%s is not directory\n" $1
fi

if [[ -f $1 ]]
then
    printf "%s is an ordinary file\n" $1
else
    printf "%s is not an ordinary file\n" $1
fi

if [[ -r $1 ]]
then
    printf "%s is readable\n" $1
else
    printf "%s is not readable\n" $1
fi

if [[ -w $1 ]]
then
    printf "%s is writable\n" $1
else
    printf "%s is not writable\n" $1
fi

if [[ -x $1 ]]
then
    printf "%s is executable\n" $1
else
    printf "%s is not executable\n" $1
fi
exit 0