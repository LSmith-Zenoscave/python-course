"""'Hello, World' is commonly the first program you write."""


def hello_world():
    """Prints 'Hello, World!'.

    example:
        $ python ./run_problem.py hello_world
        Hello, World!
    """

    # TODO: Change the phrase to "Hello, World!".
    print("Goodnight, Moon!")


def hello_to(name: str):
    """Prints a greeting to the provided name.

    arguments:
        name: a string representing the name to greet

    example:
        $ ./run_problem.py hello_to "Mr. Rossum"
        Hello, Mr. Rossum!
    """

    # TODO: Change the greeting variable so it greets the person in the name variable.
    greeting = "Hello, " + "Mrs. Lovelace" + "!"
    print(greeting)
