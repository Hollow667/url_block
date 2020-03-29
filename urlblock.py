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
            fp.write('127.0.0.1 vk.com \n')
            fp.write('127.0.0.1 www.youtube.com \n') #добавляем в файл hosts сайты для блокировки
            fp.write('127.0.0.1 www.instagram.com \n')
            fp.write('127.0.0.1 ok.ru \n')
            fp.write('127.0.0.1 www.facebook.com \n')
            fp.write('127.0.0.1 zen.yandex.ru \n')
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
    elif choices == '1':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 vk.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '2':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 www.youtube.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '3':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 www.instagram.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '4':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 ok.ru \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '5':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 www.facebook.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '6':
        try:
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 zen.yandex.ru \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
    elif choices == '7':
        try:
            url = input('введите url для блокирования:')
            fp = open('C:\Windows\System32\drivers\etc\hosts','a') #открываем файл
            fp.write('127.0.0.1 {0} \n'.format(url)) #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
else:
    if choices == '8':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 vk.com \n')
            fp.write('127.0.0.1 www.youtube.com \n') #добавляем в файл hosts сайты для блокировки
            fp.write('127.0.0.1 www.instagram.com \n')
            fp.write('127.0.0.1 ok.ru \n')
            fp.write('127.0.0.1 www.facebook.com \n')
            fp.write('127.0.0.1 zen.yandex.ru \n')
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '1':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('127.0.0.1 vk.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '2':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0. ww.youtube.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '3':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0.0.0.0 www.instagram.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '4':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0.0.0.0 ok.ru \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '5':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0.0.0.0 www.facebook.com \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '6':
        try:
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0.0.0.0 zen.yandex.ru \n') #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как super user!')
            exit()
    elif choices == '7':
        try:
            url = input('введите url для блокирования:')
            fp = open('/etc/hosts','a') #открываем файл
            fp.write('0.0.0.0 {0} \n'.format(url)) #добавляем в файл hosts сайт для блокировки
            fp.close() #закрываем файл
        except PermissionError:
            print('запустите программу как админ!')
            exit()
