#!/usr/bin/env python

from lxml import html
import requests
from sys import argv

argc = len(argv)

def remove_empty(teh_string):
    teh_string = teh_string.replace('\n\n','\n')
    teh_string = teh_string.replace('\r','\n')
    newlist=list()
    the_list = teh_string.split('\n')
    
    for line in the_list: 
        if len(line) > 0:
            newlist.append(line)
    
    return "\n".join(newlist)

def get_tune(tune_id):
    makeuri = "https://thesession.org/tunes/{}".format(tune_id)
    
    page = requests.get(makeuri)
    tree = html.fromstring(page.content)
    nds = tree.xpath('//*[@class="notes"]')

    tune_list = list()
    for tune in nds:
        tune_list.append(remove_empty(tune.text_content()))
        
    return { 'tunes':tune_list, 'count': len(tune_list) }

def get_search(sc_name='butterfly', sc_type='', sc_mode=''):
    #makeuri = "https://thesession.org/tunes/search?type={0}&mode={1}&q={2}".format(sc_type, sc_mode, sc_name)
    makeuri = "https://thesession.org/tunes/search?type={0}&mode={1}&q={2}".format(sc_type, sc_mode, sc_name)
    
    page =  requests.get(makeuri)

    tree = html.fromstring(page.content)

    results = tree.xpath('//div[@id="results"]/ol/li/a/text()')

    search = list()

    for idx,result in enumerate(results):
        search.append( {'name': result, 'id': tree.xpath('//div[@id="results"]/ol/li/a/@href')[idx].split('/')[-1] } )
    
    return search

if argc > 2 and argv[1] == 's':
    query = " ".join(argv[2:argc])
    print("Searching thesession.org for '{}'..".format(query))
    results = get_search(sc_name=query)
    for item in results:
        print("{0} (id is {1})".format(item['name'],item['id']))

if argc >= 2 and argv[1] != 's':

    #    print("Searching for tune with id {0}..".format(argv[1]))
    results = get_tune(argv[1])
    #print('Current id has {} versions..'.format(results['count']))

    if argc == 2:
        #print("Showing first..\n")
        print(results['tunes'][0])

    elif argc == 3:
        #print("Showing no. {}..\n".format(argv[2]))
        print(results['tunes'][int(argv[2])-1])


#print(argc)
#print(argv)
