class FooBar:
    def __init__(self, n):
        self.n = n
        self.event_foo = threading.Event()
        self.event_bar = threading.Event()
        self.event_foo.set()
        self.event_bar.clear()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.event_foo.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.event_foo.clear()
            self.event_bar.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.event_bar.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.event_bar.clear()
            self.event_foo.set()