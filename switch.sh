for file in *
do
    if [ ${file: -4} == ".txt" ]; then
   	 python3 switch.py $file
    fi
done
