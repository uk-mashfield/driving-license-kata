from driving_license_kata.driving_license import DrivingLicense
import pytest

def test_should_return_first_5_characters_of_surname():
  data = ["John","James","Smith","01-Jan-2000","M"]
  surname = DrivingLicense(data).get_surname()
  assert surname == "SMITH"
  
def test_should_return_surname_with_less_than_5_chars():
  pass