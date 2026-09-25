from calculator import calculate_total, calculate_average, get_result


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_get_result_pass():
    assert get_result([50, 60, 70]) == "PASS"


def test_get_result_fail():
    assert get_result([20, 30, 35]) == "FAIL"
