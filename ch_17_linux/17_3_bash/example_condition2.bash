#!/bin/bash
echo "start script $0"
echo "read number-> "
read input_num

if [ $input_num -gt 0 ] && [ $input_num -le 20 ]; then
        echo "number is between 0 and 20 inclusive"
elif [ $input_num -lt 0 ]; then
	echo "The value is less than zero"
else
        echo "number is greater than 20"
fi
