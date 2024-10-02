SELECT Persona.nome.Persona.cognome
FROM Persona,Progetto,AttivitaProgetto
WHERE Progetto.nome = 'Pegasus'
    AND AttivitaProgetto.persona=Persona.id