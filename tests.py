import unittest
from unittest.mock import MagicMock
from bot import info, unknown, start, generate_keyboard


async def async_magic():
    pass


MagicMock.__await__ = lambda x: async_magic().__await__()


class MyTestCase(unittest.TestCase):
    def test_info(self):
        bot = MagicMock()
        context = MagicMock(bot=bot)
        effective_chat = MagicMock(id=123)
        update = MagicMock(effective_chat=effective_chat)
        info(update=update, context=context)
        bot.send_message.assert_called_with(chat_id=123, text='Я отправляю самые ожидаемые анонсы из мира кино, '
                                                              'сериалов и аниме - выбери, что тебя интересует. '
                                                              'А ещё можешь подписаться на паблик, '
                                                              'нажав кнопку nmp 🥺👉👈')

    def test_unknown(self):
        bot = MagicMock()
        context = MagicMock(bot=bot)
        effective_chat = MagicMock(id=123)
        update = MagicMock(effective_chat=effective_chat)
        unknown(update=update, context=context)
        bot.send_message.assert_called_with(chat_id=123, text="Я даже не знаю, что и ответить... Может /info?")

    def test_start(self):
        bot = MagicMock()
        context = MagicMock(bot=bot)
        effective_chat = MagicMock(id=123)
        user_name = 'abc'
        effective_user = MagicMock(first_name=user_name)
        update = MagicMock(effective_chat=effective_chat, effective_user=effective_user)
        start(update=update, context=context)
        bot.send_message.assert_called_with(chat_id=123, text=f'Привет, {user_name}! Это бот группы no more people. '
                                                              f'Для того чтобы узнать, что я умею, нажми /info или '
                                                              f'сразу выбери то, что тебе нужно. ',
                                            reply_markup=generate_keyboard())
        bot.send_photo.assert_called_with(chat_id=123, photo='https://sun9-38.userapi.com/impg/-krE1PvuFBhYGOydVcVm4jGBcf'
                                                             '_owY17SzWljw/aVTJnS6cGE4.jpg?size=1920x1038&quality=96&si'
                                                             'gn=73fc4f99180a381495d0c55a43945bf3&type=album')


if __name__ == '__main__':
    unittest.main()
