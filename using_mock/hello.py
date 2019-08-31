from random import randint

class Hello:
    def greet(self, name):
        return f"Hello, {name}!"

    @staticmethod
    def guess_a_number():
        return randint(0, 10)


if __name__ == "__main__":
    c = Hello()
    print(c.greet("Bob"))
