"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """
    instantiated with a path to a file on the disk that contains words,
        one per line
        
    setting up the environment
    >>> f = open('wordfinder_test_words.txt', 'w')
    >>> f.write("cat\nporcupine\ndog")
    >>> f.close()


    >>> wf = WordFinder("wordfinder_test_words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """

    def __init__(self, path):
        self.path = path
        self.words = get_lines_from_file(path)
        print(f"{self.num_of_words()} words read")

    def get_lines_from_file(path):
        f = open(self.path, 'r')
        words = []
        for line in f:
            line = line.rstrip()
            words.append(line)
        f.close()
        return words

    def num_of_words(self):
        return len(self.words)

    def random(self):
        return choice(self.words)
