# Tietokantakaavio

## Tietokantakaavio


![alt text](https://github.com/retute/Ostoslista/blob/master/documentation/Ostoslista.ui.png "Tietokantakaavio")


## Tietokantataulut

Kun sovellus k‰ynnistet‰‰n ensimm‰isen kerran, niin tietokantaan luodaan seuraavat taulut:


### K‰ytt‰j‰ (account)

```
CREATE TABLE account (
        id INTEGER NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
)
```

### Kategoria (category)

```
CREATE TABLE category (
        id INTEGER NOT NULL,
        cname VARCHAR(144) NOT NULL,
        size INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (cname),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```

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