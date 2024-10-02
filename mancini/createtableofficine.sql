create table Nazione(
    nome varchar(100) not null,
    primary key(nome)
);

create table Regione(
    nome varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome,nazione),
    foreign key (nazione) references Nazione(nome)
);

create table Citta(
    nome varchar(100) not null:
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(nome,regione,nazione),
    foreign key (regione,nazione) references Regione(nome,nazione)
);

create table Officina(
    nome varchar(100) not null,
    indirizzo Indirizzo not null,
    id integer not null,
    citta varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(id),
    foreign key (citta,regione,nazione) references Citta(nome,regione,nazione)
);

create table Direttore(
    nascita date not null,
    staff varchar(100)  not null,
    persona varchar(100) not null,
    foreign key(staff,persona) references Staff(staff,persona)
);

create table Dipendente(
    officina integer not null,
    assunzione date not null,
    staff varchar(100)  not null,
    persona varchar(100) not null,
    foreign key(staff,persona) references Staff(staff,persona),
    foreign key (officina) references Officina(id)
);

create table Staff(
    persona varchar(100) not null,
    foreign key(persona) references Persona(cf)
);

create Persona(
    cf CodFis not null,
    nome varchar(100) not null,
    indirizzo Indirizzo not null,
    telefono varchar(100) not null,
    citta varchar(100) not null,
    regione varchar(100) not null,
    nazione varchar(100) not null,
    primary key(cf),
    foreign key (citta,regione,nazione) references Citta(nome,regione,nazione)
);