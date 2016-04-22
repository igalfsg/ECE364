#! /bin/bash
#$Author$
#$Date$
#$HeadURL$
#$Revision$


#declare empty array
arr=()

#supress output 
scriptname &>/dev/null

#convert the variable to an array 
C="A B A C A CA"
array=($C)
