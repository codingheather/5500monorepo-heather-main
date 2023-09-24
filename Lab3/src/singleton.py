class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_logger()
        else:
            print("`logger already created`")
        return cls._instance

    def init_logger(self):
        print("`Logger created exactly once`")

def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    logger = Logger()
    logger = Logger()


if __name__ == "__main__":
    main()
