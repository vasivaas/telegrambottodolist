# -*- coding: utf-8 -*-
import Strategy
from time import sleep
from time import time
import datetime

import day as day

articles = ['на']
days = {'Понеділок': 1,
        'Вівторок': 2,
        'Середу': 3,
        'Четвер': 4,
        "П'ятницю": 5,
        'Суботу': 6,
        'Неділю': 7}


def get_unix_time(text):
    unix_time = -1
    if text[0] == 'на':
        task_day = days.get(text[0], -1)
        if day == -1:
            return unix_time
        cur_day = datetime.datetime.today().weekday()
        if task_day < cur_day:
            task_day += 7
        unix_time = (task_day - cur_day) * 3600 * 24 + int(time())
        return unix_time
    return unix_time


def check_msg(msg):
    text = msg.text.split()[1:]
    pos1 = 0
    pos2 = 0
    for i in range(len(text)):
        if text[i] in articles:
            pos1 = i
            break
    if pos1 == 0:
        return -1
    task = text[:pos1]
    for i in range(pos1, len(text)):
        if text[i] == 'з':
            pos2 = i
            break
    if pos2 == 0 or len(text) - pos2 != 3:
        return -1
    task_time = text[pos1: pos2]
    unix_time = get_unix_time(task_time)
    if unix_time == -1:
        return -1
    if text[-1] != 'важливістю':
        return -1
    if text[-2] != 'високою':
        if text[-2] != 'низькою':
            return -1
    f = open(str(msg.chat.id) + '.txt', 'a+')
    task_text = ''
    for i in task:
        task_text = task_text + i + ' '
    f.write(task_text)
    f.write(str(unix_time) + ' ')
    f.write(text[-2][0] + '\n')
    f.close()
    return unix_time


def action(msg, bot):
    # if not check_msg(msg.text)
    unix_time = check_msg(msg)
    if unix_time <= 0:
        bot.send_message(msg.chat.id, "Упссс, повідомлення не коректно введено. Введіть команду /help для довідки!!")
        return
    else:
        bot.send_message(msg.chat.id, "Завдання успішно додано")
    sleep(abs(unix_time - int(time())))
    p = 0
    text = msg.text.split()[1:]
    for i in range(len(text)):
        if text[i] in articles:
            p = i
            break
    task = text[:p]
    task_text = ''
    for i in task:
        task_text = task_text + i + ' '
    bot.send_message(msg.chat.id, "Нове нагадування: " + task_text)
    f = open(str(msg.chat.id) + '.txt', 'r+')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    for i in range(len(lines)):
        if (lines[i][-1] == text[-2][0]) and (lines[i][-2] == str(unix_time)):
            lines.remove(lines[i])
            break
    for i in range(len(lines)):
        lines[i] = ' '.join(lines[i]) + '\n'
    f.close()
    f = open(str(msg.chat.id) + '.txt', 'w')
    f.writelines(lines)
    f.close()


class NewTask(Strategy.BotStrategy):
    def __init__(self):
        pass
