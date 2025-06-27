import config
import telebot
import secret


bot = telebot.TeleBot(secret.new_token)


def whichCheckList(call):
    ...