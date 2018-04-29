from collections import Counter

import requests
import re
from bs4 import BeautifulSoup


class WordCounter(object):
    def get_word_count(self, word, url):
        body_text = self.get_body_text_from_url(url)
        return self.count_word_from_text(word, body_text)

    def get_body_text_from_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        body_text = ''.join(soup.body(text=True))
        return body_text

    def count_word_from_text(self, word, charts_text):
        counts = self.get_all_words_count(charts_text)
        return counts[word]

    def get_all_words_count(self, charts_text):
        words = re.findall(r'\w+', charts_text.lower())
        return dict(Counter(words))

    def get_words_count_dict(self, words, text):
        counts = self.get_all_words_count(text)
        return {word: counts[word] for word in words}


if __name__ == '__main__':
    response = requests.get('http://www.chartjs.org/')
    soup = BeautifulSoup(response.content, 'html.parser')
    body_text = ''.join(soup.body(text=True))
    text_file = open("charts.txt", "w")
    text_file.write(body_text)
    text_file.close()
