import pytest
from testbook import testbook
from pathlib import Path
from ... import ROOT_DIR

# Set up a shared notebook context to speed up tests.
@pytest.fixture(scope='module')
def tb():
    nb_path = Path(ROOT_DIR, 'exercises', 'intro', 'intro_1.ipynb')
    nb_path = str(nb_path.absolute())
    with testbook(nb_path, execute=True) as tb:
        yield tb


# Test using function call.
def test_double_array(tb):
    double_array = tb.ref("double_array")
    assert double_array([1, 2, 3]) == [2, 4, 6]


# Test using code injection.
def test_double_array_inject(tb):
    double_array = tb.ref("double_array")

    tb.inject("""
        data = [1, 2, 3]
    """)
    data = tb.ref("data")

    assert double_array(data) == [2, 4, 6]