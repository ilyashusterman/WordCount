from unittest import TestCase

from word_count_machine.WordCounter import WordCounter


class TestWordCounter(TestCase):

    def setUp(self):
        self.word_counter = WordCounter()

    def test_count_one_word(self):
        word = 'chart'
        counts = self.word_counter.get_word_count(word,
                                                  'http://www.chartjs.org/')
        self.assertEqual(counts, 7)