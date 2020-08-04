for file in *
do
    if [ ${file: -4} == ".jpg" ]; then
   	 python3 reflection.py  $file ${file:0:-4}.txt
	 cp ${file:0 : -4}.txt reflection_${file:0 : -4}.txt
    fi
done
