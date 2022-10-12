class DrivingLicense:

    def __init__(self, data: list) -> None:
        self._data = data

    def get_license_number(self) -> str:
        pass

    def get_surname(self) -> str:
        return self._data[2].upper()[:5].ljust(5, '9')

    def get_decade(self) -> str:
        return self._data[3][-2]
