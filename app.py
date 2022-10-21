from driving_license.driving_license import DrivingLicense
from driving_license.request import DrivingLicenseRequestModel

from fastapi import FastAPI

driving_license_app = FastAPI()


@driving_license_app.get("/")
async def root():
    return {"ping": "pong"}


@driving_license_app.post("/license")
def generate_license(driving_license_model: DrivingLicenseRequestModel) -> dict[str, str]:
    return {"license": DrivingLicense(data=list(driving_license_model.dict().values())).get_license_number()}
