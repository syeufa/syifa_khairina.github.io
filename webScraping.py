import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

page = requests.get("https://www.republika.co.id")

obj = BeautifulSoup(page.text,'html.parser');
print('===========================================')
print('        == Menampilkan Kategori == ')
print('===========================================')
for kategori in obj.find_all('div',class_='teaser_conten1_center'):
    print (kategori.find('p').text)

page = requests.get("https://www.republika.co.id")
obj = BeautifulSoup(page.text,'html.parser');
print('===========================================')
print('        == Menampilkan Judul == ')
print('===========================================')
for judul in obj.find_all('div',class_='teaser_conten1_center'):
    print(judul.find('h2').text)

page = requests.get("https://www.republika.co.id")

obj = BeautifulSoup(page.text,'html.parser');
print('===========================================')
print('        == Menampilkan Waktu == ')
print('===========================================')
for waktu in obj.find_all('div',class_='date'):
    print(waktu.text)

print('===========================================')
print('     == Meyimpan Judul pada file == ')
print('===========================================')
data=[]

now = datetime.now()

f=open('C:\\Users\ASUS\Documents\webScraping\webScraping.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"Judul":publish.find('h2').text,
                 "Kategori":publish.find('a').text,
                 "Waktu_Publish":publish.find('div',class_='date').text,
                 "Waktu_Scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps = json.dumps(data, indent=1)
f.writelines(jdumps)
f.close()


