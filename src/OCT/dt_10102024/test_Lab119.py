# PUT Request
# URL
# Path - Booking id
# token - Auth
# Payload
# Headers

import pytest
import allure
import requests


# Create Token - POST req
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    token = response.json()["token"]
    print(token)
    return token


# Create Booking - POST req

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
    print(data)
    bookingid = data["bookingid"]
    return bookingid


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    print(PUT_URL)
    cookie = "token=" + create_token()
    print(cookie)

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
