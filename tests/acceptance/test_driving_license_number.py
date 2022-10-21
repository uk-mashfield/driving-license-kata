from driving_license.driving_license import DrivingLicense
import pytest


def test_should_return_a_valid_driving_license_number():
    data = ["John", "James", "Smith", "01-Jan-2000", "M"]
    driving_license = DrivingLicense(data)
    result = driving_license.get_license_number()
    assert result == "SMITH001010JJ9AA"


def test_should_return_my_valid_driving_license_number():
    data = ["Mark", "John", "Ashfield", "09-Apr-1974", "M"]
    driving_license = DrivingLicense(data)
    result = driving_license.get_license_number()
    assert result == "ASHFI704094MJ9AA"
