#! /bin/bash
#$Author: ee364a05 $
#$Date: 2016-01-22 19:03:47 -0500 (Fri, 22 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a05/Prelab02/run.bash $
#$Revision: 86514 $

if [[ $# != 2 ]]
then
    echo "Wrong Number of arguments given"
    exit 9
fi
gcc $1 -o quick_sim
if [[ $? != 0 ]]
then
echo "error: " $1 "could not be compiled!"
exit 5
fi
min=99999999

if [[ -e $2 ]]
then
    echo $2 "exists. Whould you like to delete it? (y/n)"
    read respuesta
    if [[ $respuesta == "y" || $respuesta == "yes" ]]
    then
	#echo yay
	dest=$2
	rm $dest
	touch $dest
    else
	echo "Enter a new filename:"
	read respuesta
	dest=$respuesta
	touch $dest
    fi
else
    dest=$2
    touch $dest
fi

types=(1 2 4 8 16 32)
for (( I=0; I < ${#types[*]}; I++ ))
do
    
    for (( k=0; k < 5; k++ ))
do
    amd="$(quick_sim ${types[I]} ${types[k]} a)"
    nam=$(echo $amd | cut  -d ':' -f 2)
    cach=$(echo $amd | cut  -d ':' -f 4)
    issu=$(echo $amd | cut  -d ':' -f 6)
    resu=$(echo $amd | cut  -d ':' -f 8)
    ttim=$(echo $amd | cut  -d ':' -f 10)
    echo "$nam:$cach:$issu:$resu:$ttim" >> $dest
    if (( $min > $ttim ))
    then
	min=$ttim
	mnam=$nam
	mcach=$cach
	missu=$issu
    fi
    intel="$(quick_sim ${types[I]} ${types[k]} i)"
    nam=$(echo $intel | cut  -d ':' -f 2)
    cach=$(echo $intel | cut  -d ':' -f 4)
    issu=$(echo $intel | cut  -d ':' -f 6)
    resu=$(echo $intel | cut  -d ':' -f 8)
    ttim=$(echo $intel | cut  -d ':' -f 10)
    echo "$nam:$cach:$issu:$resu:$ttim" >> $dest
    if (( $min > $ttim ))
    then
	min=$ttim
	mnam=$nam
	mcach=$cach
	missu=$issu
    fi
done
done
echo "Fastest run time achieved by $mnam with cache size $mcach and issue width $missu was $min"
exit 0