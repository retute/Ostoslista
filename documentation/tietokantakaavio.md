# Tietokantakaavio

## Tietokantakaavio


![alt text](https://github.com/retute/Ostoslista/blob/master/documentation/Ostoslista.ui.png "Tietokantakaavio")


## Tietokantataulut

Kun sovellus k‰ynnistet‰‰n ensimm‰isen kerran, niin tietokantaan luodaan seuraavat taulut:


### K‰ytt‰j‰ (account)

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


### Kategoria (category)

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
- Kateogrian nimi, jonka maksimipituus on 20 merkki‰

#### size INTEGER NOT NULL: 


### Tuote (item)

```
CREATE TABLE item (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        bought BOOLEAN NOT NULL,
        category_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (bought IN (0, 1)),
        FOREIGN KEY(category_id) REFERENCES category (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```