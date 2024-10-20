import pytest
@pytest.mark.smoke
def test_sum_tc1():
    assert 1+1==2
@pytest.mark.smoke
def test_sub_tc2():
    assert 5-2==3
@pytest.mark.reg
def test_mul_tc3():
    assert 3*4==10
@pytest.mark.skip(reason="Not completed, Skip it")
def test_div_tc4():
    assert 10/2==5
