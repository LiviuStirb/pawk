# Python AWK

This is a simple python that makes it useful to write awk like script using python. 

Usage examples:

python pawk.py -BEGIN 'sum=0' -END 'print("SUM: ", sum)' -F ";" "if(NR>1):global sum; sum+=int(fields[1])" username 



