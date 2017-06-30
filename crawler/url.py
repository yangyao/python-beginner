import urllib.request

req = urllib.request.urlopen('http://m.cnbeta.com')

html = req.read()

print(html)