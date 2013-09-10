NH6jT2Dp6WZ2

用途：
自动解析Opengate提供的支持L2TP的host，ping测试后，保存至本地文件。

使用方法：
1. 运行main.py；
2. 将vpn.txt内的IP地址填入IOS或者安卓即可。参考文档（需要翻墙访问）http://www.vpngate.net/cn/howto_l2tp.aspx#ios



原理：
利用http://www.vpngate.net/cn/发布的最新VPN服务器地址，筛选能用的主机，生成列表，手工填入IOS和安卓。


运行环境：
1.Python 2.7.5
下载链接：
http://www.python.org/getit/
本程序用Python2.7.5开发，因为Python3系列有较多差异，100%不能保证运行。
Python 2.7.5不会自动配置Windows的环境变量，需要自己手工配置。
找到PATH，在“值”里面，追加Python的安装路径，;D:\Program Files (x86)\python


2. Beautiful Soup
html网页解析库。
1）去网站http://www.crummy.com/software/BeautifulSoup/上下载Beautiful Soup；
2）解压缩到本地硬盘上，在DOS下进入解压后的目录；
3）运行“setup.py build”和“setup.py install”；
4）拷贝bs4文件夹到Python安装路径下的Lib文件夹。


3. GoAgent代理，可选。
目前的版本，默认解析目标网页的时候，是通过GAE代理访问的。如果不用代理，可能会被墙。
当然可以通过目标网页的订阅邮件里的镜像链接访问，效果一样。这样需要修改get_html.py里面的源代码。
代码如下：先把1改成0，然后填镜像地址到urllib2.urlopen，http://pl546.nas934～～～是例子。

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



参考文档:
ping 0.2
https://pypi.python.org/pypi/ping

