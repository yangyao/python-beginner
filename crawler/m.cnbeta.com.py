from bs4 import BeautifulSoup
import urllib.request
import csv
req = urllib.request.urlopen('http://m.cnbeta.com')
html = req.read()
soup = BeautifulSoup(html,'lxml')
content = soup.select('.module_list')[0]
f = open('data.csv','w+',encoding='gb18030')
writer = csv.writer(f)
for child in content.select('li'):
    writer.writerow((child.find("a").string,child.find("a").get('href'),child.find("em").string))
f.close()


