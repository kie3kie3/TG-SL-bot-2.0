import config
import telebot
import admin
import workSpace
import secret
import register
from getter import getDb, setDb


bot = telebot.TeleBot(secret.new_token)


@bot.callback_query_handler(func=lambda call: call.data.startswith('change_role!'))
def changeRoleHandle(call):
    db = getDb()
    role = call.data[call.data.index('!') + 1:]
    i = 0
    while i < len(config.roles) and config.roles[i][1] != role:
        i += 1
    role = config.roles[i]
    if role not in db['users'][str(call.message.chat.id)]['roles']:
        db['users'][str(call.message.chat.id)]['roles'].append(role)
    else:
        db['users'][str(call.message.chat.id)]['roles'].remove(role)
    register.changeRole(call.message, db, True)


@bot.callback_query_handler(func=lambda call: call.data == 'finish_change_roles')
def finishChangeRole(call):
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    workSpace.mainMenu(str(call.message.chat.id))


@bot.message_handler(commands=['start'])
def start(message):
    db = getDb()
    if str(message.chat.id) in db['user_list']:
        register.cnangeUser(message)
    else:
        msg = bot.send_message(message.chat.id, 'Привет, представься плз')
        bot.register_next_step_handler(msg, register.addUser, db)



def main():
    bot.infinity_polling()