class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = threading.Event()
        self.b = threading.Event()
        self.b.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.b.wait()
            printFoo()
            self.b.clear()
            self.f.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.f.wait()
            printBar()
            self.f.clear()
            self.b.set()
