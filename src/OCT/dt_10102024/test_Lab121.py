# Fixture is concept in Python
# You can use the Fixture in context to the test
# Similar to Pre-condition, Post-condition

# Pre-condition - token, bookingId--Fixture
# test_update_negative1
# test_update_positive1

import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_to_confirm(is_married):
    assert is_married == False
