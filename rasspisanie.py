import telebot
import requests

bot = telebot.TeleBot("8045405795:AAHOUc5n-77DWEEge-odsHHI8r8dmj7_BP0")

inline_keyboard_smena = telebot.types.InlineKeyboardMarkup()
inline_keyboard_smena.row(
    telebot.types.InlineKeyboardButton("первая", callback_data="first"),
    telebot.types.InlineKeyboardButton("вторая", callback_data="second")
)

inline_keyboard_napravlenie1 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_napravlenie1.row(
    telebot.types.InlineKeyboardButton("диз / рек / тур", callback_data="napravlenie1"),
    telebot.types.InlineKeyboardButton("псо / юр / ПД / ком", callback_data="napravlenie2"),
    telebot.types.InlineKeyboardButton("рнг / са / пб", callback_data="napravlenie3"),
    telebot.types.InlineKeyboardButton("назад", callback_data="back")
)

inline_keyboard_napravlenie2 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_napravlenie2.row(
    telebot.types.InlineKeyboardButton("диз / рек / тур", callback_data="napravlenie4"),
    telebot.types.InlineKeyboardButton("псо / юр / ПД / ком", callback_data="napravlenie5"),
    telebot.types.InlineKeyboardButton("рнг / са / пб", callback_data="napravlenie6"),
    telebot.types.InlineKeyboardButton("назад", callback_data="back")
)

inline_keyboard_back1 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_back1.row(
    telebot.types.InlineKeyboardButton("назад", callback_data="backr")
)

inline_keyboard_back2 = telebot.types.InlineKeyboardMarkup()
inline_keyboard_back2.row(
    telebot.types.InlineKeyboardButton("назад", callback_data="backt")
)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Этот бот отправляет рассписание МКПО')
    bot.send_message(message.chat.id, 'Выберите свою смену:', reply_markup=inline_keyboard_smena)

@bot.message_handler(commands=['sosal?'])
def sosal(message):
    bot.send_message(message.chat.id, 'да')

@bot.callback_query_handler(func=lambda call: True)
def handle_input_type(call):
    if call.data == "first":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы выбрали первую смену.", reply_markup=inline_keyboard_napravlenie1)
   
    elif call.data == "second":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы выбрали вторую смену.", reply_markup=inline_keyboard_napravlenie2)
    
    elif call.data == "back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы вернулись к выбору смены.", reply_markup=inline_keyboard_smena)
    
    elif call.data == "backr":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы вернулись к выбору смены.", reply_markup=inline_keyboard_napravlenie1)
    
    elif call.data == "backt":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы вернулись к выбору смены.", reply_markup=inline_keyboard_napravlenie2)
    
    elif call.data == "napravlenie1":
        bot.send_message(call.message.chat.id, "Вы выбрали дизайн / рекламу / туризм.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009447-1%20%D1%81%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%94%D0%98%D0%97,%20%D0%A0%D0%95%D0%9A,%20%D0%A2%D0%A3%D0%A0.xls", call.message)
        
    
    elif call.data == "napravlenie2":
        bot.send_message(call.message.chat.id, "Вы выбрали психологию / юристу / ПД / коммерция.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009448-1%20%D1%81%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%9F%D0%A1%D0%9E,%D0%AE%D0%A0,%20%D0%9F%D0%94,%20%D0%9A%D0%9E%D0%9C%D0%9C.xls", call.message)
    
    elif call.data == "napravlenie3":
        bot.send_message(call.message.chat.id, "Вы выбрали рНГ / СА / ПБ.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009449-1%20%D0%A1%D0%9C%D0%95%D0%9D%D0%90%20%D0%A0%D0%9D%D0%93,%20C%D0%90,%20%D0%9F%D0%91.xls", call.message)
    
    elif call.data == "napravlenie4":
        bot.send_message(call.message.chat.id, "Вы выбрали дизайн / рекламу / туризм.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009450-2%20%D1%81%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%94%D0%98%D0%97,%20%D0%A0%D0%95%D0%9A,%20%D0%A2%D0%A3%D0%A0.xls", call.message)
    
    elif call.data == "napravlenie5":
        bot.send_message(call.message.chat.id, "Вы выбрали психологию / юристу / ПД / коммерция.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009451-2%20%D1%81%D0%BC%D0%B5%D0%BD%D0%B0%20%D0%9F%D0%A1%D0%9E,%20%D0%9F%D0%94.xls", call.message)
    
    elif call.data == "napravlenie6":
        bot.send_message(call.message.chat.id, "Вы выбрали рНГ / СА / ПБ.")
        fileSend("https://f-mkpo.udsu.ru/files/raspisanie-2020/009452-2%20%D0%A1%D0%9C%D0%95%D0%9D%D0%90%20%D0%A0%D0%9D%D0%93,%20%D0%A1%D0%90,%D0%9F%D0%91.xls", call.message)
        
def fileSend(url, message):    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ
        with open('downloaded_file.xls', 'wb') as f:
            f.write(response.content)
        
        with open('downloaded_file.xls', 'rb') as f:
            bot.send_document(message.chat.id, f)
        
       
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"Не удалось скачать файл. Ошибка: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")




bot.polling(none_stop=True)