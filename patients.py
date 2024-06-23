class Patient:
    def __init__(self,name,status):
        self.name = name
        self.status = status


    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'


    def __repr__(self):
        return f'Patient({self.name},{self.status})'


