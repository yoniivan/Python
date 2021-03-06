# Gets as a param a text file woth words and returns the most frequency word as a Tuple(key, value)
from itertools import chain

file = 'words_text_file.txt'


def file_to_generator(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip('\n').split(' ')


def get_frequency(generator):
    word_dict = dict()
    for arr in chain.from_iterable(generator):
        if len(word_dict) == 0:
            word_dict.update({arr: 1})
        else:
            word_dict[arr] = word_dict.get(arr, 0) + 1
    max_item = max(word_dict, key=lambda k: word_dict[k])
    max_quantity = word_dict.get(max_item)
    return max_item, max_quantity


print(get_frequency(file_to_generator(file)))
