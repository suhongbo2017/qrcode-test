import qrcode #导入模块
from datetime import datetime

run = True #默认设置循环运行

while run:
    data = input('请输入二维码内容，退出输入q:') #输入二维码内容
    if data =='q': #判断输入是q，则退出循环。
        break
    img = qrcode.make(data) #生成二维码数据
    img.save(f'./{data}.png') #保存为png图像。
    with open('./log.txt','+a',encoding='utf-8')as qrc: # 生成内容日志。
        qrc.write(datetime.now(),data)
    

