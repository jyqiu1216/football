# -*- coding: utf-8 -*-

import requests
import json
import csv
from pymongo import MongoClient

host = "127.0.0.1"
port = 27017

client = MongoClient(host, port)
db = client['jc']

url = 'http://i.sporttery.cn/odds_calculator/get_odds?i_format=json&i_callback=getData&poolcode[]=had'
# req = request.Request(url='%s' % url)
res = requests.get(url)
resp = res.text.split('(')[1].split(')')[0].encode('utf-8').decode('unicode_escape')
params = json.loads(resp)
data = params['data']
print(data)
d = {}

csv_file = open('test.csv', 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(['num', 'h', 'd', 'a'])
for key in data.keys():
    csv = []
    d['id'] = data[key]['id']
    d['a'] = float(data[key]['had']['a'])
    d['d'] = float(data[key]['had']['d'])
    d['h'] = float(data[key]['had']['h'])
    d['num'] = data[key]['num']
    d['h_cn'] = data[key]['h_cn']
    d['h_id'] = data[key]['h_id']
    d['a_cn'] = data[key]['a_cn']
    d['a_id'] = data[key]['a_id']
    d['date'] = data[key]['date']
    d['time'] = data[key]['time']
    print(d)
    # db.match.insert(d)
    csv.append(d['num'])
    csv.append(d['h'])
    csv.append(d['d'])
    csv.append(d['a'])
    writer.writerow(csv)
csv_file.close()
