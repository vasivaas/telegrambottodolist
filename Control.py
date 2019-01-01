# -*- coding: utf-8 -*-
import All
import Delete
import Help
import New
import Start
import config
from telebot import TeleBot

bot = TeleBot(config.token)

commands = ['start', 'help', 'new', 'all', 'delete']
st = Start
hp = Help
nw = New
al = All
dl = Delete


@bot.message_handler(content_types=["text"])
def handle_text(msg):
    if msg.text[0] != "/":
        bot.send_message(msg.chat.id, "Вкажи мені команду.")
        return

    comm = msg.text.split()[0][1:]
    if comm not in commands:
        bot.send_message(msg.chat.id, "Хибна команда. Введи /help для інстркції.")
        return

    if comm == 'start':
        st.action(msg.chat.id, bot)
        return

    if comm == 'help':
        hp.action(msg.chat.id, bot)
        return

    if comm == 'new':
        nw.action(msg, bot)
        return

    if comm == 'all':
        al.action(msg.chat.id, bot)
        return

    if comm == 'delete':
        dl.action(msg.chat.id, msg.text, bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
