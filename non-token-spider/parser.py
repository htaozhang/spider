#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv
import re
import os
import json
import sys
import codecs
import commands
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')



def parser_market_page(market_page):
    tree = etree.HTML(codecs.open(market_page, 'r', 'utf-8').read())
    bigtypes = tree.xpath(u'//*[@class="mainbigtype"]/div')
    res = []

    for (i, bigtype) in enumerate(bigtypes):
        res.append((bigtype.xpath('a')[0].text.strip(), bigtype.xpath('a/@href')[0]))
        pass
    return res

def parser_bigtype_page(bigtype_page):
    tree = etree.HTML(codecs.open(bigtype_page, 'r', 'utf-8').read())
    smarttypes = tree.xpath(u'//*[@id="collapseOne0"]/div')
    res = []

    for (i, smarttype) in enumerate(smarttypes):
        res.append((smarttype.xpath('a')[0].text.strip(), smarttype.xpath('a/@href')[0]))
        pass
    return res


def parser_total_page(smarttype_page, isfile = True):
    tree = etree.HTML((codecs.open(smarttype_page, 'r', 'utf-8').read()) if isfile else smarttype_page)
    page_info = tree.xpath(u'//*[@class="page-op"]/span')[0].text
    res = re.compile(r'\d+').findall(page_info)[0]
    
    if not res or int(res) <= 0:
        return -1

    return int(res)


def parser_data_content(data):
    tree = etree.HTML(data)
    res = tree.xpath(u'//*[@class="popover-content1"]')
    
    for x in res:
        if x.text.find('联系电话') != -1:
            #return ''.join([e.strip() for e in x.text.strip().split(r'^M')])
            return '或'.join([e.strip() for e in x.text.strip().split(r'或')])
            

    return '-'

def parser_smarttype_page(smarttype_page):
    tree = etree.HTML(codecs.open(smarttype_page, 'r', 'utf-8').read())
    tables = tree.xpath(u'//*[@class="row-fluid"]/table')
    table = None

    for x in tables:
        if x.xpath('@class')[0].find('table table-bordered table-hover') != -1:
            table = x
            break
        pass

    trs = table.xpath('tbody/tr')
    
    result = []

    for (i, row) in enumerate(trs):
        if i == 0:
            continue
        
        cols = row.xpath('td')
        element = []

        for (j, col) in enumerate(cols):
            if j > 8:
                continue
            elif j == 0:
                element.append(col.xpath('a')[0].text.strip())
            elif j == 8:
                element.append(col.xpath('a')[0].text.strip())
                element.append(parser_data_content(col.xpath('a/@data-content')[0].strip()))
            else:
                element.append(col.text.strip() if col.text else '')
            pass
        result.append(element)
        pass

    return result


def parser_all_page(path):
    files = os.listdir(path)
    writer = csv.writer(file('./data.csv', 'a+'))

    for filename in files:
        bigtype, smalltype, other = filename.split('_')
        
        try:
            info = parser_smarttype_page(path + '/' + filename)
        except Exception, e:
            print e

        cmd = 'mv %s/%s ./done' % (path, filename)   
        commands.getoutput(cmd)
        
        if len(info) <= 0:
            continue
        for e in info:
            if len(e) != 10:
                continue
            writer.writerow([bigtype, smalltype] + e)
        pass

    return

if __name__ == '__main__':
    #parser_market_page(sys.argv[1])
    #parser_bigtype_page(sys.argv[1])
    #parser_total_page(sys.argv[1])
    #parser_smarttype_page(sys.argv[1])
    parser_all_page(sys.argv[1])


