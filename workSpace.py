import config
import telebot
from changeRoles import findRole
from secret import new_token
from getter import getDb, setDb


bot = telebot.TeleBot(new_token)


def makeOneAction(action):
    realAction = action[:action.index('_')]
    role = action[action.index('_') + 1:]
    res = config.rolesDict[role] + ' ' + config.actionsDecript[realAction]
    btn = telebot.types.InlineKeyboardButton(text=res, callback_data=action)
    return btn


def makeActionsButton(id, db):
    btnActions = []
    roles = db['users'][id]['roles']
    for elem in roles:
        actions = config.rolesActions[elem[1]]
        for elem1 in actions:
            btnActions.append(makeOneAction(elem1))
    return btnActions


def mainMenu(id):
    db = getDb()
    markup = telebot.types.InlineKeyboardMarkup()
    for elem in makeActionsButton(id, db):
        markup.add(elem)
    bot.send_message(int(id), text='Добрый день, что сегодня?', reply_markup=markup)
