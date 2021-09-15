import pytest  # for @pytest.fixture mixins

from sql.query import Query


@pytest.fixture(scope="module")
def default():
    pass
    # return FIV4E()
