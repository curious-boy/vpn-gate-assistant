NH6jT2Dp6WZ2

��;��
�Զ�����Opengate�ṩ��֧��L2TP��host��ping���Ժ󣬱����������ļ���

ʹ�÷�����
1. ����main.py��
2. ��vpn.txt�ڵ�IP��ַ����IOS���߰�׿���ɡ��ο��ĵ�����Ҫ��ǽ���ʣ�http://www.vpngate.net/cn/howto_l2tp.aspx#ios



ԭ��
����http://www.vpngate.net/cn/����������VPN��������ַ��ɸѡ���õ������������б��ֹ�����IOS�Ͱ�׿��


���л�����
1.Python 2.7.5
�������ӣ�
http://www.python.org/getit/
��������Python2.7.5��������ΪPython3ϵ���н϶���죬100%���ܱ�֤���С�
Python 2.7.5�����Զ�����Windows�Ļ�����������Ҫ�Լ��ֹ����á�
�ҵ�PATH���ڡ�ֵ�����棬׷��Python�İ�װ·����;D:\Program Files (x86)\python


2. Beautiful Soup
html��ҳ�����⡣
1��ȥ��վhttp://www.crummy.com/software/BeautifulSoup/������Beautiful Soup��
2����ѹ��������Ӳ���ϣ���DOS�½����ѹ���Ŀ¼��
3�����С�setup.py build���͡�setup.py install����
4������bs4�ļ��е�Python��װ·���µ�Lib�ļ��С�


3. GoAgent������ѡ��
Ŀǰ�İ汾��Ĭ�Ͻ���Ŀ����ҳ��ʱ����ͨ��GAE������ʵġ�������ô������ܻᱻǽ��
��Ȼ����ͨ��Ŀ����ҳ�Ķ����ʼ���ľ������ӷ��ʣ�Ч��һ����������Ҫ�޸�get_html.py�����Դ���롣
�������£��Ȱ�1�ĳ�0��Ȼ������ַ��urllib2.urlopen��http://pl546.nas934�����������ӡ�

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



�ο��ĵ�:
ping 0.2
https://pypi.python.org/pypi/ping

