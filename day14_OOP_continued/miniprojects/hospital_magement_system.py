class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def __init__(self, name, fee):
        super().__init__(name)
        self.fee = fee


class Surgeon(Doctor):
    def __init__(self, name):
        super().__init__(name, 5000)


class Patient(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__records = []


class Appointment:
    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient

    def bill(self):
        return self.doctor.fee


doc = Surgeon("Dr. Rao")
pat = Patient("Kavitha")
appt = Appointment(doc, pat)
print("Bill:", appt.bill())
