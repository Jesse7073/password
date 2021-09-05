x = 3
password = 'a123456'
while x > 0:
    enter = input('請輸入密碼:')
    if password != enter:
        x = x - 1
        print('密碼錯誤!還有', x, '次機會')
    else:
        print('登入成功')
        break