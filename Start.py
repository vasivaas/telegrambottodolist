# -*- coding: utf-8 -*-
import Strategy


def action(num, bot):
    bot.send_message(num, """Привіт, я допоможу тобі з твоїм персональним списком справ! 
                          Скористайся командою /new щоб добавити завдання. Ось приклад :
                          /new намалювати щось на Понеділок(або інший день тижня) з низькою 
                           (високою) важливістю. Команда /help для повного ознайомлення 
                            зі мною. Що ж почнемо""")

    name = str(num) + ".txt"
    file = open(name, "w")
    file.close()


class StartCommand(Strategy.BotStrategy):
    def __init__(self):
        pass
