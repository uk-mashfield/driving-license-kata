from driving_license_kata.driving_license import DrivingLicense
import pytest


@pytest.fixture
def driving_license_generator():
    return DrivingLicense


@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2000", "M"], "SMITH"),
                             (["John", "James", "Smit", "01-Jan-2000", "M"], "SMIT9"),
                             (["John", "James", "SmithtyHughes", "01-Jan-2000", "M"], "SMITH")
                         ])
def test_should_ensure_surname_is_formatted_correctly(data, expected, driving_license_generator: DrivingLicense):
    surname = driving_license_generator(data).get_surname()
    assert surname == expected


@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2050", "M"], "5"),
                             (["John", "James", "Smith", "01-Jan-2090", "M"], "9"),
                             (["John", "James", "Smith", "01-Jan-2000", "M"], "0")
                         ])
def test_extract_the_decade_from_the_year_of_birth(data, expected, driving_license_generator: DrivingLicense):
    decade = driving_license_generator(data).get_decade()
    assert decade == expected
