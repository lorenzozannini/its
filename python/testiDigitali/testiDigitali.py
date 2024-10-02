class Documento:
    def getText(self):
        return self.testo
    
    def setText(self,testo):
        self.testo=testo
    
    def isInText(self,parola):
        a=" "
        parole=a.join(self.testo.split())
        parole=a.join(parole.split(","))
        parole=a.join(parole.split("."))
        parole=a.join(parole.split("?"))
        parole=a.join(parole.split("!"))
        parole=a.join(parole.split(":"))
        parole=a.join(parole.split(";"))
        parole=parole.split()
        if parola in parole:
            return True
        else:
            return False
    
class Email(Documento):
    def __init__(self):
        super().__init__()
        
    def setMittente(self,m):
        self.mittente=m
    
    def getMittente(self):
        return self.mittente
    
    def setDestinatario(self,d):
        self.destinatario=d
    
    def getDestinatario(self):
        return self.destinatario
    
    def setTitolo(self,t):
        self.titolo=t
    
    def getTitolo(self):
        return self.titolo
    
    def getText(self):
        text=f"Da: {self.getMittente()}, A: {self.getDestinatario()}\n"
        text+=f"Titolo: {self.getTitolo()}\n"
        text+=f"Messaggio: {super().getText()}\n"
        return text
    
    def writeToFile(self):
        file=open("testiDigitali/documenti.txt","a")
        file.write(self.getText())
        file.close()
    
class File(Documento):
    def __init__(self,nome_percorso):
        super().__init__()
        self.nome_percorso=nome_percorso
    
    def leggiTestoDaFile(self): 
        file=open(f"{self.nome_percorso}/documenti.txt","r")
        text=file.read()
        file.close()
        return text
    
    def getText(self):
        s=f"Percorso: {self.nome_percorso}/documenti.txt\n"
        s+=f"Contenuto: {self.leggiTestoDaFile()}"
        return s

d=Documento()
d.setText("ciao, .v ,a. fkseo.dio n ,b")
print(d.getText())
print(d.isInText("dio"))
e=Email()
e.setMittente("alice@example.com")
e.setDestinatario("bob@example.com")
e.setTitolo("Incontro")
e.setText("Ciao Bob, possiamo incontrarci domani?")
print(e.getText())
e.writeToFile()
file=File("testiDigitali")
print(file.getText())