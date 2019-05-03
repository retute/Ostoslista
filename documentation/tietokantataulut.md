# Tietokantataulut

Kun sovellus k‰ynnistet‰‰n ensimm‰isen kerran, niin tietokantaan luodaan seuraavat taulut:


## K‰ytt‰j‰ (account)

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
)
```

#### id INTEGER NOT NULL
- k‰ytt‰j‰n id, joka ei voi olla tyhj‰
- primary key
- K‰ytt‰j‰‰ voidaan hakea kaikista k‰ytt‰jist‰ id.n perusteella.

#### username VARCHAR(20) NOT NULL
- K‰ytt‰j‰nimi, jonka maksimipituus 20 merkki‰.
- Ei voi olla tyhj‰.
- K‰ytt‰j‰nimi on uniikki eli toista samannimist‰ k‰ytt‰j‰‰ ei voi luoda.
- K‰ytt‰j‰nime‰ k‰ytet‰‰n kirjautumisen yhteydess‰.

#### password VARCHAR(20) NOT NULL
- K‰ytt‰j‰n salasana, jonka maksimipituus 20 merkki‰.
- Ei voi olla tyhj‰.
- Salasana ei n‰y muille sen teksikent‰ss‰: esim. salasana "koira" n‰kyy kent‰ss‰ "*****".


## Kategoria (category)

```
CREATE TABLE category (
        id INTEGER NOT NULL,
        cname VARCHAR(20) NOT NULL,
        size INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (cname),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```
#### id INTEGER NOT NULL
- Kategorian id, joka ei voi olla tyhj‰.
- Primary key.

#### cname VARCHAR(20) NOT NULL
- Kateogrian nimi, jonka maksimipituus on 20 merkki‰.
- Nimi on uniikki eli sovelluksessa ei 
- Nimi annetaan, kun luodaan uutta kategoriaa.

#### size INTEGER NOT NULL: 
- Kategorian koko, joka on aluksi nolla.
- Kun tuote lis‰t‰‰n kategoriaan, niin koko kasvaa.
- Kun kategoriassa oleva tuote poistetaan, niin koko pienenee.

## Tuote (item)

```
CREATE TABLE item (
        id INTEGER NOT NULL,
        name VARCHAR(20) NOT NULL,
        bought BOOLEAN NOT NULL,
        category_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (bought IN (0, 1)),
        FOREIGN KEY(category_id) REFERENCES category (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```

#### id INTEGER NOT NULL
- Tuotteen id, joka ei voi olla tyhj‰.
- Primary key.

#### name VARCHAR(20) NOT NULL
- Tuotteen nimi, jonka maksimipituus on 20 merkki‰.
- Nimi annetaan, kun tuotetta lis‰t‰‰n listaan.
- Nimen minimipituus on 2 merkki‰.

#### bought BOOLEAN NOT NULL
- Status siit‰, onko tuotetta ostettu.
- Oletusarvoisesti *bought=0* eli tuotetta ei ole ostettu.
- Kun tuote ostetaan, niin *bought=1*.
- Arvoa voi muuttaa sovelluksessa.

#### category_id INTEGER NOT NULL
- Tuotteen kategorian id-tunnus.
- Jokaisella tuotteella oltava kategoria.
- Foreign key.

#### account_id INTEGER NOT NULL
- Tuotteen luoman k‰ytt‰j‰n id-tunnus.
- Jokaisella tuotteella on yksi k‰ytt‰j‰, joka sen on lis‰nnyt listaan.
- Foreign key.
