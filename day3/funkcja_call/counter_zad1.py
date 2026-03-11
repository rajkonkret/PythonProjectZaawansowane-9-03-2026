class CallCounter:

    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'funkcję call wywołano {self.count} razy')
