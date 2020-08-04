for file in *
do
	if [ ${file:0:4} == "ratio" -o ${file:0:7} == "resized" ]; then 
		if [ ${file: -4} == ".jpg" ]; then
			 python3 rgb.py  $file
		fi
	fi
done
