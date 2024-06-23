from Hospital_Manager import HospitalManager

def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)
        
class FrontendManager:
    def __init__(self, specializations_cnt = 20):
        self.specializations_cnt = specializations_cnt
        self.hospital_manger = HospitalManager(self.specializations_cnt)
        self.add_dummy_data() # This function for automatic testing

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        # let's add the order 1 2 3 4...
        messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    #This function for automatic testing
    def add_dummy_data(self):
        for i in range(10):
            self.hospital_manger.add_patient(2, 'Dummy' + str(i), i % 3)
        for i in range(4):
            self.hospital_manger.add_patient(5, 'AnotherDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manger.add_patient(8, 'ThirdDummy' + str(i), 1)
        for i in range(3):
            self.hospital_manger.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i+5), 2)
    

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1

                if self.hospital_manger.can_add_more_patients(specialization):
                    name = input('Enter patient name: ')
                    status = input_valid_int('Enter status (0 normal / 1 urgent / 2 super urgent): ', 0, 2)
                    self.hospital_manger.add_patient(specialization, name, status)
                else:
                    print("Sorry we can't add more patients for this specialization at the moment.")

            elif choice == 2:
                results = self.hospital_manger.get_printable_patients_info()
                if not results:
                    print('No patients at the moment')
                else:
                    for idx, patients_info in results:
                        print(f'Specialization {idx+1}: There are {len(patients_info)} patients.')
                        print("\n".join(patients_info) + '\n')

            elif choice == 3:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1
                patient = self.hospital_manger.get_next_patient(specialization)

                if patient is None:
                    print('No patients at the moment. Have rest, Dr')
                else:
                    print(f'{patient.name}, Please go with the Dr')

            elif choice == 4:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1
                name = input('Enter patient name: ')
                if not self.hospital_manger.remove_patient(specialization, name):
                    print('No patient with such a name in this specialization!')
                else:
                    print("Patient removed")
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()