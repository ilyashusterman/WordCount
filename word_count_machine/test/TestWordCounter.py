from unittest import TestCase

import os

from word_count_machine.WordCounter import WordCounter

CLIENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           ''))

class TestWordCounter(TestCase):
    def setUp(self):
        self.charts_text = open(os.path.join(CLIENT_PATH, 'charts.txt'), 'r+').read()
        self.word_counter = WordCounter()

    def test_count_word_from_text(self):
        word = 'chart'
        count = self.word_counter.count_word_from_text(word,
                                                       self.charts_text)
        self.assertEqual(count, 7)

    def test_count_one_word(self):
        word = 'chart'
        counts = self.word_counter.get_word_count(word,
                                                  'http://www.chartjs.org/')
        self.assertEqual(counts, 7)

    def test_words_count_dict_text(self):
        words = ['developers', 'chart']
        check_result = {
            'developers': 1,
            'chart': 7
        }
        words_count = self.word_counter.get_words_count_dict(words,
                                                             self.charts_text)
        self.assertDictEqual(check_result, words_count)

