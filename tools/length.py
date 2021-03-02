import csv
import subprocess
import shlex

f = open('parlerdata.csv')
csv_f = csv.reader(f)
file = open('myfile.csv', 'w+')

for row in csv_f:
    url = row[0]
    length = subprocess.check_output(shlex.split("/usr/local/bin/mediainfo '--Inform=Video;%Duration%' " + url)) # Thanks @Jim Dennis for suggesting the []
    print(length)
    file.write(str(length))

file.close()
