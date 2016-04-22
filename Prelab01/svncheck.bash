#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-18 14:42:06 -0500 (Mon, 18 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab01/svncheck.bash $
#$Revision: 85542 $

if [[ $# != 0 ]]
then
    echo "Wrong Number of arguments given"
    exit 9
fi
exec 3<file_list
while read line <&3
do

    nombre=$(svn status $line | head -c 1)
   # printf "%s \n" $line

    if [[ $nombre == "" ]]
    then
#is in svn (file might not exist
	if [[ -e $line ]]
	then
	    if [[ ! -x $line ]]
	    then
		svn propset svn:executable ON $line
	    fi
	else
	    printf "Error: File %s appears to not exist here or on svn. \n" $line
	fi
    elif [[ $nombre == "?" ]]
    then
	if [[ -e $line ]]
	then
	    if [[ ! -x $line ]]
	    then
		echo "Do you want us to add it for you? (y/n)"
		read respuesta
		if [ $respuesta == "y" || $respuesta == "y"]
		then
		    chmod +x $line
		fi
	    fi
	    svn add $line
	else
	    printf "Error: File %s appears to not exist here or on svn. \n" $line
	fi
    fi

done 

svn commit -m "Auto-committing code"