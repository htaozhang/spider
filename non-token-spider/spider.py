#!/usr/bin/python
#coding: utf-8
import httplib
import urllib
import requests
import urllib
import re
import time
import sys
import codecs
from lxml import etree

import parser

reload(sys)
sys.setdefaultencoding('utf-8')


def task():
    #httplib.HTTPConnection.debuglevel = 1
    #httplib.HTTPSConnection.debuglevel = 1

    session = requests.Session()
    
    #home
    home_url = 'http://www.jc.net.cn/'
    page_home = session.get(home_url).text
    
    #login
    params = 'login_name=malinlizhen&login_password=cbb123456&autoLogin=1'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    page = session.post('http://www.jc.net.cn/net/sys/FrontLoginAction.do?method=loginPost', data = params, headers = header).text

    #start
    page = session.get(home_url + '/market/').text
    open('market_page.html', 'w').write(page)
    bigtypes = parser.parser_market_page('market_page.html')
    

    for x in bigtypes:
        bigtype, x_url = x 
        page = session.get('http://www.jc.net.cn' + x_url).text
        filename = './level1/%s.html' % bigtype
        open(filename, 'w').write(page)

        smarttypes = parser.parser_bigtype_page(filename)
        
        for y in smarttypes:
            smarttype, y_url = y
            page = session.post('http://www.jc.net.cn' + y_url).text
            total_page = parser.parser_total_page(page, False)
            y_url = y_url[0:y_url.find('pno=')]
            
            for i in range(total_page):
                page = session.post('http://www.jc.net.cn' + y_url + 'pno=%d' % (i + 1)).text
                filename = './level2/%s_%s_%s.html' % (bigtype, smarttype, i + 1)
                open(filename, 'w').write(page)
                #detailinfo = parser.parser_smarttype_page(filename)
            #break
        #break

    return


if __name__ == '__main__':
    task()
