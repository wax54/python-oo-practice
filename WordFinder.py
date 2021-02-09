"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """
    instantiated with a path to a file on the disk that contains words,
    one per line
    
    >>> words = ['cat','','#hello','porcupine','dog']
    >>> wf = WordFinder("wordfinder_test_words.txt")
    5 words read

    >>> res = wf.random()
    >>> res in words
    True
    
    >>> res = wf.random()
    >>> res in words
    True
    
    >>> res = wf.random()
    >>> res in words
    True
    
    >>> res = wf.random()
    >>> res in words
    True
    """

    def __init__(self, path):
        self.path = path
        self.words = self.get_words_from_file()
        print(f"{self.num_of_words()} words read")

    def __repr__(self):
        return f"WordFinder ({self.path})"

    def __str__(self):
        return f"A Word Finder Associated with the File {self.path}"

    def get_words_from_file(self):
        """returns a list of words from self.path assuming there is one word per line"""
        f = open(self.path, 'r')
        words = []
        for line in f:
            line = line.strip()
            words.append(line)
        f.close()
        return words

    def num_of_words(self):
        """returns the number of words in the file"""
        return len(self.words)

    def random(self):
        """returns a random word from the file"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """
    instantiated with a path to a file on the disk that contains words,
    one per line
    sometimes comments denoted with '#' as the first character in the line
    and blank lines will be present, these will be ignored

    >>> words = ['cat', 'porcupine', 'dog']
    >>> ignored = ['','#hello']
    >>> swf = SpecialWordFinder("wordfinder_test_words.txt")
    3 words read

    >>> res = swf.random()
    >>> res not in ignored
    True
    >>> res in words
    True

    >>> res = swf.random()
    >>> res not in ignored
    True
    >>> res in words
    True

    >>> res = swf.random()
    >>> res not in ignored
    True
    >>> res in words
    True

    >>> res = swf.random()
    >>> res not in ignored
    True
    >>> res in words
    True
    """

    def __init__(self, path):
        """Initializes the specialWordFinder the same way as a WordFinder
        But now get_words_from_file has new meaning
        """
        super().__init__(path)

    def __repr__(self):
        return f"SpecialWordFinder ({self.path})"

    def __str__(self):
        return f"A Word Finder that skips spaces and # comments Associated with the File {self.path}"

    def get_words_from_file(self):
        """gets all the lines from the file using the supers function 
        then, makes a new list from the result ignoring all blank lines and comments
        """
        lines = super().get_words_from_file()
        words = []
        for line in lines:
            if line != '' and line[0] != '#':
                words.append(line)
        return words
