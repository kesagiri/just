import telebot
import time
from selenium import webdriver
import constants
import requests


bot = telebot.TeleBot(constants.token)


def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/ticket_s', '/ticket')
    user_markup.row('сколько тикетов?')
    bot.send_message(message.from_user.id, "Клавиатура включена. Для получения справки нажмите /help", reply_markup=user_markup)


def stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Клавиатура отключена, для включения ввести /start", reply_markup=hide_markup)


def help(message):
    bot.send_message(message.chat.id, "Могу показать сколько тикетов свободных и в работе, а также взять свободный"
                                      " тикет в работу")


def open(message):
    cookies = {
        'BITRIX_SM_LOGIN': 'a.dubchak',
        'BITRIX_SM_VOTE_USER_ID': '148',
        '_ym_uid': '1491811544846709114',
        'optimizelyEndUserId': 'oeu1493972306883r0.6919147453266121',
        'optimizelySegments': '%7B%224978310576%22%3A%22false%22%2C%224978350724%22%3A%22gc%22%2C%224980220558%22%3A%22direct%22%7D',
        'optimizelyBuckets': '%7B%227959575893%22%3A%227955394618%22%7D',
        '_identity_dealer': 'c9b281c5d8e889ce10bcb33e639d99133a6723ea68170e1176c0ff2af459c5c3a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_identity_dealer%22%3Bi%3A1%3Bs%3A59%3A%22%5B%22cw11502%22%2C%226391880c-5bf5-42f7-8c31-6f801539b3ef%22%2C62208000%5D%22%3B%7D',
        'PHPSESSID': '34f96f22b271a70cbb078f621282fc8f',
        'BITRIX_SM_UIDH': '6e63d7801da29927a69ebf208569da6b',
        'BITRIX_SM_UIDL': 'a.dubchak',
        'BITRIX_SM_SALE_UID': '0',
        'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
        '_ym_isad': '1',
        '_identity_vds': 'fd1f4d1263b68759acd99e5794a6ca937402266b2e7b76f13bfd6615bb8e4f21a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_identity_vds%22%3Bi%3A1%3Bs%3A60%3A%22%5B%22primepro%22%2C%22639179d5-c50d-4558-a454-382821c4d81b%22%2C62208000%5D%22%3B%7D',
        'cp': '1e84e5c755902e1cfb1aa9f353cb2d66',
        'cp_l': 'VzNzaWJHOW5hVzRpT2lKdGVYTjBaV1ZzSWl3aWN5STZJakZsT0RSbE5XTTNOVFU1TURKbE1XTm1ZakZoWVRsbU16VXpZMkl5WkRZMklpd2ljR0ZuWlNJNklsd3ZJbjFk',
        'master_login': 'mysteel',
        'PHPSTAFFSESSID': 'f9208a75c8e61151498a6236b4f7edab',
        '_identity_token_hosting': '32a430eab7ef81750e287c7660ef9e66d24313adbc6af88c553510eee8d6bfbba%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22_identity_token_hosting%22%3Bi%3A1%3Bs%3A65%3A%22%7B%22id%22%3A%22lketerno2%22%2C%22token%22%3A%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%7D%22%3B%7D',
        '_identity_first': '6bff6db9592347882bbd1f73afa00cb3ddb6d9302446b033f6cd2805204044a5a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_first%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22lketerno2%22%2C%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%2C62208000%5D%22%3B%7D',
        '_ga': 'GA1.2.324740584.1479473720',
        '_gid': 'GA1.2.2105787682.1496042893',
        '_identity_hosting': '4a219aa72455af1e9aca97a48ce1be2922a1653370b5343edae0cd1237b6aa3aa%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22lketerno2%22%2C%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%2C62208000%5D%22%3B%7D',
        '_identity_staff': '7828a185a3e8276ee9070cb174f35a1e0383c7992119c115a6193cd117428df9a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_staff%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22a.dubchak%22%2C%2263913761-17aa-4a26-8993-5aea44417d9a%22%2C62208000%5D%22%3B%7D',
    }

    headers = {
        'Bx-ajax': 'true',
        'Origin': 'https://corporate.timeweb.ru',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://corporate.timeweb.ru/',
        'Connection': 'keep-alive',
    }

    params = (
        ('action', 'open'),
        ('site_id', 's1'),
        ('sessid', '0d4305860fcf0a39bfbdb794057d1d19'),
    )

    data = [
        ('REPORT', ''),
        ('ready', 'Y'),
        ('', ''),
        ('', ''),
    ]

    requests.post('https://corporate.timeweb.ru/bitrix/tools/timeman.php', headers=headers, params=params, cookies=cookies, data=data)
    bot.send_message(message.chat.id, "Залогинился")


def close(message):
    cookies = {
        'BITRIX_SM_LOGIN': 'a.dubchak',
        'BITRIX_SM_VOTE_USER_ID': '148',
        '_ym_uid': '1491811544846709114',
        'optimizelyEndUserId': 'oeu1493972306883r0.6919147453266121',
        'optimizelySegments': '%7B%224978310576%22%3A%22false%22%2C%224978350724%22%3A%22gc%22%2C%224980220558%22%3A%22direct%22%7D',
        'optimizelyBuckets': '%7B%227959575893%22%3A%227955394618%22%7D',
        '_identity_dealer': 'c9b281c5d8e889ce10bcb33e639d99133a6723ea68170e1176c0ff2af459c5c3a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_identity_dealer%22%3Bi%3A1%3Bs%3A59%3A%22%5B%22cw11502%22%2C%226391880c-5bf5-42f7-8c31-6f801539b3ef%22%2C62208000%5D%22%3B%7D',
        'PHPSESSID': '34f96f22b271a70cbb078f621282fc8f',
        'BITRIX_SM_UIDH': '6e63d7801da29927a69ebf208569da6b',
        'BITRIX_SM_UIDL': 'a.dubchak',
        'BITRIX_SM_SALE_UID': '0',
        'BITRIX_SM_SOUND_LOGIN_PLAYED': 'Y',
        '_ym_isad': '1',
        '_identity_vds': 'fd1f4d1263b68759acd99e5794a6ca937402266b2e7b76f13bfd6615bb8e4f21a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_identity_vds%22%3Bi%3A1%3Bs%3A60%3A%22%5B%22primepro%22%2C%22639179d5-c50d-4558-a454-382821c4d81b%22%2C62208000%5D%22%3B%7D',
        'cp': '1e84e5c755902e1cfb1aa9f353cb2d66',
        'cp_l': 'VzNzaWJHOW5hVzRpT2lKdGVYTjBaV1ZzSWl3aWN5STZJakZsT0RSbE5XTTNOVFU1TURKbE1XTm1ZakZoWVRsbU16VXpZMkl5WkRZMklpd2ljR0ZuWlNJNklsd3ZJbjFk',
        'master_login': 'mysteel',
        'PHPSTAFFSESSID': 'f9208a75c8e61151498a6236b4f7edab',
        '_identity_token_hosting': '32a430eab7ef81750e287c7660ef9e66d24313adbc6af88c553510eee8d6bfbba%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22_identity_token_hosting%22%3Bi%3A1%3Bs%3A65%3A%22%7B%22id%22%3A%22lketerno2%22%2C%22token%22%3A%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%7D%22%3B%7D',
        '_identity_first': '6bff6db9592347882bbd1f73afa00cb3ddb6d9302446b033f6cd2805204044a5a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_first%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22lketerno2%22%2C%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%2C62208000%5D%22%3B%7D',
        '_ga': 'GA1.2.324740584.1479473720',
        '_gid': 'GA1.2.2105787682.1496042893',
        '_identity_hosting': '4a219aa72455af1e9aca97a48ce1be2922a1653370b5343edae0cd1237b6aa3aa%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22lketerno2%22%2C%226391c76c-222f-4a21-89e2-c32ebd0c42ef%22%2C62208000%5D%22%3B%7D',
        '_identity_staff': '7828a185a3e8276ee9070cb174f35a1e0383c7992119c115a6193cd117428df9a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_staff%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22a.dubchak%22%2C%2263913761-17aa-4a26-8993-5aea44417d9a%22%2C62208000%5D%22%3B%7D',
    }

    headers = {
        'Bx-ajax': 'true',
        'Origin': 'https://corporate.timeweb.ru',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://corporate.timeweb.ru/',
        'Connection': 'keep-alive',
    }

    params = (
        ('action', 'close'),
        ('site_id', 's1'),
        ('sessid', '0d4305860fcf0a39bfbdb794057d1d19'),
    )

    data = [
        ('REPORT', ''),
        ('ready', 'Y'),
        ('', ''),
        ('', ''),
    ]

    requests.post('https://corporate.timeweb.ru/bitrix/tools/timeman.php', headers=headers, params=params, cookies=cookies, data=data)
    bot.send_message(message.chat.id, "Разлогинился")


def ticket_s(message):
    driver = webdriver.Chrome("C:/Users/a.dubchak/IdeaProjects/chromedriver.exe")
    driver.get('https://staff2.timeweb.ru/tickets/picker/pick?service=clients')
    element = driver.find_element_by_id("loginform-username")
    element.send_keys("a.dubchak")  # логин
    element1 = driver.find_element_by_id("loginform-password")
    element1.send_keys("HMbEr3YXRzbr")  # пароль
    element2 = driver.find_element_by_name("login-button")
    element2.click()
    time.sleep(1)
    if driver.title == "Ошибка":
        bot.send_message(message.chat.id, "Свободных тикетов нет")
        print("Свободных тикетов нет")
        driver.close()
    else:
        bot.send_message(message.chat.id, "Тикет в работе" + "\n" + driver.title)
        print("Тикет в работе")
        print(driver.title)


def ticket(message):
    cookies = {
        'master_login': 'beb43e61cba2d6998a1fa4e4c8505a9d97a9188ecce17233af0bee0075516d47a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22master_login%22%3Bi%3A1%3Bs%3A9%3A%22a.dubchak%22%3B%7D',
        '_ym_uid': '1491811544846709114',
        'optimizelyEndUserId': 'oeu1493972306883r0.6919147453266121',
        'optimizelySegments': '%7B%224978310576%22%3A%22false%22%2C%224978350724%22%3A%22gc%22%2C%224980220558%22%3A%22direct%22%7D',
        'optimizelyBuckets': '%7B%227959575893%22%3A%227955394618%22%7D',
        '_identity_dealer': 'c9b281c5d8e889ce10bcb33e639d99133a6723ea68170e1176c0ff2af459c5c3a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_identity_dealer%22%3Bi%3A1%3Bs%3A59%3A%22%5B%22cw11502%22%2C%226391880c-5bf5-42f7-8c31-6f801539b3ef%22%2C62208000%5D%22%3B%7D',
        '_csrf': 'ac637ae66a6868c7edb58f02e51ae5794a6b223de101e5bdd9201404148a586fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22hlds2fRRHc61R3UNGRlQ33TiuF8F_hV5%22%3B%7D',
        '_ym_isad': '1',
        'PHPSTAFFSESSID': '06df50e80448a7b08e335966bb27833f',
        '_identity_vds': '27545681865928d51a72ecef0cf622a6ab3fc8c4ccdea8cd8e2b37d5c10a9822a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22_identity_vds%22%3Bi%3A1%3Bs%3A58%3A%22%5B%22goshav%22%2C%226391cf34-e0bf-4ead-a563-3756b0b7d49b%22%2C62208000%5D%22%3B%7D',
        'PHPSESSID': 'd81fd3e37ff1d0af6310a658e7eb7efa',
        '_identity_token_hosting': 'a0417892905fdc05a8d2d81b68f81d3fc0c3f732beeca91b4bf53693988aaea1a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22_identity_token_hosting%22%3Bi%3A1%3Bs%3A63%3A%22%7B%22id%22%3A%22cm72928%22%2C%22token%22%3A%2263913155-d5e0-4a5b-948d-a29673ad8605%22%7D%22%3B%7D',
        '_identity_first': '71885f7bb2ad7df9c72a39e7c57e1a4511c35aaa28c70b61ba5f62ac5cb63397a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_first%22%3Bi%3A1%3Bs%3A59%3A%22%5B%22cm72928%22%2C%2263913155-d5e0-4a5b-948d-a29673ad8605%22%2C62208000%5D%22%3B%7D',
        '_ga': 'GA1.2.324740584.1479473720',
        '_gid': 'GA1.2.2105787682.1496042893',
        '_identity_hosting': 'c0194f993eb3274f561d25eb219404205be32c8c4f89580e3df14e45fdde5c30a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity_hosting%22%3Bi%3A1%3Bs%3A59%3A%22%5B%22cm72928%22%2C%2263913155-d5e0-4a5b-948d-a29673ad8605%22%2C62208000%5D%22%3B%7D',
        '__utma': '1.85001656.1473670399.1496050409.1496052231.918',
        '__utmb': '1.3.10.1496052231',
        '__utmc': '1',
        '__utmz': '1.1473670399.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '_identity_staff': '7828a185a3e8276ee9070cb174f35a1e0383c7992119c115a6193cd117428df9a%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22_identity_staff%22%3Bi%3A1%3Bs%3A61%3A%22%5B%22a.dubchak%22%2C%2263913761-17aa-4a26-8993-5aea44417d9a%22%2C62208000%5D%22%3B%7D',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://staff2.timeweb.ru/tickets/picker/pick?service=clients',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }

    params = (
        ('service', 'clients'),
    )

    requests.get('https://staff2.timeweb.ru/tickets/picker/pick', headers=headers, params=params, cookies=cookies)
    r = requests.get('https://staff2.timeweb.ru/tickets/picker/pick', headers=headers, params=params, cookies=cookies)
    statusCod = int(r.status_code)
    if statusCod != int(500):
        bot.send_message(message.chat.id, "Тикет в работе")
        print(statusCod)
    else:
        while statusCod == int(500):
            requests.get('https://staff2.timeweb.ru/tickets/picker/pick', headers=headers, params=params, cookies=cookies)
            r2 = requests.get('https://staff2.timeweb.ru/tickets/picker/pick', headers=headers, params=params, cookies=cookies)
            statusWhile = int(r2.status_code)
            if statusWhile != int(500):
                bot.send_message(message.chat.id, "Цикл выполнен. Тикет взят в работу")
                print(statusWhile)
                break

