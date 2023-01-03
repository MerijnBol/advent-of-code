class Progress:
    progress: int

    def __init__(self):
        self.progress = 1

    def ping(self):
        print(self.progress * ".", end="\r")
        self.progress += 1
