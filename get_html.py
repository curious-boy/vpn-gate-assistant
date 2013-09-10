#coding=utf8

import urllib2
from datetime import *
import time
from bs4 import BeautifulSoup

#==================================================================
dt = datetime.now()
time = 'time: ' + dt.strftime('%Y-%m-%d %I:%M:%S')
print time

#====================Fetch the html via proxy===============================
# NOTICE: 1: use GAE; 0: directly connect
if 1:
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.vpngate.net/cn/')
    html = response.read()
else:
    #fill in the mirror address here
    html = urllib2.urlopen('http://pl546.nas934.p-ibaraki.nttpc.ne.jp:35325/').read()

#====================Parse the html=========================================
soup = BeautifulSoup(html)
n = len(soup.findAll(href='howto_l2tp.aspx'))
vpn = ''

for i in range(0, n):
    soup1 = soup.findAll(href='howto_l2tp.aspx')[i]
    vpn = vpn + soup1.parent.parent.find(style='font-size: 12pt;').text + '\n'

else:
    print vpn

#====================Save the host list=======================================
fileHandle = open('temp.txt', 'w' )  
fileHandle.write(vpn)  
fileHandle.close()

