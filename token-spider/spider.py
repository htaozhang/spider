#!/usr/bin/python
#coding: utf-8

import requests
import urllib
import re
import time
import sys
import codecs
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')


def task():
    session = requests.Session()
    
    #home
    home_url = 'http://www.iccchina.com'
    page_home = session.get(home_url).text
    
    pat = re.compile("encodeURIComponent\('(.*?)'\)")
    token = urllib.quote(pat.findall(page_home)[0])
    
    #login
    params = 'authenticity_token=' + token + '&username=xinhe&password=cbb123456&remember_me=1&authenticity_token=' + token
    page = session.post('http://www.iccchina.com/users/login',data = params).text
    
    #verify
    page = session.get('http://www.iccchina.com/users/dkey_verify').text
    params = 'authenticity_token=' + token + '&dkey=' + raw_input('please input dkey:')

    #print page
    #start
    page = session.post('http://www.iccchina.com/users/key_check', data = params).text
    page = session.get(home_url).text

    open('page.html', 'w').write(page)
    f = codecs.open('page.html', 'r', 'utf-8')
    content = f.read()
    f.close()
    tree = etree.HTML(content)
    types = tree.xpath(u'//*[@id="nav_category_b"]/div')
    
    for type in types:
        k0 = type.xpath('h3/a')[0].text
        print '\n' + k0

        first_levels = type.xpath('div/dl')
        for first_level in first_levels:
            if not first_level.xpath('dt/a'):
                continue

            k1 = first_level.xpath('dt/a')[0].text
            print '\t' + k1

            second_levels = first_level.xpath('dd/em')
            for second_level in second_levels:
                k2 = second_level.xpath('a')[0].text
                detail_url = 'http://search.iccchina.com/' + second_level.xpath('a/@href')[0]
                print '\t\t' + k2 + ': ' + detail_url
                the_page = session.get(detail_url).text
                open('%s.html' % ('_'.join([k0, k1, k2])), 'w').write(the_page)
                pass
            pass

    return


if __name__ == '__main__':
    task()
