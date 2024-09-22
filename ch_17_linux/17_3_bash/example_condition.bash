#!/bin/bash
echo "start script $0"
echo "read number-> "
read input_num

if [ $input_num -gt 10 ]; then
	echo "number is greater 10"
else
	echo "number is less than or equal to 10"
fi
