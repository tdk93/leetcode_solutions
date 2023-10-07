class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        self.event3 = threading.Event()
        self.event1.set()
        self.event2.clear()
        self.event3.clear()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.event1.wait()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.event1.clear()
        self.event2.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event2.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.event2.clear()
        self.event3.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event3.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.event3.clear()
        self.event1.set()