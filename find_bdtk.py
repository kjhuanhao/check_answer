
import requests
import json
import re
from bing import bing_search
def get_link(filename,num):
    with open(f'{filename}/outocr/{num}.txt',encoding='utf-8') as f:
        q = f.read()

    url = f'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&ch=&tn=baidu&bar=&wd={q}'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'BIDUPSID=B9FE5C35F8235EA485D74ADF71C55F31; PSTM=1668924110; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ISSW=1; ISSW=1; newlogin=1; BAIDUID=B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1; H_PS_PSSID=36545_37552_37512_37139_34812_37303_37729_37801_37715_37741_26350_37786; BDUSS=HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV; BDUSS_BFESS=HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV; ab_sr=1.0.1_NjgwOTg5YmIzNzYyYzQ5ZjVhZjVjMTg0MWU2MzQ3MjBiYmE0M2M1ZGY2MTI4OTZmN2I3YTQ1ZGQzMGJiZDgwZmUzMWU1MDIzODgzYzZhYzU0YTczYzgzYjNmNGJmN2JkMjMyOWI3ZGVmYzE0MTgwOTc0ZWNlNzc5ZjllYzg5NDQ4YTM3OTkxZjU1YmNjZDUzYTMxMWUzNDIzOTg2NzU3YQ==; BAIDUID_BFESS=B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1; delPer=0; BD_CK_SAM=1; PSINO=7; BA_HECTOR=21808h8g0524ag8gak2k2rb21hnusc51f; ZFY=iwSxJrbZbzcv2fci3fveiLGqSLgR8SvZg6qUhbqEhJg:C; B64_BOT=1; baikeVisitId=5eb6a7b0-0640-413f-a9b2-3d938745065e; sug=3; sugstore=0; bdime=0; H_PS_645EC=14beR3eUMs3cIcSxSlq9zPa6tRuPLzKMwLNCfm%2F5W%2FPYAOwHVSGuIalo10E; ORIGIN=2',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    cookies = {
        'BIDUPSID': 'B9FE5C35F8235EA485D74ADF71C55F31',
        'PSTM': '1668924110',
        'BD_UPN': '12314753',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'ISSW': '1',
        'newlogin': '1',
        'BAIDUID': 'B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1',
        'H_PS_PSSID': '36545_37552_37512_37139_34812_37303_37729_37801_37715_37741_26350_37786',
        'BDUSS': 'HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV',
        'BDUSS_BFESS': 'HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV',
        'ab_sr': '1.0.1_NjgwOTg5YmIzNzYyYzQ5ZjVhZjVjMTg0MWU2MzQ3MjBiYmE0M2M1ZGY2MTI4OTZmN2I3YTQ1ZGQzMGJiZDgwZmUzMWU1MDIzODgzYzZhYzU0YTczYzgzYjNmNGJmN2JkMjMyOWI3ZGVmYzE0MTgwOTc0ZWNlNzc5ZjllYzg5NDQ4YTM3OTkxZjU1YmNjZDUzYTMxMWUzNDIzOTg2NzU3YQ==',
        'BAIDUID_BFESS': 'B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1',
        'delPer': '0',
        'BD_CK_SAM': '1',
        'PSINO': '7',
        'BA_HECTOR': '21808h8g0524ag8gak2k2rb21hnusc51f',
        'ZFY': 'iwSxJrbZbzcv2fci3fveiLGqSLgR8SvZg6qUhbqEhJg:C',
        'B64_BOT': '1',
        'baikeVisitId': '5eb6a7b0-0640-413f-a9b2-3d938745065e',
        'sug': '3',
        'sugstore': '0',
        'bdime': '0',
        'H_PS_645EC': '14beR3eUMs3cIcSxSlq9zPa6tRuPLzKMwLNCfm%2F5W%2FPYAOwHVSGuIalo10E',
        'ORIGIN': '2',
    }

    res = requests.get(url,headers=headers,cookies=cookies)
    text = res.text
    obj = re.compile('https://easylearn.baidu.com/edu-page/.*?=search')
    link = obj.findall(text)[0]
    obj_id = re.compile('id=(.*?)&')
    t_id = obj_id.findall(link)[0]
    return t_id



def check_an(t_id):
    cookies = {
        'BIDUPSID': 'B9FE5C35F8235EA485D74ADF71C55F31',
        'PSTM': '1668924110',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'newlogin': '1',
        'BAIDUID': 'B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1',
        'H_PS_PSSID': '36545_37552_37512_37139_34812_37303_37729_37801_37715_37741_26350_37786',
        'BDUSS': 'HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV',
        'BDUSS_BFESS': 'HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV',
        'ab_sr': '1.0.1_NjgwOTg5YmIzNzYyYzQ5ZjVhZjVjMTg0MWU2MzQ3MjBiYmE0M2M1ZGY2MTI4OTZmN2I3YTQ1ZGQzMGJiZDgwZmUzMWU1MDIzODgzYzZhYzU0YTczYzgzYjNmNGJmN2JkMjMyOWI3ZGVmYzE0MTgwOTc0ZWNlNzc5ZjllYzg5NDQ4YTM3OTkxZjU1YmNjZDUzYTMxMWUzNDIzOTg2NzU3YQ==',
        'Hm_lvt_4bfd1db084bb12333b0db120cc8ca177': '1669123574,1669177715,1669295101',
        'BAIDUID_BFESS': 'B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1',
        'Hm_lpvt_4bfd1db084bb12333b0db120cc8ca177': '1669295877',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'BIDUPSID=B9FE5C35F8235EA485D74ADF71C55F31; PSTM=1668924110; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; newlogin=1; BAIDUID=B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1; H_PS_PSSID=36545_37552_37512_37139_34812_37303_37729_37801_37715_37741_26350_37786; BDUSS=HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV; BDUSS_BFESS=HA4d2xCVDhVQ1NPb0doT01JVlJlV0ZIb2ZEVG82NXdOUDVEaWlPZnhuSC04NlpqRUFBQUFBJCQAAAAAAAAAAAEAAAC42h2gu8O6wDY2NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP5mf2P-Zn9jV; ab_sr=1.0.1_NjgwOTg5YmIzNzYyYzQ5ZjVhZjVjMTg0MWU2MzQ3MjBiYmE0M2M1ZGY2MTI4OTZmN2I3YTQ1ZGQzMGJiZDgwZmUzMWU1MDIzODgzYzZhYzU0YTczYzgzYjNmNGJmN2JkMjMyOWI3ZGVmYzE0MTgwOTc0ZWNlNzc5ZjllYzg5NDQ4YTM3OTkxZjU1YmNjZDUzYTMxMWUzNDIzOTg2NzU3YQ==; Hm_lvt_4bfd1db084bb12333b0db120cc8ca177=1669123574,1669177715,1669295101; BAIDUID_BFESS=B9FE5C35F8235EA46EF60FB4BD55F298:SL=0:NR=10:FG=1; Hm_lpvt_4bfd1db084bb12333b0db120cc8ca177=1669295877',
        #'Referer': 'https://www.baidu.com/link?url=p2Kj_BMTbZYwb2aUpmkNqf9Tq2NOLnzdfiZnNpyhCSlWoUkd1o6RZ91QTXwvOzHlvnp3wGK8ZIG14OWM9Dw29ycxoM_xhw5HKQqed0cDxlByqYoNsYf4o3W8rXsT0R16ZefHNsMKb_0vRlSeOog97q&wd=&eqid=9fb8010500018f6f00000006637f6ed3',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'id': t_id,
        'fr': 'search',
    }

    response = requests.get('https://easylearn.baidu.com/edu-web/content/shitiinfo', params=params, cookies=cookies, headers=headers)
    res = response.text.encode('utf-8').decode('unicode_escape')
    res_json = json.loads(res, strict=False)
    for i in res_json['data']['answer']:
        print(i)

if __name__=='__main__':
    num = int(input('Please enter a num'))
    count = 0
    for i in range(0,num+1):
        count += 1
        try:
            print(f"=====第{count}=====")
            check_an(get_link('安全常识测试',count))
        except:
            print(f'对不起，第{count}题，题库中没有答案')
            bing_search('安全用电测试',count)

