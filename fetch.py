#!/home/peterpark/anaconda3/bin/python
import requests
from bs4 import BeautifulSoup
import urllib

response = requests.get("https://mcgill.ca/mathstat/graduate/current-students/phd-comprehensive-examinations/part")
data = response.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    href = link.get('href')
    if href != None:
        if "pdf" in href:
            if "https" in href:
                req = requests.get(href)
            else:
                req = requests.get("https:" + href)
            file = open(href.split("/")[-1], "wb+")
            for chunk in req.iter_content(100000):
                file.write(chunk)
            file.close
