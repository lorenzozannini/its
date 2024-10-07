#1
SELECT a.codice,a.nome, COUNT(DISTINCT ap.comp)
FROM ArrPart ap,Aeroporto a
WHERE 
    a.codice=ap.partenza or
    a.codice=ap.arrivo
GROUP BY a.codice,a.nome

#2
SELECT count(*)
FROM ArrPart ap,Volo v
WHERE ap.codice=v.codice AND ap.comp=v.comp
    AND ap.partenza='HTR'
    AND v.durataMinuti>=100

#5
SELECT a.codice,MIN(c.annoFondaz) min_anno_fondaz
FROM Aeroporto a,ArrPart ap,Compagnia c
WHERE 
    a.codice=ap.partenza OR
    a.codice=ap.arrivo
    AND ap.comp=c.nome
GROUP BY a.codice


#6
SELECT lap.nazione, COUNT(DISTINCT laa.nazione)
FROM LuogoAeroporto lap,ArrPart ap,LuogoAeroporto laa
WHERE lap.aeroporto=ap.partenza
    AND laa.aeroporto=ap.arrivo
GROUP BY lap.nazione