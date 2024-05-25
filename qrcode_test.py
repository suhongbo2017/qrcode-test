import qrcode
run = True

while run:
    data = input('请输入二维码内容，退出输入q:')
    if data =='q':
        break
    img = qrcode.make(data)
    img.save(f'{data}.png')
    

