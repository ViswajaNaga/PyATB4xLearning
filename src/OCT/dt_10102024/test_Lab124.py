import pytest
import allure
import requests

def test_update_req_1(create_token,create_booking):
    print("Token ->",create_token)
    print("Booking ID ->",create_booking)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token()

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    payload = {
        "firstname": "Viswaja",
        "lastname": "Naga",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=payload)

    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Viswaja"

