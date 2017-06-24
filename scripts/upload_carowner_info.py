# -*-coding:utf-8 -*-

from os import path
import csv
import json
import requests
from threading import Thread
from time import sleep
import random
carowner_file_name = 'carowner.csv'
base_path = path.dirname(__file__)
carowner_file_path = path.join(base_path, carowner_file_name)


def upload(j):
    print('')
    created_url = 'http://app.xiulianzone.com/4c/carowner/create/'
    update_url = 'http://app.xiulianzone.com/4c/carowner/update/'
    sleep(random.randint(2, 7))
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


with open(carowner_file_path, 'rt', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for item in reader:
        # operate
        sleep(random.randint(0, 4))
        j = {}
        for k, v in item.items():
            j[k] = v
            if v == 'NULL':
                j[k] = ''
        print(j)
        # Thread(target=upload, args=(j,)).start()
