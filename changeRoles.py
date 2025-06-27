import telebot
import secret
import config
from getter import getDb, setDb


bot = telebot.TeleBot(secret.new_token)


def findRole(role):
    i = 0
    while config.rolesActions[i][1] != role:
        i += 1
    return config.rolesActions[i]


def checkRoles(db, id):
    res = ''
    roleList = db['users'][id]['roles']
    for elem in config.roles:
        if elem in roleList:
            if res != '':
                res += ', '
            res += elem[0]
    return res


def changeRole(message, db, edit=False):
    markup = telebot.types.InlineKeyboardMarkup()
    for elem in config.roles:
        button = telebot.types.InlineKeyboardButton(
            text=elem[0],
            callback_data= 'change_role!' + elem[1]
        )
        markup.add(button)
    rolesAlready = checkRoles(db, str(message.chat.id))
    button = telebot.types.InlineKeyboardButton(
        text="Я выставил все роли",
        callback_data='finish_change_roles'
    )
    markup.add(button)
    if edit:
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=f'Отметь кем ты работаешь, как отметишь нажми последнюю кнопку. Для отмены нажми еще раз. Сейчас отмечены следующие роли: {rolesAlready}'
        )
        bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reply_markup=markup
        )
    else:
        bot.send_message(
            message.chat.id,
            f'Отметь кем ты работаешь, как отметишь нажми последнюю кнопку. Для отмены нажми еще раз. Сейчас отмечены следующие роли: {rolesAlready}',
            reply_markup=markup
        )
        


def addUser(message, db):
    db['user_list'].append(str(message.chat.id))
    db['users'][str(message.chat.id)] = {
        'roles' : [],
        'week_late' : 0,
        'monthly_counter' : 0,
        'today_come': '',
        'today_checklist': [],
        'name': message.text
    }
    bot.send_message(message.chat.id, 'Хорошо, теперь укажи кем работаешь')
    setDb(db)
    changeRole(message, db)

    

def cnangeUser(message, db):
    bot.send_message(message.chat.id, text='Чуть позже добавлю все возможности, а пока...')
    changeRole(message, db, False)