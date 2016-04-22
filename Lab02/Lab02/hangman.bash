#! /bin/bash
#$Author$
#$Date$
#$HeadURL$
#$Revision$

let val=$RANDOMM%3
game=0
ati=0
if [[ $val == 0 ]]
then
word=(b a n a n a)
guess=(. . . . . .)
final="banana"
elif [[ $val == 1 ]]
then
word=(p a r s i m o n i o u s)
guess=(. . . . . . . . . . . .)
final="parasimonious"
else
word=(s e s q u i p e d a l i a n)
guess=(. . . . . . . . . . . . . .)
final="sesquipedalian"
fi
echo Your word is ${#word[*]} letters long.
while (( $game != 1 ))
do
    echo word is: ${guess[*]}
    echo -n Make a guess:
    read adivina
    for (( I=0; I < ${#word[*]}; I++ ))
    do
	if [[ $adivina == ${word[I]} ]] 
	then
	    guess[I]=$adivina
	    ati=1
	fi
    done
    if [[ $ati == 1 ]]
    then
	echo good going!
	ati=0
    else
	echo sorry try again.
    fi
    for (( I=0; I < ${#word[*]}; I++ ))
    do
	if [[ ${guess[I]} == "." ]] 
	then
	    falta=1
	fi
    done
    if [[ $falta == 0 ]] 
    then
	echo congratulations! you guessed the word: $final
	exit 0
    fi
    falta=0
done
 