from persona import Persona
class Paziente(Persona):
    def __init__(self, first_name, last_name,idCode):
        super().__init__(first_name, last_name)
        if isinstance(idCode,str):
            self.idCode=idCode
        else:
            self.idCode=None
            print("Il codice id inserito non è una stringa")
    
    def setidCode(self,idCode):
        if isinstance(idCode,str):
            self.idCode=idCode
        else:
            print("Il codice id inserito non è una stringa")
    
    def getidCode(self):
        return self.idCode
    
    def patientInfo(self):
        self.greet()
        print(f"\nID:{self.getidCode()}")
    
p=Paziente("Mario","Rossi","ABCD")
p.patientInfo()