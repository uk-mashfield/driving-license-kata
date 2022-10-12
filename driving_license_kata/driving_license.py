from datetime import datetime

DOB_FORMAT = '%d-%b-%Y'

class DrivingLicense:

    def __init__(self, data: list) -> None:
        self.first_name, self.middle_name, self.last_name, self.dob, self.gender = data
        self.date = datetime.strptime(self.dob, DOB_FORMAT)

    def get_license_number(self) -> str:
        return self.get_surname() \
               + self.get_decade() \
               + self.get_month() \
               + self.get_day() \
               + self.get_year_digit() \
               + self.get_initials() \
               + '9AA'

    def get_surname(self) -> str:
        return self.last_name.upper()[:5].ljust(5, '9')

    def get_decade(self) -> str:
        year = str(self.date.year)
        return year[-2]

    def get_month(self) -> str:
        month = self.date.month
        if self.gender == 'F':
            month += 50
        return str(month) if month > 9 else '0' + str(month)

    def get_day(self):
        return self.dob[:2]

    def get_year_digit(self):
        year = str(self.date.year)
        return year[-1]

    def get_initials(self):
        return (
                (self.first_name[0])
                + (self.middle_name[0] if len(self.middle_name) > 0 else '9')
        ).upper()
