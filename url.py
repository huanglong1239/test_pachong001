
import  urllib.request
url='http://www.zczy56.com'
response= urllib.request.urlopen(url)
print(response.read().decode())



'''
import urllib.request
proxy_handler = urllib.request.ProxyHandler({'http': 'http://172.168.10.120:8888/'})
opener = urllib.request.build_opener(proxy_handler)
r = opener.open('http://www.xxx.com')
print(r.read().decode())
'''
