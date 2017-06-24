# -*-coding:utf-8 -*-

"""数据接口测试"""
import json
import requests


def register(baseapi):
    """维修企业注册测试"""
    api = baseapi + '/restservices/lciprest/lcipaccountcompany/query'
    print('*'*30)
    company_info = {
        "name": "test1",  # 必填
        "password": "a0000010",  # 必填: 需加长度验证(6 - 15位)
        "industryid": "11111111",  # 必填
        "orgnumber": "11111111",  # 必填
        "address": "测试地址",  # 必填
        "emails": "xxxxxx@xxxx.com",  # 必填: 需加邮箱格式验证
        "linkzip": "222222",  # 必填: 需加邮编格式验证
        "businesstype": "175",  # 必填: 对应经济类型分类代码表LCIPBusinessType
        "levels": "01",  # 必填: 对应维修企业经营业务类别代码表LCIPlevel
        "linkman": "测试",  # 必填
        "linktel": "138238000",  # 必填: 需加格式验证
        "legalname": "测试",  # 必填
        "legaltel": "138238000",  # 必填: 需加格式验证
        "businessrange": "测试",  # 必填
        "certificatefirsttime": "2016-01-01",  # 必填: 需加格式验证: 不能大于当前日期
        "certificatestarttime": "2016-01-01",  # 必填: 需加格式验证: 不能大于营业执照发证日期certificatefirsttime
        "certificateendtime": "2016-01-01",  # 必填: 需加格式验证: 不能小于营业期限开始时间certificatestarttime
        "operatestate": "1",  # 必填: 对应维修企业经营状态代码表LCIPOperatestate
        "areaid": "510101",  # 必填: 对应给出的省市区各级代码表
    }
    res = requests.post(url=api, json=company_info)
    data = res.json()
    status = data.get('status')
    code = data.get('code')
    companycode = data.get('companycode')
    print('test_register: status:%s  code:%s  companycode:%s' % (status, code, companycode))
    return data

def getAccesstoken(username=None, password=None):
    """获取票据（access_token）测试"""
    api = 'http://app.xiulianzone.com/4h' + '/restservices/lciprest/lcipgetaccesstoken/query'
    # 构造参数
    userinfo = {
        'username': username,
        'password': password,
    }
    # 发送请求
    res = requests.post(url=api, json=userinfo)
    print(res.status_code)
    data = res.json()
    status = data.get('status')
    code = data.get('code')
    access_token = data.get('access_token')
    print('test_getaccesstoken: status:%s  code:%s  access_token:%s' % (status, code, access_token))
    return data

def addCarfixrecord():
    """新增维修记录测试"""
    api = 'http://app.xiulianzone.com/4h' + '/restservices/lciprest/lcipcarfixrecordadd/query'
    token = getAccesstoken('18888888888', '123456').get('access_token')
    # 构造维修单数据
    car_info = {
        "access_token": token,  # 必填
        "carno": "川A12312",  # 必填
        "carvin": "LFV3A21K7D4262398",  # 必填
        "enginenumber": "234324234234234",  # 为空时, 不传此参数即可
        "company": "",  # 必填
        "repairnature": "30",  # 必填, 对应维修性质代码表LCIPrepairnature
        "repairtype": "xxxx",  # 必填
        "cartype": "9",  # 必填, 对应汽车类型代码表LCIPWebCarType
        "repairdate": "2016-01-01",  # 必填, 需加格式验证, 最小值为2014 - 01 - 01, 不能大于当前日期
        "repairmile": "5000",  # 必填
        "workorderno": "12345567",  # 必填
        "faultdescript": "洗车",  # 必填
        "faultreason": "无",  # 必填
        "materialsum": "100",  # 必填
        "mlaborsum": "200",  # 必填
        "otherexpsum": "300",  # 必填
        "total": "400",  # 必填
        "settledate": "2017-01-05",  # 必填, 需加格式验证, 不能小于送修日期repairdate
        "statementno": "8888883131231",  # 必填
    }
    req_data = {'carInfo': car_info}

    # 配件列表
    carpartslist = []
    part = {
        "partsort": "10",  # 必填, 对应零部件大类代码表LCIPStatisticsType
        "partsname": "23123",  # 必填
        "partsno": "2323",  # 必填
        "partsmanufacture": "宝马",  # 必填
        "partsquantity": "1",  # 必填
        "partscost": "100",  # 必填
        "partsallcost": "100",  # 必填
        "partsattribute": "10",  # 必填, 对应汽车配件属性代码表LCIPPartsattribute
        "caruserparts": "1"
    }
    carpartslist.append(part)
    # 维修项目列表
    repairhourslist = []
    repair = {
        "repairhours": "1",  # 必填
        "repairname": "洗车",  # 必填
        "repaircost": "50",  # 必填
        "laborhourprice": "50",  #
    }
    repairhourslist.append(repair)

    # 其它费用列表
    others = []
    other = {
        "othername": "打蜡",  # 必填
        "othercost": "20"  # 必填
    }
    others.append(other)

    req_data['carpartslist'] = json.dumps(carpartslist)
    req_data['repairhourslist'] = json.dumps(repairhourslist)
    req_data['othercostlist'] = json.dumps(others)

    res = requests.post(url=api, json=req_data)
    data = res.json()
    print('test_addcarfixrecord:')
    for k, v in data.items():
        print('    %s:%s' % (k, v))

def deleteCarfixrecord():
    """删除维修记录测试"""
    api = 'http://app.xiulianzone.com/4h' + '/restservices/lciprest/lcipdeletefixrecord/query'
    data, token = addCarfixrecord()
    req_data = {
        "recordid": data.get('recordid'),  # 必填
        "access_token": token,  # 必填, 新增记录成功返回值recordid
        "repairyear": "2015",  # 必填, 与新增记录送修日期年份值一致
    }
    res = requests.post(url=api, json=req_data)
    data = res.json()
    print('test_deleteCarfixrecord', data)

def updateCarfixrecord():
    """更新维修记录测试"""
    api = 'http://app.xiulianzone.com/4h' + '/restservices/lciprest/lcipfixrecordmodify/query'
    # 构造参数
    temp_data, token = addCarfixrecord()
    req_data = {
        "access_token": token,  # 必填
        "recordid": temp_data.get('recordid'),  # 必填
        "caruser": "张三",  # 为空时, 不传此参数即可
        "linkman": "张思",  # 为空时, 不传此参数即可
        "mobilephone": "13800138000",  # 为空时, 不传此参数即可
        "carmodel": "宝马",  # 为空时, 不传此参数即可
        "company": "test3",  # 为空时, 不传此参数即可
        "companylinker": "23",  # 为空时, 不传此参数即可
        "companyphone": "13800138000",  # 为空时, 不传此参数即可
        "companyaddress": "解放一路",  # 为空时, 不传此参数即可
        "repairnature": "10",  # 对应维修性质代码表LCIPrepairnature
        "repairtype": "小修",  # 为空时, 不传此参数即可
        "cartype": "2",  # 对应汽车类型代码表LCIPWebCarType
        "repairdate": "2016-01-01",  # 值不为空时需加格式验证
        "repairmile": "5000",  # 为空时, 不传此参数即可
        "workorderno": "12345567",  # 为空时, 不传此参数即可
        "faultdescript": "洗车",  # 为空时, 不传此参数即可
        "faultreason": "无",  # 为空时, 不传此参数即可
        "settledate": "2016-01-05",  # 值不为空时需加格式验证, 并不能小于送修日期repairdate
        "settleno": "123131231",  # 为空时, 不传此参数即可
        "securitymile": "10000",  # 为空时, 不传此参数即可
        "securitydate": "30",  # 为空时, 不传此参数即可
        "repairyear": "2016"
    }
    res = requests.post(url=api, json=req_data)
    data = res.json()

def searchCarfixrecord(self):
    """查询维修记录"""
    api = self.baseapi + '/restservices/lciprest/lcipsearchfixdatainfo/query'
    print('*' * 30)
    token = getAccesstoken()
    addCarfixrecord()
    # 构造参数
    req_data = {
        "access_token": token,  # 必填
        "carno": "川A12312",  # 必填
        "pagenum": "1",  # 必填, 查找当前车牌号对应年份维修记录的页码
        "pagesize": "10",
        "settledate": "2017-01-05"
    }

    res = requests.post(url=api, json=req_data)
    res_data = res.json()
    self.assertEqual(res.status_code, 200)
    print('维修记录数据查询', res_data)
    data_list = res_data.get('data')
    if res_data.get('code') == '1' and data_list:
        for data in data_list:
            # 处理查询的数据
            carinfo = data.get('carInfo')
            carno = carinfo.get('carno')
            print('carno: %s' % carno)
            carpartslist = data.get('carpartslist')  # 取得材料费用数据
            if carpartslist:
                for part in carpartslist:
                    partname = part.get('partsname')  # 得到材料费用中零部件名称
                    print('零部件名称：', partname)
            repairhourslist = data.get('repairhourslist')
            if repairhourslist:
                for item in repairhourslist:
                    repairname = item.get('repairname')  # 得到工时费用中维修项目名称
                    print('维修项目：', repairname)
            othercostlist = data.get('othercostlist')  # 取得其他费用数据
            if othercostlist:
                for other in othercostlist:
                    othername = other.get('othername')
                    print('其他费用：', othername)

if __name__ == '__main__':
    # getAccesstoken('13570240741', password='123456')
    addCarfixrecord()