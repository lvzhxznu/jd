import  requests

from pyquery import PyQuery as pq

from lxml import  etree


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}


s = requests.session()

s.get("https://www.jd.com", headers = headers, timeout =1)

r = s.get("https://www.jd.com", headers = headers, timeout = 1)


#print(r.text)

print(r.request.headers)

print(r.headers)

print(r.cookies)