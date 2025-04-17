import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 1

        self.lock_zero = threading.Lock()
        self.lock_even = threading.Lock()
        self.lock_odd = threading.Lock()

        self.lock_even.acquire()
        self.lock_odd.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lock_zero.acquire()
            if self.i > self.n:
                self.lock_even.release()
                self.lock_odd.release()
                break

            printNumber(0)
            if self.i % 2 == 0:
                self.lock_even.release()
            else:
                self.lock_odd.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lock_even.acquire()
            if self.i > self.n:
                break
            printNumber(self.i)
            self.i += 1
            self.lock_zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lock_odd.acquire()
            if self.i > self.n:
                break
            printNumber(self.i)
            self.i += 1
            self.lock_zero.release()

