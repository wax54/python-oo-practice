"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    start: int
        the integer to begin counting from
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0, curr=None):
        """
        sets self.start to start
        sets self.curr to curr unless a curr is specified
        defaults to 0 when none specified
        """
        self.start = start
        self.curr = start if curr is None else curr

    def generate(self):
        """
        returns the next number in the sequence
        """
        curr = self.curr
        self.curr += 1
        return curr

    def reset(self):
        """
        sets curr to the start number
        """
        self.curr = self.start

    def __repr__(self):
        """
        displays the starting int and the next int that will be returned from generate()
        """
        return f"SerialGenerator(start={self.start}, next={self.curr + 1})"
