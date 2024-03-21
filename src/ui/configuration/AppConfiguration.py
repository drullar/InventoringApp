class AppConfiguration:
    """Abstraction used for dependency injection. Whenever more than one class need an instance of the same class,
    they should you this to get it."""

    def __init__(self):
        return