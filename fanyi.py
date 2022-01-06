# -*- coding: utf-8 -*-
"""
@Author  : studieren
@Time    : 2022-01-06 10:06
调用百度翻译api翻译字符

"""
from hashlib import md5
import random,requests

def make_md5(s, encoding='utf-8'):
    # sign1 = md5().update(s.encode(encoding='utf-8')).hexdigest()
    sign = md5(s.encode(encoding='utf-8')).hexdigest()
    return sign


def translate_api(query, to_lang='en'):
    """
    :param query: 待翻译的字符串
    :param to_lang: 默认翻译成英语en，如果要翻译成汉语，参数改成zh
    :return:
    """
    appid = '属于你自己的百度appid' #可以从https://fanyi-api.baidu.com/manage/developer 获取
    token = '属于你自己的百度token'
    from_lang = 'auto' # 自动检测待翻译字符串
    endpoint = 'https://fanyi-api.baidu.com/'
    # path1 = 'api/trans/vip/doccount'
    path2 = 'api/trans/vip/translate'
    url = endpoint + path2
    salt = random.randint(10000, 99999)
    sign = make_md5(appid + query + str(salt) + token)
    params = {
        'appid': appid,
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'salt': salt,
        'sign': sign
    }
    fanyiheaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, params=params, headers=fanyiheaders)
    result = r.json()
    dic = eval(json.dumps(result, indent=4, ensure_ascii=False))
    res = '\n'.join([i['dst'] for i in dic['trans_result']])
    time.sleep(2) # 翻译间隔2秒，免费
    return res
