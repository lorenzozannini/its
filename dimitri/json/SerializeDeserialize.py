import json

def Serialize(dict, file_path):
    string=json.dumps(dict)
    try:
        with open(file_path,"w") as file:
            file.write(string)
            return True
    except:
        return False


def Deserialize(file_path):
    try:
        with open(file_path,"r") as file:
            dict=json.load(file)
            return dict
    except:
        return None


maths=0
q=0
risp=0
path="./json/quiz.json"
des=Deserialize(path)
for i in des.values():
    for type,quizs in i.items():
        for quiz,infos in quizs.items():
            if type=="maths":
                maths+=1
                q+=1
            else:
                q+=1
            risp+=len(infos['options'])

print(f"Nel questionario ci sono {q} domande e ci sono {maths} domande di matematica e il numero medio di risposte disponibili è {risp/q}")