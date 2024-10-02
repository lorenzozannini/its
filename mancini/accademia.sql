#2
SELECT Persona.nome,Persona.cognome,Persona.posizione
FROM Persona,Progetto,AttivitaProgetto
WHERE Progetto.nome = 'Pegasus'
    AND AttivitaProgetto.persona=Persona.id
ORDER BY persona.cognome DESC;

#3
SELECT Persona.nome.Persona.cognome
FROM Persona,Progetto,AttivitaProgetto
WHERE Progetto.nome = 'Pegasus'
    AND AttivitaProgetto.persona=Persona.id
    and count(persona.id)>1
