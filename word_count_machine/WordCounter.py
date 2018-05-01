from collections import Counter

import requests
import re
from bs4 import BeautifulSoup


class WordCounter(object):

    def __init__(self):
        self.parser = 'html.parser'

    def get_word_count(self, word, url):
        body_text = self.get_body_text_from_url(url)
        return self.count_word_from_text(word, body_text)

    def count_word_from_text(self, word, charts_text):
        counts = self.get_all_words_count(charts_text)
        return counts[word]

    def get_all_words_count(self, charts_text):
        words = re.findall(r'\w+', charts_text.lower())
        return dict(Counter(words))

    def get_all_matches_count(self, match, text):
        return {match: text.count(match)}

    def get_matches_count_dict(self, list_matches, text):
        counts = {}
        for word in list_matches:
            counts.update(self.get_all_matches_count(word, text))
        return counts

    def get_words_count_dict(self, words, text):
        counts = self.get_all_words_count(text)
        expressions = [word for word in words if len(word.split(' ')) > 1]
        words_count = {word: counts[word.lower()] for word in words
                       if word in counts and
                       word not in expressions}
        words_count.update(self.get_matches_count_dict(expressions, text))
        zero_counts = {word: 0 for word in words
                       if word not in list(words_count.keys())}
        words_count.update(zero_counts)
        return words_count

    def get_body_text_from_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, self.parser)
        # TODO delete me
        # body_text = ''.join(soup.body(text=True))
        body_text = ''.join(soup.get_text())
        return body_text

    def get_words_count_url(self, words, url):
        text = self.get_body_text_from_url(url)
        return self.get_words_count_dict(words, text)


if __name__ == '__main__':
    response = requests.get('https://www.chartjs.org/')
    soup = BeautifulSoup(response.content, 'html.parser')
    body_text = ''.join(soup.get_text())
    text_file = open("charts.txt", "w")
    text_file.write(body_text)
    text_file.close()
