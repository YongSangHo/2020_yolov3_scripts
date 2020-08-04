for file in *
do
    if [ ${file: -4} == ".jpg" ]; then
        python3 resize.py $file ${file:0:-4}.txt
	
    fi
done
