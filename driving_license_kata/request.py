from pydantic.main import BaseModel


# "John", "James", "Smith", "01-Jan-2051", "M"
class DrivingLicenseRequestModel(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    date_of_birth: str
    gender: str
