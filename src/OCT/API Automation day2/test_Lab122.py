# Multiple Fixtures
# Fixtures are nothing but normal functions but they can be reused.

import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking_id():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

@pytest.fixture()
def read_json_file():
    return "{}"


def test_consume(create_token,create_booking_id,read_excel_file,read_json_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)
    print(read_json_file)