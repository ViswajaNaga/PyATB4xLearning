import pytest
import requests

@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    return token


# Create Booking - POST req

@pytest.fixture()
def create_booking():
    print("Create Booking Testcase")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Vish",
        "lastname": "Naga",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=url, headers=headers, json=payload)

    print(type(url))
    print(type(headers))
    print(type(payload))

    assert response.status_code == 200

    # get the response body and verify the json bookingid is not null
    data = response.json()
    bookingid = data["bookingid"]
    return bookingid


@pytest.fixture()
def read_mysql_file_database():
    pass

@pytest.fixture()
def launch_browser():
    print("Launching a browser! Chrome")
    return "chrome"


@pytest.fixture()
def close_browser():
    print("close a browser! Chrome")
    return "closed"

@pytest.fixture()
def read_url_testdata_excel():
    pass