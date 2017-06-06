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
    cookies = {}

    headers = {}

    params = (
        
    )

    data = [
      
    ]

    requests.post('https://corporate.timeweb.ru/bitrix/tools/timeman.php', headers=headers, params=params, cookies=cookies, data=data)
    bot.send_message(message.chat.id, "Залогинился")


def close(message):
    cookies = {
    }

    headers = {
      
    }

    params = (
       
    )

    data = [
      
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
    }

    headers = {
       
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

