import os
import collections
import re

frequent_words_number = 10

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r',encoding="windows-1251") as my_file:
            return my_file.read().replace('\n', '').lower()


def get_most_frequent_words(text):
    all_found_words = re.findall('\w+',text)
    return collections.Counter(all_found_words).most_common(frequent_words_number)


if __name__ == '__main__':
    opened_file = load_data(input("Enter path to file: "))
    ten_most_frequent_words = get_most_frequent_words(opened_file)
    for word in ten_most_frequent_words:
        print("Word: {0} Frequency: {1}".format(word[0].ljust(5), word[1]))