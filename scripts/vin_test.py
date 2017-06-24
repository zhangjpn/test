# -*-codint:utf-8 -*-

def is_valid_vin(vin):
    """判断vin是否有效"""
    if not isinstance(vin, str):
        return False
    kv = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'p': 7, 'r': 9,
        's': 2, 't': 3, 'u': 4, 'v': 5, 'w': 6, 'x': 7, 'y': 8, 'z': 9
    }  # 'q': 8, 无q
    wv = {
        '1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 10,
        '10': 9, '11': 8, '12': 7, '13': 6, '14': 5, '15': 4, '16': 3, '17': 2
    }

    if len(vin) != 17:
        return False
    lowervin = vin.lower()
    verifyCode = lowervin[8]
    # 计算
    total = 0
    for i in range(17):
        if i == 8:
            continue
        code = lowervin[i]
        if code in kv:
            total += kv[code] * wv[str(i + 1)]
        else:
            print('%s code not in kv'%code)
            return False
    res = str(total % 11)
    if verifyCode in '0123456789':
            print('verify code in 1234567890')
            print(verifyCode)
            return res == verifyCode
    elif verifyCode == 'x':
        print(res)
        return res == '10'


def is_valid_vin2(vin):
    """判断vin是否有效"""
    if not isinstance(vin, str):
        return False
    kv = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'p': 7, 'r': 9,
        's': 2, 't': 3, 'u': 4, 'v': 5, 'w': 6, 'x': 7, 'y': 8, 'z': 9
    }  # 'q': 8, 无q
    wv = {
        '1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 10,
        '10': 9, '11': 8, '12': 7, '13': 6, '14': 5, '15': 4, '16': 3, '17': 2
    }

    if len(vin) != 17:
        return False
    lowervin = vin.lower()
    verifyCode = lowervin[8]
    if verifyCode < '0' or verifyCode > '9':
        if verifyCode != 'x':
            return False
    total = 0
    for i in range(17):
        if i == 8:
            continue
        code = lowervin[i]
        if code in kv:
            total += kv[code] * wv[str(i + 1)]
        else:
            return False
    res = str(total % 11)
    if verifyCode == 'x':
        return res == '10'
    else:
        return res == verifyCode

if __name__ == '__main__':
    vin = 'LSGDC82C11S10203O'
    vin2 = 'LDC633T2XE3176572'

    print(is_valid_vin2(vin))