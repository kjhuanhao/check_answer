import base64
import pyautogui
import time
import requests
import os


filename = input('输入文件夹名:')
if not os.path.exists(filename):
    os.makedirs(filename)
if not os.path.exists(filename + '/outocr'):
    os.makedirs(filename + '/outocr')



def get_questions():
     num = int(input('Enter a number:'))
     _id = 0
     while _id < num:
        _id += 1
        print(f'正在截取第:{_id}题')
        time.sleep(3)
        img = pyautogui.screenshot(region=[1504,110, 400, 560])  # 分别代表：左上角坐标，宽高
        img.save(filename + '/' + str(_id) +'.jpg')
        if _id != num:
            pyautogui.click(1874, 920)



def ocr():
    API_KEY = ""
    SECRET_KEY = ""
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_KEY}&client_secret={SECRET_KEY}'
    response = requests.get(host)
    access_token = response.json()['access_token']
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    num = int(input('请输图片数量:'))
    count = 1
    for i in range(1,num+1):
        # 二进制方式打开图片文件

        f = open(filename + f'/{count}.jpg', 'rb')
        img = base64.b64encode(f.read())

        params = {"image":img}
        #access_token = '[调用鉴权接口获取的token]'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            text = response.json()
            for t in text['words_result']:
                output = t['words']
                with open(f'{filename}/outocr/' + str(count) + '.txt', 'a+',encoding='utf-8') as f:
                    f.write(output + '\n')
                    f.close()
            print('done' , count)
        count += 1
#get_questions()
ocr()

def find_answer():
    pass
