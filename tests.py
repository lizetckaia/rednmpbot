import unittest
from unittest.mock import MagicMock
from bot import info, unknown



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
        bot.send_message.assert_called_with(chat_id=123, text = 'Я отправляю самые ожидаемые анонсы из мира кино, '
                                                                'сериалов и аниме - выбери, что тебя интересует. '
                                                                'А ещё можешь подписаться на паблик, '
                                                                'нажав кнопку nmp 🥺👉👈')
    def test_unknown(self):
        bot = MagicMock()
        context = MagicMock(bot=bot)
        effective_chat = MagicMock(id=123)
        update = MagicMock(effective_chat=effective_chat)
        info(update=update, context=context)
        bot.send_message.assert_called_with(chat_id=123, text="Я даже не знаю, что и ответить... Может /info?")




if __name__ == '__main__':
    unittest.main()
