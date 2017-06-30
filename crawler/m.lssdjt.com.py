# coding: utf-8
import time
import datetime
import urllib.request
from bs4 import BeautifulSoup
import sys
import csv
__author__ = 'yangyao'

site = 'http://m.lssdjt.com/'
csvfile = open('history.csv','w+',encoding='gb18030')
f = csv.writer(csvfile)
start_date = datetime.datetime(2017,1,1)
start_timestamp = time.mktime(start_date.timetuple())
print(start_timestamp)
end_timestamp = start_timestamp + (86400*365)
while start_timestamp < end_timestamp:
    local_date = time.localtime(start_timestamp)
    date = time.strftime('%Y-%m-%d',local_date)
    print(date)
    link = site +'?date='+date
    print(link)
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,'lxml')
    dom = soup.select("div.list li")
    for li in dom:
        if li.string is None:
            continue
        if li.find('a') is None:
            continue
        f.writerow((li.find('a')['href'], li.string))
    #sys.exit()
    start_timestamp += 86400

