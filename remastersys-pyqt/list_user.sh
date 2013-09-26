#!/bin/bash

# list user names

for LINE in `cat /etc/passwd`
	do
		id=`echo $LINE | cut -d ":" -f3`
		if [ `echo $id | grep '^[[:digit:]]*$'` ]
			then
				if [ "$id" -gt 999 ] && [ "$id" -lt 2000 ]
					then
						name=`echo $LINE | cut -d ":" -f1`
						echo $name
				fi
		else
			continue
		fi
done
