class Console:
    @staticmethod
    def print(label, string):
        print(f"{label}: \t{string}")

    @staticmethod
    def log(*args):
        print(*args)
