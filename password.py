x = 3
password = 'a123456'
while x > 0:
    x = x - 1
    enter = input('請輸入密碼:')
    if password == enter:
        print('登入成功')
        break
    elif password != enter and x > 0:
        print('密碼錯誤!還有', x, '次機會')
    else:
        print('帳號已被封鎖')
        break