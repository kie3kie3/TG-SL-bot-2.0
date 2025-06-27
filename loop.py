import telebot
import secret
import time
from getter import getDb, setDb
import newDay
import newWeek
import newMonth
import checkLate


bot = telebot.TeleBot(secret.new_token)


def checkTime():
    db = getDb()
    curT = time.localtime()
    today = time.localtime(db['today'])
    if curT.tm_mon != today.tm_mon or curT.tm_mday != today.tm_mday or curT.tm_year != today.tm_year:
        if curT.tm_wday == 6:
            db = newWeek.makeNewWeek(db)
        db = newDay.makeNewDay(db)
        if curT.tm_mon != today.tm_mon or curT.tm_year != today.tm_year:
            db = newMonth.makeNewMonth(db)
    db = checkLate.checkLate(db)
    setDb(db)


def main():
    while True:
        time.sleep(5)
        checkTime()
        checkLate.checLate()