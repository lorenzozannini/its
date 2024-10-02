import os
import PyPDF2

def CercaParolaInNomeFile(file,parola):
    file=file.lower()
    parola=parola.lower()
    if file.find(parola) >= 0:
        return True
    return False

def CercaParolaInContenutoFile(path,parola):
    fileName,fileExt = os.path.splitext(path)
    if fileExt.lower() == ".txt":
        return CercaParolaInFileTxt(path,parola)
    if fileExt.lower() == ".pdf":
        return CercaParolaInFilePdf(path,parola)

def CercaParolaInFileTxt(path,parola):
    with open(path,"r") as file:
        line=file.readline()
        while len(line)>0:
            if line.lower().find(parola.lower()) >=0:
                return True
            line=file.readline()
    return False

def CercaParolaInFilePdf(path,parola):
    pdf = PyPDF2.PdfReader(path)
    numsPages =len(pdf.pages)
    for p in range(numsPages):
        page=pdf.pages[p]
        text = page.extract_text()
        if text.lower().find(parola.lower())>=0:
            return True 
    return False



sRoot = input("Inserisci la directory dove cercare: ")
sParola = input("Inserisci la parola da cercare: ")
sOutDir= input("Inserisci la directory dove mettere i file trovati: ")
bRet=False

for root , ListDir, ListFiles in os.walk(sRoot):
    #print(f"Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} files")
    for file in ListFiles:
        print(f"Devo cercare {sParola} in {file}")
        bRet= CercaParolaInNomeFile(file,sParola)
        if bRet==True:
            print(f"Trovata parola in title {file}")
        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet=CercaParolaInContenutoFile(sFilePathCompleto,sParola)
            if bRet==True:
                print(f"Trovata parola in {file}")