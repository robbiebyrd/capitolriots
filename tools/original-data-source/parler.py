from bs4 import BeautifulSoup
from pprint import pprint
import csv
with open('parlerdata.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    with open("parler.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    for item in soup.find_all("div", class_="video-container"):
        for video in item.find_all('video'):
            data_source = video['data-src']
            poster_image = video['poster']

        title_text = item.select('div')[1].get_text(strip=True)
        title_array = title_text.split(' • ')
        time = title_array[0]
        title = title_array[1]

        writer.writerow([data_source, poster_image, time, title])
