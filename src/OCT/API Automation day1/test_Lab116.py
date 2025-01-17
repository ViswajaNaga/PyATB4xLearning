import pytest
import allure

@allure.title("Sum Validation")
@allure.description("This test attempts to validate sum.")
@allure.tag("Reg")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Viswaja")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_sum_tc1():
    assert 1+1==2

@allure.title("Subtraction Validation")
@allure.description("This test attempts to validate Subtraction.")
@pytest.mark.smoke
def test_sub_tc2():
    assert 5-2==3

@allure.title("Multiplication Validation")
@allure.description("This test attempts to validate Multiplication.")
@pytest.mark.reg
def test_mul_tc3():
    assert 3*4==10

@allure.title("Division Validation")
@allure.description("This test attempts to validate Division.")
@pytest.mark.skip(reason="Not completed, Skip it")
def test_div_tc4():
    assert 10/2==5
