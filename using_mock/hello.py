class Hello:
    def greet(self, name):
        return f"Hello, {name}!"


if __name__ == "__main__":
    c = Hello()
    print(c.greet("Bob"))
