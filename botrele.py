import telegram
import serial
import time
import logging
import pyfirmata
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
#Revisar que el puerto serial sea el que se está usando en arduino
ser = serial.Serial('/dev/ttyACM0',9600)

def start(bot,update): #Declara funcion
	bot.send_message(chat_id=update.message.chat_id,text='Hola creador!')
	
def turnOff(bot,update):
	bot.send_message(chat_id=update.message.chat_id,text='Apagado')
	ser.write(b'Y')#N
	
def turnOn(bot,update):
	bot.send_message(chat_id=update.message.chat_id,text='Encendido')
	ser.write(b'N')#Y
	
bot =telegram.Bot(token='890900042:AAHCSgivIhh4eEE8uDHXqHQM9ZY3P460jO0')
update = Updater(token='890900042:AAHCSgivIhh4eEE8uDHXqHQM9ZY3P460jO0')
dispatcher = update.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level = logging.INFO)
start_handler=CommandHandler('start',start)
turnOn_handler =CommandHandler('turnOn',turnOn)
turnOff_handler = CommandHandler('turnOff',turnOff)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(turnOn_handler)
dispatcher.add_handler(turnOff_handler)
update.start_polling()