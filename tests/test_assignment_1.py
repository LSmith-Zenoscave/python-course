from assignments.assignment_1.hello_world import hello_world, hello_to


def test_hello_world(capsys):
    """The function hello_world() should say \"Hello, World!\"."""
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!" + "\n"


def test_hello_to(capsys):
    """The function hello_to() should say \"Hello, <name given>!\"."""
    hello_to("Mr. Rossum")
    captured = capsys.readouterr()
    assert captured.out == "Hello, Mr. Rossum!" + "\n"

    hello_to("John Cleese")
    captured = capsys.readouterr()
    assert captured.out == "Hello, John Cleese!" + "\n"
