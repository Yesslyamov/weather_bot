import pyowm
import telebot

owm = pyowm.OWM('eeea37c6dd04cd0abecf62b2bf16cf13', language = 'ru')
bot = telebot.TeleBot("1571601492:AAHwKEP44yMy0MbRXfqzoy7eGLlABsK7JAA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	welcome = "Привет, я бот, который погоду даёт. Напиши мне название города, а я скажу какая там погода!"
	bot.send_message(message.chat.id, welcome)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')['temp']
	  

		answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + '\n'
		answer += 'Температура сейчас около ' + str(temp) + '\n\n'

		if temp < 10:
			answer += 'На улице прохладно. Если выйдешь, надень что-нибудь по теплее'
		elif temp  < 20:
			answer += 'На улице тепло. Можно наадеть легкую ветровку!'
		else:
			answer += 'На улице жарко. Футболки и шорт будет достаточно'

		bot.send_message(message.chat.id, answer)
	
	except:
		bot.send_message(message.chat.id, 'Такого города не существует.')
    
bot.polling( none_stop = True )