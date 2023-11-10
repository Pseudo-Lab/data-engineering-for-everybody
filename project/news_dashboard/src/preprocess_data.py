import re

from konlpy.tag import Hannanum


def tokenize(text):
    han = Hannanum()
    processed_word = [re.sub(r'[^\w\s]', '', word) for word in han.nouns(text)]
    filtered_word = [word for word in processed_word if len(word) > 1]
    return filtered_word