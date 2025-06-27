import time
import config


def makeShedule(db):
    t = time.localtime()
    x = (t.tm_year, t.tm_mon, t.tm_mday, 0, 0, 0, t.tm_wday, t.tm_yday, t.tm_isdst)
    today = time.mktime(x)
    db['today_day'] = today
    wday = 0
    if t.tm_wday == 5 or t.tm_wday == 6:
        wday = 1
    for elem in config.roles_come.keys():
        today_come = today + 3600 * config.roles_come[elem][0] + 60 * config.roles_come[elem][1] + wday * config.roles_come[elem][2] * 3600
        db['today_come'][elem] = today_come
    for elem in config.roles_checkList.keys():
        today_checkList = today + 3600 * config.roles_checkList[elem][0] + 60 * config.roles_checkList[elem][1] + wday * config.roles_checkList[elem][2] * 3600
        db['today_checkList'][elem] = today_checkList
    return db


def makeNewDay(db):
    db = makeShedule(db)
    for elem in db['come'].keys:
        db['come'][elem] = False
        db['checkList'][elem] = False
    return db