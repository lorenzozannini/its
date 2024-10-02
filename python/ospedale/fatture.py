class Fattura:
    def __init__(self,patient,doctor):
        if doctor.isAValidDoctor()==True:
            self.patient=patient
            self.doctor=doctor
            self.fatture=len(patient)
            self.salary=0
        else:
            self.patient=None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self):
        self.salary=self.doctor.parcel*self.fatture
        return self.salary
    
    def getFatture(self):
        self.fatture=len(self.patient)
        return self.fatture
    
    def addPatient(self,newPatient):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {newPatient.idCode}")
    
    def removePatient(self,idCode):
        for p in self.patient:
            if p.idCode==idCode:
                self.patient.remove(p)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {idCode}")
    

    
