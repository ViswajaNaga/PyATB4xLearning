import pytest
import allure
import requests

@allure.title("TC1 - Create Booking CRUD Positive")
@allure.description("TC1-> Verify that POST request - create booking.")
@pytest.mark.crud
def test_create_booking_positive_TC1():
    # To make request we need
    # URL
    # Method-POST
    # Headers
    # Payload
    # Auth-Not req
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers={"Content-Type" : "application/json"}
    payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
                     },
    "additionalneeds" : "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    # statuscode
    assert response.status_code==200
    response_data=response.json()
    # Response body verification
    bookingid = response_data["bookingid"]

    assert bookingid>0
    assert bookingid is not None
    assert type(bookingid)==int

    firstname = response_data["booking"]["firstname"]
    lastname = response_data["booking"]["lastname"]
    totalprice = response_data["booking"]["totalprice"]
    depositpaid = response_data["booking"]["depositpaid"]
    checkin = response_data["booking"]["bookingdates"]["checkin"]
    checkout = response_data["booking"]["bookingdates"]["checkout"]

    assert firstname =="Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    # Headers
    # json Schema validation
    # Time response

@allure.title("TC2 - Create Booking CRUD Negative")
@allure.description("TC2-> Verify that POST request - create booking with {}.")
@pytest.mark.crud
def test_create_booking_negative_TC2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers={"Content-Type" : "application/json"}
    payload={}
    response=requests.post(url=URL,headers=headers,json=payload)

    print(type(URL))
    print(type(headers))
    print(type(payload))

    assert response.status_code == 500


@allure.title("TC3 - Create Booking CRUD Negative passing invalid data")
@allure.description("TC2-> Verify that POST request - create booking with totalprice as negative/string.")
@pytest.mark.crud
def test_create_booking_negative_TC2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers={"Content-Type" : "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": -1,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response=requests.post(url=URL,headers=headers,json=payload)

    assert response.status_code == 200 # coming as 200 which is a bug that needs to be raised.
















