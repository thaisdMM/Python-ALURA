class Counter:
    """
    Class that represents a counter.
    The instance maintains a specific counter, while a global counter is shared
    by all instances
    """

    global_counter = 0

    def __init__(self):
        self.valor = 0

    def __str__(self):
        return f"Counter: {self.valor}"

    def increment(self):
        self.valor += 1

    @classmethod
    def reset_counter(cls):
        cls.global_counter = 0
        return "Global counter has been reset!"
