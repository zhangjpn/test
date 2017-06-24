# -*-coding:utf-8 -*-

from os import path
import csv
import requests
from threading import Thread

base_path = path.dirname(__file__)

customerconsume = 'customerconsume.csv'
car_file_name = 'car.csv'

car_file_path = path.join(base_path, car_file_name)
customerconsume_file_path = path.join(base_path, customerconsume)

def upload(j):
    created_url = 'http://app.xiulianzone.com/4c/customer/consume/create/'
    update_url = 'http://app.xiulianzone.com/4c/customer/consume/update/'
    res = requests.post(url=update_url, json=j)
    if res.status_code != 200:
        print('更新失败')
        res = requests.post(url=created_url, json=j)
        if res.status_code != 200:
            print('上传失败')
        else:
            print('上传成功')
    else:
        print('更新成功')


with open(customerconsume_file_path, 'rt', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for item in reader:
        j = {}
        for k, v in item.items():
            j[k] = v
            if v == 'NULL':
                j[k] = ''
            if isinstance(v, (int, float)):
                if v < 0:
                    j[k] = abs(v)
        # c = None
        # with open(car_file_path, 'rt', encoding='utf-8') as f2:
        #     reader2 = csv.DictReader(f2)
        #     for k in reader2:
        #         if k['CarNum'] == j['ConsumeCarNum']:
        #             c = k
        #             break
        # if c['VIN'] is not 'Null':
        #     if k['VIN'][8] == 'X' or k['VIN'][8] == 'x':
        #         print(c['VIN'])
        #         continue
        # Thread(target=upload, args=(j,)).start()