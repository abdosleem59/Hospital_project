from patients import Patient

class HospitalManager:
    def __init__(self, specialization_cnt):
        self.specialization_patients = [[] for _ in range(specialization_cnt)]
        self.MAX_QUEUE = 10

    def can_add_more_patients(self,specialization):
        return len(self.specialization_patients[specialization]) < self.MAX_QUEUE


    def add_patient(self, specialization, name, status):
        self.specialization_patients[specialization].append(Patient(name, status))
        self.specialization_patients[specialization].sort(key=lambda x: x.status, reverse=True)


    def get_next_patient(self, specialization):
        if len(self.specialization_patients[specialization])!=0:
            return self.specialization_patients[specialization].pop(0)
        return None
    

    def remove_patient(self, specialization, name):
        spec = self.specialization_patients[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False


    def get_printable_patients_info(self):
        results = []    # send back results to front end to print on its way
        for idx, specialization in enumerate(self.specialization_patients):
            if not specialization:
                continue
            cur_patients = []
            for patient in specialization:
                cur_patients.append(str(patient))
            results.append((idx, cur_patients))
        return results