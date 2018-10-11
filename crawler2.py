from io import BytesIO
import requests
import bs4
from PIL import Image
import urllib.request
import os
import sys

def getimg(query):
    res = requests.get('https://www.google.com/search?q='+query+'&&sourcelmns&tbm=isch')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    img = soup.findAll(attrs={"alt":"Image result for "+query})
    i = 0;
    for im in img:
        url = im['src']
        print(url)
        i = i+1
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
            image = Image.open(BytesIO(raw_data))
        directory = os.getcwd()+"/"+query+"/"
        try:
            os.stat(directory)
        except:
            os.mkdir(directory) 
        name = query+str(i)+".png"
        image.save(directory+name)
getimg(sys.argv[1])
