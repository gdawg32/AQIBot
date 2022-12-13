import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import air

TOKEN = '5827192803:AAGQKNJ3LPAH4C-x52TVHC8QOohTjPg37DU'

# Init the  bot with token
bot = telebot.TeleBot(TOKEN)

# List of cities available
cities=air.cityLists()

# Define the Inline Keyboard for the user to choose the cities
def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    for i in cities:
        markup.add(
            InlineKeyboardButton(i, callback_data=i),
        )
    return markup

#To catch the message you need to use this decorator. 
@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, "Hello there!", reply_markup=markup_inline())

# Handles the request made by the user in the Inline Keyboard and replies with AQI level
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data in cities:
        for j in cities:
            if call.data == j:
                aqi_level = air.City_Stats(j)
                bot.answer_callback_query(call.id, "AQI Level in: "+j+" is: "+aqi_level)  

#Launches the bot in infinite loop mode with additional
#...exception handling, which allows the bot
#...to work even in case of errors. 
bot.infinity_polling()                   