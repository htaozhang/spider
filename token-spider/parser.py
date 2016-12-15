#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import json
import sys
import codecs
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

mp = {'3': '高档', '2': '中档', '1': '普通'}

def to_html():
    htmls = os.listdir('./html')
    for html in htmls:
        infos = os.path.basename(os.path.splitext(r'%s' % (html))[0]).split('_')
        type, level1, level2 = infos
        #print type, level1, level2
        
        file_obj = open('./html/' + html, 'r')
        content = json.loads(file_obj.read()[1:-1])
        file_obj.close()
        open('./data/' + html , 'w').write(content['html'])
        pass
    return

def statistic():
    print '%s,%s,%s,%s,%s' % ('产品分类', '一级', '二级', '档次', '品牌')
    htmls = os.listdir('./data')
    for html in htmls:

        infos = os.path.basename(os.path.splitext(r'%s' % (html))[0]).split('_')
        type, level1, level2 = infos
        #print type + '_' + level1 + '_' + level2
        f = codecs.open('./data/' + html, 'r', 'utf-8')
        content = f.read()
        f.close()
        tree = etree.HTML(content)
        
        path = '//*[@id="select_brand"]/div[@class="pinpai_search"]/div[@class="b_brand"]/div[@class="pinpai"]//div[@id="brand_area"]'
        father = tree.xpath(u'%s' % path)[0]
        
        #print father.xpath(u'@id')[0], father.xpath(u'@p_count')[0]

        nodes = father.xpath(u'div')

        data = {}

        for node in nodes:
            pid, nid = node.xpath(u'@pid'), node.xpath(u'@nid')
            if not pid or not nid:
                continue
            pid, nid = pid[0], nid[0]
            name = node.xpath(u'a')[0].text.strip()
            data.setdefault(nid, set())
            data[nid].add(name)
            #print name, nid

            
        for i in ['3', '2', '1']:
            if i not in data:
                continue
            print '%s,%s,%s,%s,%s' % (type.strip(), level1.strip(), level2.strip(), mp[i], ','.join(list(data[i])))


        #nodes = tree.xpath(u'//*[@id="brand_area"]/div[@class="p_2"]')
        #for node in nodes:
            #print node.xpath(u'a')[0].text, 
            #print node.xpath(u'@nid')[0]
        #break
        
    return

if __name__ == '__main__':
    #to_html()
    statistic()



