#1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
select p.posizione,avg(p.stipendio) as media,stddev(p.stipendio) as deviazione
from Persona p
group by p.posizione

#2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media della loro categoria?
with Media as(
    select avg(p.stipendio) as media_stipendio
    from Persona p
    where p.posizione='Ricercatore'
)
select p.*
from Media m,Persona p
where p.stipendio>m.media_stipendio
	and p.posizione='Ricercatore'

#3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria?
with MediaDev as(
    select p.posizione,avg(p.stipendio) as media_stipendio, stddev(p.stipendio) as deviazione
    from Persona p
    group by p.posizione
)

#4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività
progettuali? Restituire tutti i loro dati e il numero di ore lavorate.
with OreLavorate as(
    select p.*,sum(ap.oreDurata) as ore_lavorate
    from AttivitaProgetto ap, Persona p
    where p.id=ap.persona
    group by p.id
)
select *
from OreLavorate ol
where ol.ore_lavorate>20

#5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i
progetti? Restituire nome dei progetti e loro durata in giorni.
with Durata as(
    select p.nome,diffdate(p.fine,p.inizio)
    from Progetto p
    group by p.id
)

#7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del numero di assenze medio per malattia dei professori associati? Restituire id, nome e
cognome del professore e il numero di giorni di assenza per malattia.
with Assenze as(
    select p.id,p.nome,p.cognome,count(*) as assenze
    from Persona p,Assenza a
    where p.id=a.persona
        and a.tipo='Malattia'
        and p.posizione='Professore Ordinario'
    group by p.id
),
MediaAssenze(
    select avg(a.assenze) as media_assenze
    from Assenze a
)
select a.id,a.nome,a.cognome,a.assenze
from MediaAssenze ma, Assenze a
where a.assenze>ma.media_assenze







#1. Quali sono i voli di durata maggiore della durata media di tutti i voli della stessa
compagnia? Restituire il codice del volo, la compagnia e la durata.
with MediaDurataCompagnie as(
    select v.comp,avg(v.durataMinuti) as media_comp
    from Volo v
    group by v.comp
)
select v.codice,v.comp,v.durataMinuti
from MediaDurataCompagnie mdc,Volo v
where v.comp=mdc.comp
    and v.durataMinuti>mdc.media_comp

#2. Quali sono le città che hanno piu” di un aeroporto e dove almeno uno di questi ha
un volo operato da “Apitalia”?

with NumeroAeroportiPerCitta as(
    select la.citta,count(*) as numero_aeroporti
    from LuogoAeroporto la
    group by la.citta
)
select DISTINCT nac.citta
from NumeroAeroportiPerCitta nac, ArrPart ap
where ap.comp='Apitalia'
    and nac.numero_aeroporti>1

#9. Quali sono le città raggiungibili con esattamente uno scalo intermedo partendo
dall’aeroporto “JFK”?
with CittaDirette as(
    select ap.arrivo
    from ArrPart ap
    where ap.partenza='JFK'
),
CittaConScalo as(
    select ap.arrivo
    from CittaDirette cd,ArrPart ap
    where ap.partenza=cd.arrivo
)
select DISTINCT la.citta
from CittaConScalo ccs,LuogoAeroporto la
where ccs.arrivo=la.aeroporto