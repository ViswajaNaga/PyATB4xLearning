# Create Booking Testcase
# Verify that Booking Id is integer
# status code
# headers
# Requests Module

import pytest
import allure
import requests

@allure.title("Test GET Request- RestFul Booker Project1")
@allure.description("TC1-> Verify that GET Request with ID works.")
@allure.tag("Reg","smoke")
@allure.label("owner", "Viswaja")
@allure.testcase("TC1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200


@allure.title("Test GET Request- RestFul Booker Project1")
@allure.description("TC2-> Verify that GET Request with -ID gives error.")
@pytest.mark.smoke
def test_get_single_request_by_id_negative1():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET Request- RestFul Booker Project1")
@allure.description("TC3-> Verify that GET Request with invalid id gives error.")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET Request- RestFul Booker Project1")
@allure.description("TC3-> Verify that GET Request with invalid URL gives error.")
@pytest.mark.smoke
def test_get_single_request_by_id_negative3():
    url = "https://restful-booker.herokuapp.com/bookingss"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET Request- RestFul Booker Project1")
@allure.description("TC3-> Verify that GET Request with invalid pathparam gives error.")
@pytest.mark.smoke
def test_get_single_request_by_id_negative4():
    url = "https://restful-booker.herokuapp.com/bookings/1"
    response_data = requests.get(url)
    assert response_data.status_code == 404