
################################################################################
# example fibonacci number code;
# you do not have to modify this code in any way
################################################################################


def fibs(n):
    '''
    This function computes first n fibonacci numbers.
    Notice that this function uses O(n) memory.
    '''
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    '''
    This function computes the n-th fibonacci number,
    but it uses O(n) memory to do so,
    which is bad.
    '''
    return fibs(n)[-1]


def fib(n):
    '''
    This function computes the n-th fibonacci number,
    but it consumes only O(1) memory,
    and is optimal.
    '''
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


################################################################################
# fibonacci number code using generators;
# you will need to implement the functions below
################################################################################


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''
    def __init__(self, n = None):
        '''
        Initializes the object with a limit n. If n is not specified it runs infinitely
        '''
        self.n = n
    
    
    def __repr__(self):
        '''
        Returns Fib as a string. Returns Fib of n if limit is specified. Returns Fib() if no limit is specified
        '''
        if self.n is None:
            return "Fib()"
        else:
            return "Fib({})".format(self.n)

    
    def __iter__(self):
        '''
        Returns an iterator object for Fib (below)
        '''
        return FibIter(self.n)



class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''
    def __init__(self, n):
        '''
        Initialize FibIter object with a limit of n
        '''
        self.n = n
        self.a = 0
        self.b = 1

    
    def __next__(self):
        '''
        Generate the next fibonacci number in the sequence
        '''
        if self.n is None or self.n > 0:
            xs = self.b
            self.a, self.b = self.b, self.a + self.b
            if self.n is not None:
                self.n -= 1
            return xs
        else:
            raise StopIteration


def fib_yield(n=None):
    '''
    This function returns a generator that computes the first n fibonacci numbers.
    If n is None, then the generator is infinite.
    '''
    a = 1
    b = 1
    if n is not None:
        for i in range(1, n + 1):
            c = a
            a = b
            b = b + c
            yield c
