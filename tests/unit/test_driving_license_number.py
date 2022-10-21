from driving_license.driving_license import DrivingLicense
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


@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2050", "M"], "01"),
                             (["John", "James", "Smith", "01-Feb-2090", "M"], "02"),
                             (["John", "James", "Smith", "01-Mar-2000", "M"], "03"),
                             (["John", "James", "Smith", "01-Apr-2000", "M"], "04"),
                             (["John", "James", "Smith", "01-May-2000", "M"], "05"),
                             (["John", "James", "Smith", "01-Jun-2000", "M"], "06"),
                             (["John", "James", "Smith", "01-Jul-2000", "M"], "07"),
                             (["John", "James", "Smith", "01-Aug-2000", "M"], "08"),
                             (["John", "James", "Smith", "01-Sep-2000", "M"], "09"),
                             (["John", "James", "Smith", "01-Oct-2000", "M"], "10"),
                             (["John", "James", "Smith", "01-Nov-2000", "M"], "11"),
                             (["John", "James", "Smith", "01-Dec-2000", "M"], "12"),
                             (["John", "James", "Smith", "01-Jan-2050", "F"], "51"),
                             (["John", "James", "Smith", "01-Feb-2090", "F"], "52"),
                             (["John", "James", "Smith", "01-Mar-2000", "F"], "53"),
                             (["John", "James", "Smith", "01-Apr-2000", "F"], "54"),
                             (["John", "James", "Smith", "01-May-2000", "F"], "55"),
                             (["John", "James", "Smith", "01-Jun-2000", "F"], "56"),
                             (["John", "James", "Smith", "01-Jul-2000", "F"], "57"),
                             (["John", "James", "Smith", "01-Aug-2000", "F"], "58"),
                             (["John", "James", "Smith", "01-Sep-2000", "F"], "59"),
                             (["John", "James", "Smith", "01-Oct-2000", "F"], "60"),
                             (["John", "James", "Smith", "01-Nov-2000", "F"], "61"),
                             (["John", "James", "Smith", "01-Dec-2000", "F"], "62"),
                         ])
def test_month_of_birth(data, expected, driving_license_generator: DrivingLicense):
    month = driving_license_generator(data).get_month()
    assert month == expected

@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2050", "M"], "01"),
                             (["John", "James", "Smith", "02-Feb-2090", "M"], "02"),
                             (["John", "James", "Smith", "03-Mar-2000", "M"], "03"),
                             (["John", "James", "Smith", "04-Apr-2000", "M"], "04"),
                             (["John", "James", "Smith", "05-May-2000", "M"], "05"),
                             (["John", "James", "Smith", "06-Jun-2000", "M"], "06"),
                             (["John", "James", "Smith", "07-Jul-2000", "M"], "07"),
                             (["John", "James", "Smith", "08-Aug-2000", "M"], "08"),
                             (["John", "James", "Smith", "09-Sep-2000", "M"], "09"),
                             (["John", "James", "Smith", "10-Oct-2000", "M"], "10"),
                             (["John", "James", "Smith", "11-Nov-2000", "M"], "11"),
                             (["John", "James", "Smith", "12-Dec-2000", "M"], "12"),
                             (["John", "James", "Smith", "13-Jan-2050", "F"], "13"),
                             (["John", "James", "Smith", "14-Feb-2090", "F"], "14"),
                             (["John", "James", "Smith", "15-Mar-2000", "F"], "15"),
                             (["John", "James", "Smith", "16-Apr-2000", "F"], "16"),
                             (["John", "James", "Smith", "17-May-2000", "F"], "17"),
                             (["John", "James", "Smith", "18-Jun-2000", "F"], "18"),
                             (["John", "James", "Smith", "19-Jul-2000", "F"], "19"),
                             (["John", "James", "Smith", "20-Aug-2000", "F"], "20"),
                             (["John", "James", "Smith", "21-Sep-2000", "F"], "21"),
                             (["John", "James", "Smith", "22-Oct-2000", "F"], "22"),
                             (["John", "James", "Smith", "23-Nov-2000", "F"], "23"),
                             (["John", "James", "Smith", "24-Dec-2000", "F"], "24"),
                             (["John", "James", "Smith", "25-Dec-2000", "F"], "25"),
                             (["John", "James", "Smith", "26-Dec-2000", "F"], "26"),
                             (["John", "James", "Smith", "27-Dec-2000", "F"], "27"),
                             (["John", "James", "Smith", "28-Dec-2000", "F"], "28"),
                             (["John", "James", "Smith", "29-Dec-2000", "F"], "29"),
                             (["John", "James", "Smith", "30-Dec-2000", "F"], "30"),
                             (["John", "James", "Smith", "31-Dec-2000", "F"], "31"),
                         ])
def test_day_of_birth(data, expected, driving_license_generator: DrivingLicense):
    day = driving_license_generator(data).get_day()
    assert day == expected

@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2051", "M"], "1"),
                             (["John", "James", "Smith", "01-Feb-2092", "M"], "2"),
                             (["John", "James", "Smith", "01-Mar-2003", "M"], "3"),
                             (["John", "James", "Smith", "01-Apr-2004", "M"], "4"),
                             (["John", "James", "Smith", "01-May-2005", "M"], "5"),
                             (["John", "James", "Smith", "01-Jun-2006", "M"], "6"),
                             (["John", "James", "Smith", "01-Jul-2007", "M"], "7"),
                             (["John", "James", "Smith", "01-Aug-2008", "M"], "8"),
                             (["John", "James", "Smith", "01-Sep-2009", "M"], "9"),
                             (["John", "James", "Smith", "01-Oct-2000", "M"], "0"),
                         ])
def test_year_digit(data, expected, driving_license_generator: DrivingLicense):
    year = driving_license_generator(data).get_year_digit()
    assert year == expected

@pytest.mark.parametrize("data, expected",
                         [
                             (["John", "James", "Smith", "01-Jan-2050", "M"], "JJ"),
                             (["Adam", "Fred", "Smith", "02-Feb-2090", "M"], "AF"),
                             (["Sally", "Jemima", "Smith", "03-Mar-2000", "M"], "SJ"),
                             (["John", "", "Smith", "04-Apr-2000", "M"], "J9"),
                             (["Henry", "", "Smith", "05-May-2000", "M"], "H9"),
                             (["zak", "towley", "Smith", "06-Jun-2000", "M"], "ZT"),
                         ])
def test_initials(data, expected, driving_license_generator: DrivingLicense):
    initials = driving_license_generator(data).get_initials()
    assert initials == expected
