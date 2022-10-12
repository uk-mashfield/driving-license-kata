class DrivingLicense:

    def __init__(self, data: list) -> None:
        self._data = data
        self._months = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }

    def get_license_number(self) -> str:
        return self.get_surname() \
               + self.get_decade() \
               + self.get_month() \
               + self.get_day() \
               + self.get_year_digit() + \
               self.get_initials() \
               + '9AA'

    def get_surname(self) -> str:
        return self._data[2].upper()[:5].ljust(5, '9')

    def get_decade(self) -> str:
        return self._data[3][-2]

    def get_month(self) -> str:
        month = self._months[self._data[3][3:6]]
        if self._data[-1] == 'F':
            month = chr(ord(month[0]) + 5) + month[1]
        return month

    def get_day(self):
        return self._data[3][:2]

    def get_year_digit(self):
        return self._data[3][-1]

    def get_initials(self):
        return (
                (self._data[0][0])
                + (self._data[1][0] if len(self._data[1]) > 0 else '9')
        ).upper()
