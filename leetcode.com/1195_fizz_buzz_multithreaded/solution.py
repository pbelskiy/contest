class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.l = threading.Lock()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.l.acquire()
            if self.i > self.n:
                self.l.release()
                break
            if self.i % 3 == 0 and self.i % 5 != 0:
                printFizz()
                self.i += 1
            self.l.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.l.acquire()
            if self.i > self.n:
                self.l.release()
                break
            if self.i % 3 != 0 and self.i % 5 == 0:
                printBuzz()
                self.i += 1
            self.l.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.l.acquire()
            if self.i > self.n:
                self.l.release()
                break
            if self.i % 3 == 0 and self.i % 5 == 0:
                printFizzBuzz()
                self.i += 1
            self.l.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.l.acquire()
            if self.i > self.n:
                self.l.release()
                break
            if self.i % 3 != 0 and self.i % 5 != 0:
                printNumber(self.i)
                self.i += 1
            self.l.release()
