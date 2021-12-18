import unittest
from unittest.mock import MagicMock
from bot import info, unknown


async def async_magic():
    pass


MagicMock.__await__ = lambda x: async_magic().__await__()


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_info(self):
        message = MagicMock()
        result = await info(message=message)
        message.answer.assert_called_with('Я отправляю самые ожидаемые анонсы из мира кино, сериалов и аниме - '
                                          'выбери, что тебя интересует. А ещё можешь подписаться на паблик, '
                                          'нажав кнопку nmp 🥺👉👈')

    async def test_unknown(self):
        message = MagicMock()
        result = await info(message=message)
        message.answer.assert_called_with("Я даже не знаю, что и ответить... Может /info?")


if __name__ == '__main__':
    unittest.main()
