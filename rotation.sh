for file in *
do
    if [ ${file: -4} == ".jpg" ]; then
   	 python3 rotate.py -i  $file -a 90
    fi
done
