import sys
os = sys.platform #определяем os
print('''

██╗░░░██╗██████╗░██╗░░░░░  ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
██║░░░██║██╔══██╗██║░░░░░  ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██║░░░██║██████╔╝██║░░░░░  ██████╦╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░
██║░░░██║██╔══██╗██║░░░░░  ██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░
╚██████╔╝██║░░██║███████╗  ██████╦╝███████╗╚█████╔╝╚█████╔╝██║░╚██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
by lime
Привет! Ты много сидишь в соц. сетях? Я тебе помогу, и заблокирую доступ к соц. сетям!
''')
choices = input(
'''Выбери соц. сети к которым тебе нужно заблокировать доступ:
1. vk
2. youtube
3. instagram
4. однокласники
5. facebook
6. Яндекс. дзен
7. указать url самому
8. заблокировать всё из списка
==>''')
if os in 'win32':
    if choices == '8':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://vk.com/')
            fp.write('127.0.0.1 https://www.youtube.com/') #добавляем в файл hosts сайты для блокировки
            fp.write('127.0.0.1 https://www.instagram.com/')
            fp.write('127.0.0.1 https://ok.ru/')
            fp.write('127.0.0.1 https://www.facebook.com')
            fp.write('127.0.0.1 https://zen.yandex.ru')
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
    elif choices == '1':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://vk.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '2':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.youtube.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '3':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.instagram.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '4':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://ok.ru/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '5':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.facebook.com') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '6':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 https://zen.yandex.ru') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '7':
        try:
            url = input('введите url для блокирования:')
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 {0}'.format(url)) #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
else:
    if choices == '8':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://vk.com/')
            fp.write('127.0.0.1 https://www.youtube.com/') #добавляем в файл hosts сайты для блокировки
            fp.write('127.0.0.1 https://www.instagram.com/')
            fp.write('127.0.0.1 https://ok.ru/')
            fp.write('127.0.0.1 https://www.facebook.com')
            fp.write('127.0.0.1 https://zen.yandex.ru')
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '1':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://vk.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '2':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.youtube.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '3':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.instagram.com/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '4':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://ok.ru/') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '5':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://www.facebook.com') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '6':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 https://zen.yandex.ru') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '7':
        try:
            url = input('введите url для блокирования:')
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 {0}'.format(url)) #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
