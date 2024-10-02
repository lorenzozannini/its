#7
select a.comp
from arrpart a,luogoaeroporto lp, luogoaeroporto la
where a.partenza=lp.aeroporto
    and a.arrivo=la.aeroporto
    and lp.citta='Roma'
    and la.citta='New York';

#8
select distinct ar.codice,ar.nome,l.citta,l.nazione
from arrpart a,luogoaeroporto l,aeroporto ar
where a.partenza=ar.codice
    and l.aeroporto=ar.codice
    and a.comp='MagicFly';

#9
select a.codice,a.comp,lp.aeroporto,la.aeroporto
from arrpart a,luogoaeroporto lp, luogoaeroporto la
where a.partenza=lp.aeroporto
    and a.arrivo=la.aeroporto
    and lp.citta='Roma'
    and la.citta='New York';

#10
