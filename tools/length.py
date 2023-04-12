import csv
import subprocess
import shlex

f = open('parlerdata.csv')
csv_f = csv.reader(f)
with open('myfile.csv', 'w+') as file:
    for row in csv_f:
        url = row[0]
        length = subprocess.check_output(
            shlex.split(
                f"/usr/local/bin/mediainfo '--Inform=Video;%Duration%' {url}"
            )
        )
        print(length)
        file.write(str(length))
