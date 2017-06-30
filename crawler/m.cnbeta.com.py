from bs4 import BeautifulSoup
import urllib.request
import csv
req = urllib.request.urlopen('http://m.cnbeta.com')
html = req.read()
soup = BeautifulSoup(html,'lxml')
content = soup.select('.module_list')[0]
# todo 保存cnbeta的新闻到csv文件中
writer = csv.writer(open('data.csv','w+'))
for child in content.select('li'):
    writer.writerow((child.find("a").string,child.find("a").get('href'),child.find("em").string))




