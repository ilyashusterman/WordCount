from unittest import TestCase

import os

from word_count_machine.WordCounter import WordCounter

TEST_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))


class TestWordCounter(TestCase):
    def setUp(self):
        self.charts_text = open(os.path.join(TEST_PATH, 'charts_html.txt'),
                                'r+').read()
        self.word_counter = WordCounter()

    def test_count_word_from_text(self):
        word = 'chart'
        count = self.word_counter.count_word_from_text(word,
                                                       self.charts_text)
        self.assertEqual(count, 8)

    def test_words_count_dict_text(self):
        words = ['developers', 'chart']
        check_result = {
            'developers': 1,
            'chart': 8
        }
        words_count = self.word_counter.get_words_count_dict(words,
                                                             self.charts_text)
        self.assertDictEqual(check_result, words_count)

    def test_count_one_word_from_url(self):
        word = 'chart'
        counts = self.word_counter.get_word_count(word,
                                                  'http://www.chartjs.org/')
        self.assertEqual(counts, 8)

    def test_count_list_words_from_url(self):
        words = ['developers', 'chart']
        check_result = {
            'developers': 1,
            'chart': 8
        }
        words_count = \
            self.word_counter.get_words_count_url(words,
                                                  'http://www.chartjs.org/')
        self.assertDictEqual(check_result, words_count)

    def test_count_match_list_from_text(self):
        words = ['developers', 'chart']
        check_result = {
            'developers': 1,
            'chart': 5
        }
        words_count = \
            self.word_counter.get_matches_count_dict(words, self.charts_text)
        self.assertDictEqual(words_count, check_result)
