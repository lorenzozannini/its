from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name,specialization,parcel):
        super().__init__(first_name, last_name)
        if isinstance(specialization,str):
            self.specialization=specialization
        else:
            self.specialization=None
            print("La specializzazione inserita non è una stringa")
        if isinstance(parcel,float):
            self.parcel=parcel
        else:
            self.parcel=None
            print("La parcella inserita non è un float")
    
    def setSpecialization(self,specialization):
        if isinstance(specialization,str):
            self.specialization=specialization
        else:
            print("La specializzazione inserita non è una stringa")

    def setParcel(self,parcel):
        if isinstance(parcel,float):
            self.parcel=parcel
        else:

            print("La parcella inserita non è un float")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self):
        if self.age>30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastName()} is not valid")
            return False
        
    def doctorGreet(self):
        self.greet()
        print(f" Sono un medico {self.getSpecialization()}")
    

d1=Dottore("Mario","Verdi","pediatra",12)
d2=Dottore("Mario","Rossi","chirurgo",4.65)
d1.setAge(30)
d2.setAge(31)
d1.isAValidDoctor()
d2.isAValidDoctor()
d1.doctorGreet()
d2.doctorGreet()