# Käyttötapaukset

## Tunnuksen luominen ja kirjautuminen

Kirjautumatta näen etusivun, jossa on listattuna kaikki sovellusta käyttävät käyttäjänimet.

> SELECT Account.username FROM Account
GROUP BY Account.id

Käyttäjänä pystyn luomaan uuden käyttäjätunnuksen sovellukseen, joilla voin kirjautua sisään.

> INSERT INTO account (username, password) VALUES (kayttaja, salasana)

Käyttäjänä voin kirjautua sovellukseen sisään luomallani käyttäjätunnuksella ja salasanalla, jolloin minulle aukeaa kaikki sovelluksen tarjoamat ominaisuudet.

> SELECT account.id AS account_id, account.username AS account_username, account.password AS account_password
FROM account
WHERE account.username = kayttaja AND account.password = salasana

Kirjautuessa käyttäjätunnuksella saan virheilmoituksen, jos käyttäjätunnut tai salasana on virheellinen.

*"Username or password didn't match. Try again!"*


## Ostosten lisääminen ostoslistaan

Käyttäjänä pystyn siirtymään sivulle, jossa pystyn lisäämään ostoksia ostoslistaan. 

Käyttäjänä pystyn lisäämään ostoslistaan tuotteita, jotta muistaisin ostaa ne seuraavan tilaisuuden tullen.

Käyttäjänä pystyn asettamaan ostokselle kategorian, joka määrittelee ostoksen käyttötarkoitusta.

> INSERT INTO item (name, bought, category_id, account_id) VALUES (milk, 0, drinks_id, current_user.id)


## Ostoslista

Käyttäjänä näen ostoslistan, johon olen itse lisännyt tuotteita ostettavaksi.

Käyttäjänä näen listasta tuotteet ja niiden statuksen, jotta tiedän mitä on tullut ostettua ja mitä ei.

> SELECT Item.id, Item.name, Category.cname, Item.bought FROM Item
JOIN Account ON Item.account_id = Account.id
JOIN Category ON Item.category_id = Category.id
WHERE (Item.account_id = :account)
GROUP BY Item.id

## Ostaminen

Käyttäjänä pystyn merkitsemään ostoslistan tuoteita ostetuksi, jotta tiedän mitä kaikkea olen jo ostanut.

> UPDATE item SET bought=1 WHERE item.id = milk_id

Käyttäjänä voin poistaa tuotteita ostoslistasta, jos en enää tarvitsekkaan jotain tuotetta. 

> DELETE FROM item WHERE item.id = milk_id

## Kategorian luominen

Käyttäjänä pystyn luomaan sovelluksessa kategorioita, joiden mukaan ostokset luokitellaan.

Kategorian luominen tapahtuu kategorian luomissivulla, jossa kategorialle annetaan nimi.

> INSERT INTO category (cname, size, account_id) VALUES (snacks, 0, current_user.id) 

Käyttäjä lisää ostokselle kategorian ja näin kasvattaa kategorian kokoa yhdellä.

> UPDATE category SET size=1 WHERE category.id = snacks_id
