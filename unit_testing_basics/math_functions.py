

def fib(n):
    """
    The ratio of two consecutive Fibonacci numbers tends
    to the golden ratio as n increases.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def next_collatz_element(n):
    """
    The Collatz conjecture is a conjecture in mathematics that concerns
    a sequence defined as follows: start with any positive integer n.
    Then each term is obtained from the previous term as follows:
    if the previous term is even, the next term is one half of the
    previous term. If the previous term is odd, the next term is 3 times
    the previous term plus 1. The conjecture is that no matter what
    value of n, the sequence will always reach 1.
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
