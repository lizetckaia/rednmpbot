from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

TOKEN = 'Введите токен своего телеграм бота'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update, context):
    """
    Функция, узнающая имя пользователя и приветствующая его. Далее предлагает выбрать нужный вариант или
    воспользоваться командой /help
    Функция принимает значения update(обновление, пришедшее с сервера) и context(объект, хранящий данные бота)
    """
    user_name = update.effective_user.first_name
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo='https://sun9-38.userapi.com/impg/-krE1PvuFBhYGOydVcVm4jGBcf_owY17SzWljw/aVTJnS6cGE4.'
                                 'jpg?size=1920x1038&quality=96&sign=73fc4f99180a381495d0c55a43945bf3&type=album'
                           )
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'Привет, {user_name}! Это бот группы no more people. Для того чтобы узнать, '
                                  f'что я умею, нажми /info или сразу выбери то, что тебе нужно. ',
                             reply_markup=generate_keyboard()
                             )


def unknown(update, context):
    """
    Функция обраюотки нераспознанных команд
    Функция принимает значения update(обновление, пришедшее с сервера) и context(объект, хранящий данные бота)
    """
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я даже не знаю, что и ответить... Может /info?")


def info(update, context):
    """
    Функция, отправляющая пользователю информацию о работе бота
    Функция принимает значения update(обновление, пришедшее с сервера) и context(объект, хранящий данные бота)
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Я отправляю самые ожидаемые анонсы из мира кино, сериалов и аниме - выбери, что тебя интересует.'
             ' А ещё можешь подписаться на паблик, нажав кнопку nmp 🥺👉👈'
    )


CALLBACK_MOVIE = 'movie'
CALLBACK_ANIME = 'anime'
CALLBACK_SERIES = 'series'
CALLBACK_NMP = 'nmp'


def generate_keyboard():
    """
    Функция, генерирующая 3 кнопки:
    1 - кнопка 'Фильм' с возвратным значением CALLBACK_MOVIE
    2 - кнопка 'Аниме' с возвратным значением CALLBACK_ANIME
    3 - кнопка 'Сериал' с возвратным значением CALLBACK_SERIES
    4 - кнопка 'Nmp' с возвратным значением CALLBACK_NMP
    """
    keyboard = [
        [InlineKeyboardButton('Фильм', callback_data=CALLBACK_MOVIE),
         InlineKeyboardButton('Аниме', callback_data=CALLBACK_ANIME),
         InlineKeyboardButton('Сериал', callback_data=CALLBACK_SERIES),
         InlineKeyboardButton('Nmp', callback_data=CALLBACK_NMP)]
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_regulate(update, context):
    """
    Фунцкия, обрабатывающая нажатие на каждую кнопку и выводящая выбранный пользователем список.
    Функция принимает значения update(обновление, пришедшее с сервера) и context(объект, хранящий данные бота)
    """
    query = update.callback_query
    current_callback = query.data

    chat_id1 = update.effective_message.chat_id
    query.edit_message_text(
        text=update.effective_message.text
    )

    if current_callback == CALLBACK_MOVIE:
        context.bot.send_message(
            chat_id=chat_id1,
            text='The Batman (2022) - Мэтт Ривз')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://upload.wikimedia.org/wikipedia/ru/thumb/b/b2/'
                                     'The_Batman_Poster.jpg/1200px-The_Batman_Poster.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Thor: Love and Thunder (2022) - Тайка Вайтити')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://upload.wikimedia.org/wikipedia/ru/b/b1/Thor_Love_and_Thunder_logo.png')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Operation Fortune: Ruse de guerre (2022) - Гай Ричи')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://itc.ua/wp-content/uploads/2021/12/operation-fort'
                                     'une-ruse-de-guerre-poster.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Killers of the Flower Moon (2022) - Мартин Скорсезе')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://avatars.mds.yandex.net/get-kinopoisk-image/160064'
                                     '7/992abe49-0aa2-4f3b-97ed-8db0218d20b1/300x450')

    elif current_callback == CALLBACK_ANIME:
        context.bot.send_message(
            chat_id=chat_id1,
            text='Bungou Stray Dogs 4th Season'
        )
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://nyaa.shikimori.one/system/animes/original/50330.jpg?1636365168')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Kaguya-sama wa Kokurasetai: Ultra Romantic'
        )
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://desu.shikimori.one/system/animes/original/43608.jpg?1634815767')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Golden Kamuy 4th Season'
        )
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://desu.shikimori.one/system/animes/original/50528.jpg?1638791107')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Mob Psycho 100 III'
        )
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://moe.shikimori.one/system/animes/original/50172.jpg?1634707220')
    elif current_callback == CALLBACK_SERIES:
        context.bot.send_message(
            chat_id=chat_id1,
            text='Invincible S2')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://media.kg-portal.ru/tv/i/invincible/posters/invincible_2.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Better Call Saul S6 (2022)')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://www.film.ru/sites/default/files/movies/posters/4149193-852283.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='The Mandalorian S3')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://cdn.igromania.ru/mnt/news/1/c/b/a/b/a/98772/html/more/'
                                     'df27ea84b86194e36b88b41a_560xH.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='The Boys S3')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://www.film.ru/sites/default/files/movies/posters/45185835-1217608.jpg')
        context.bot.send_message(
            chat_id=chat_id1,
            text='Loki S2')
        context.bot.send_photo(chat_id=chat_id1,
                               photo='https://avatars.mds.yandex.net/get-kinopoisk-image/4486454/a893efe1-c720-'
                                     '450e-9c00-c8d5fcef63c3/600x900')
    elif current_callback == CALLBACK_NMP:
        context.bot.send_message(
            chat_id=chat_id1,
            text='https://vk.com/rednmp'
        )


keyboard_handler = CallbackQueryHandler(callback=keyboard_regulate, pass_chat_data=True)
unknown_handler = MessageHandler(Filters.command, unknown)
start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(keyboard_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
