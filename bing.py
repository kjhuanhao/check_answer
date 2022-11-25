# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2022/11/25 9:03
# @File     : bing.py
# @Project  : 未命名
import re
import requests
def bing_search(filename,count):
    cookies = {
        '_EDGE_V': '1',
        'SRCHD': 'AF=NOFORM',
        'SRCHUID': 'V=2&GUID=2E6897E81C224A1DA1EA8483732AD5D0&dmnchg=1',
        'ANON': 'A=17FC7060C6571E9859C1532FFFFFFFFF',
        'USRLOC': 'HS=1&CLOC=LAT=21.662484961348156|LON=110.91691268044993|A=733.4464586120832|TS=221125010309|SRC=W',
        'ISSW': '1',
        'ZHCHATSTRONGATTRACT': 'TRUE',
        'MUID': '0D738107AAC66B1F1ABB9365ABBC6ACE',
        'MUIDB': '0D738107AAC66B1F1ABB9365ABBC6ACE',
        'MUIDV': 'NU=1',
        'MMCASM': 'ID=7F083BB5026A4AF584E0F7BDFCDB58D6',
        '_TTSS_IN': 'hist=WyJmciIsImVuIiwiemgtSGFucyIsImF1dG8tZGV0ZWN0Il0=',
        '_TTSS_OUT': 'hist=WyJmciIsInpoLUhhbnMiLCJlbiJd',
        '_tarLang': 'default=en',
        'ANIMIA': 'FRE=1',
        'ZHCHATWEAKATTRACT': 'TRUE',
        'SUID': 'A',
        '_EDGE_S': 'SID=21123D5C99496EB224E12F3B982F6F15',
        'WLS': 'C=d77f6b449c648651&N=hao',
        '_SS': 'SID=21123D5C99496EB224E12F3B982F6F15',
        '_U': '1fORH20k8G9XJJ5TnK0P6ImBIUCju1PIKmD5WYWCxTSn57_uRnTMauxECaUtnSGMxcW4G01bQXIZfPNmooUNwK3MJrO8qxn5j88AgjW7Xb8MsmgE5JeCSKmfnouBz4e2-oRxy-I7f9Nt4-gbJgolde_ZRoj4JYBOuY-VbR2mQxmRfAn_T-6otBqxOZ4Wi41re',
        'SRCHUSR': 'DOB=20221120&T=1669338189000',
        'ipv6': 'hit=1669341792820&t=4',
        'SNRHOP': 'TS=638049350603727037&I=1',
        'SRCHHPGUSR': 'SRCHLANG=zh-Hans&BRW=XW&BRH=S&CW=1920&CH=388&SCW=1903&SCH=2191&DPR=1.0&UTC=480&DM=1&PV=8.0.0&HV=1669338191&BZA=0&PRVCW=1920&PRVCH=937&EXLTT=31&THEME=1&PR=1',
    }

    headers = {
        'authority': 'cn.bing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=2E6897E81C224A1DA1EA8483732AD5D0&dmnchg=1; ANON=A=17FC7060C6571E9859C1532FFFFFFFFF; USRLOC=HS=1&CLOC=LAT=21.662484961348156|LON=110.91691268044993|A=733.4464586120832|TS=221125010309|SRC=W; ISSW=1; ZHCHATSTRONGATTRACT=TRUE; MUID=0D738107AAC66B1F1ABB9365ABBC6ACE; MUIDB=0D738107AAC66B1F1ABB9365ABBC6ACE; MUIDV=NU=1; MMCASM=ID=7F083BB5026A4AF584E0F7BDFCDB58D6; _TTSS_IN=hist=WyJmciIsImVuIiwiemgtSGFucyIsImF1dG8tZGV0ZWN0Il0=; _TTSS_OUT=hist=WyJmciIsInpoLUhhbnMiLCJlbiJd; _tarLang=default=en; ANIMIA=FRE=1; ZHCHATWEAKATTRACT=TRUE; SUID=A; _EDGE_S=SID=21123D5C99496EB224E12F3B982F6F15; WLS=C=d77f6b449c648651&N=hao; _SS=SID=21123D5C99496EB224E12F3B982F6F15; _U=1fORH20k8G9XJJ5TnK0P6ImBIUCju1PIKmD5WYWCxTSn57_uRnTMauxECaUtnSGMxcW4G01bQXIZfPNmooUNwK3MJrO8qxn5j88AgjW7Xb8MsmgE5JeCSKmfnouBz4e2-oRxy-I7f9Nt4-gbJgolde_ZRoj4JYBOuY-VbR2mQxmRfAn_T-6otBqxOZ4Wi41re; SRCHUSR=DOB=20221120&T=1669338189000; ipv6=hit=1669341792820&t=4; SNRHOP=TS=638049350603727037&I=1; SRCHHPGUSR=SRCHLANG=zh-Hans&BRW=XW&BRH=S&CW=1920&CH=388&SCW=1903&SCH=2191&DPR=1.0&UTC=480&DM=1&PV=8.0.0&HV=1669338191&BZA=0&PRVCW=1920&PRVCH=937&EXLTT=31&THEME=1&PR=1',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"107.0.1418.56"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="107.0.1418.56", "Chromium";v="107.0.5304.110", "Not=A?Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"8.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        'x-edge-shopping-flag': '1',
    }

    with open(f'{filename}/outocr/{count}.txt','r',encoding='utf-8') as f:
        t = f.read()
    params = {
        'q': t,
    }
    try:
        response = requests.get('https://cn.bing.com/search', params=params, cookies=cookies, headers=headers)
        search = response.text
        obj = re.compile('<main aria-label="搜索结果">.*')
        obj_refer = re.compile('https://.*?.html')
        search_result = obj.findall(search)[0]
        #print(obj_refer.findall(search_result))
        link = obj_refer.findall(search_result)
        print('参考链接:')
        print(link[0])
    except:
        print('没有搜索结果')


