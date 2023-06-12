import sys
import telebot
from config import API as token
from Audio_to_text import audio_to_text
from image_gen import generic_image


bot = telebot.TeleBot(token)

ALL_COMMANDS = '/help - help, \n' \
               '/generate - generate image for text\n' \
               'voice - translate voice for text'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Заєбав \n' + ALL_COMMANDS)


@bot.message_handler(content_types=['voice'])
def save_audio(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'audio/audio_n.ogg'
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        text = audio_to_text(src)
        bot.reply_to(message, text)

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Заєбав')


@bot.message_handler(commands=['help'])
def print_msg(message):

    bot.send_message(message.chat.id, ALL_COMMANDS)


@bot.message_handler(commands=['generate'])
def print_g(message):
    bot.send_message(message.chat.id, 'send me text for generate')
    @bot.message_handler(content_types=['text'])
    def generate_img(message):

        if generic_image(message.text, '1024x1024'):
            with open('data.png', 'rb') as file:
                bot.send_photo(message.chat.id, file)

            return


if __name__ == "__main__":
    bot.polling()

