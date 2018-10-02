#!/usr/bin/env python3

import sys
from unidecode import unidecode


def find_anagrams(words):
    # dic contains the list of words grouped by anagrams list.
    # dic[key] = a anagram list
    # The anagram list consists of a dictionary of similar words (e.g.
    # "s'ouvrit" and "s'ouvrît" are similar).
    # anagrams[word with special characters] = list of similar words
    dic = {}

    def add_word(key, word, word_without_special_char):
        anagrams = dic.get(key)
        if anagrams is None:
            dic[key] = {word_without_special_char: [word]}
        else:
            similar_words = anagrams.get(word_without_special_char)

            if similar_words is None:
                anagrams[word_without_special_char] = [word]
            else:
                similar_words.append(word)

    def word_to_key(word_without_special_char):
        return ''.join(sorted(word_without_special_char.replace("'", '')))

    for word in words:
        word_without_special_char = unidecode(word)
        key = word_to_key(word_without_special_char)
        add_word(key, word, word_without_special_char)

    anagrams = filter(lambda potential_anagrams: len(potential_anagrams) > 1,
                      dic.values())
    return map(lambda anagram: anagram.values(), anagrams)


def print_anagrams(anagrams):
    for words in anagrams:
        print("\t".join(map(lambda similar: ",".join(similar), words)))


def print_usage_if_asked():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print(
            """{} reads from stdin a list of words and prints in stdout a complete list
of anagrams.
Each anagram is separated by a tabulation character. Similar words (e.g. have
the same letters in the same order but one with accents and not the other) are
separated by a colon.

Output example:
trinquâtes	triséquant
tripatouille, tripatouillé	toupillerait
driveras	verdiras""".format(sys.argv[0]))
        exit(1)


if __name__ == '__main__':
    print_usage_if_asked()

    words = map(lambda l: l.rstrip(), sys.stdin)
    anagrams = find_anagrams(words)
    print_anagrams(anagrams)
