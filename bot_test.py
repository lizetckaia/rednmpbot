import unittest
from bot import generate_keyboard, start, unknown, info


class botTest(unittest.TestCase):
    keyboard = [
        ["Аниме"],
        ["Фильм"],
        ["Сериал"],
        ["Nmp"],
    ]

    def test_keyboard(self):
        self.assertNotEqual(generate_keyboard(), self.keyboard)

    def test_unknown(self):
        self.assertEqual(unknown('/help'), "Я даже не знаю, что и ответить... Может /info?")

    def test_info(self):
        self.assertEqual(info('/info'), 'Я отправляю самые ожидаемые анонсы из мира кино, сериалов и аниме - выбери, '
                                        'что тебя интересует.А ещё можешь подписаться на паблик, нажав кнопку nmp 🥺👉👈')


if __name__ == '__main__':
    unittest.main()
