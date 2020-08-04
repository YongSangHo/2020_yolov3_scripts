#! /bin/bash
for file in *
do
    if [ ${file: -4} == ".jpg" ]; then
   	 python3 test.py $file
	 cp ${file:0: -4}.txt dim40_${file:0 : -4}.txt
	 
    fi
done
