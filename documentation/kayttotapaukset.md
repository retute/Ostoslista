# K�ytt�tapaukset

## Tunnuksen luominen ja kirjautuminen

Kirjautumatta n�en etusivun, jossa on listattuna kaikki sovellusta k�ytt�v�t k�ytt�j�nimet.

> SELECT Account.username FROM Account
GROUP BY Account.id

K�ytt�j�n� pystyn luomaan uuden k�ytt�j�tunnuksen sovellukseen, joilla voin kirjautua sis��n.

> INSERT INTO account (username, password) VALUES (kayttaja, salasana)

K�ytt�j�n� voin kirjautua sovellukseen sis��n luomallani k�ytt�j�tunnuksella ja salasanalla, jolloin minulle aukeaa kaikki sovelluksen tarjoamat ominaisuudet.

> SELECT account.id AS account_id, account.username AS account_username, account.password AS account_password
FROM account
WHERE account.username = kayttaja AND account.password = salasana

Kirjautuessa k�ytt�j�tunnuksella saan virheilmoituksen, jos k�ytt�j�tunnut tai salasana on virheellinen.

*"Username or password didn't match. Try again!"*


## Ostosten lis��minen ostoslistaan

K�ytt�j�n� pystyn siirtym��n sivulle, jossa pystyn lis��m��n ostoksia ostoslistaan. 

K�ytt�j�n� pystyn lis��m��n ostoslistaan tuotteita, jotta muistaisin ostaa ne seuraavan tilaisuuden tullen.

K�ytt�j�n� pystyn asettamaan ostokselle kategorian, joka m��rittelee ostoksen k�ytt�tarkoitusta.

> INSERT INTO item (name, bought, category_id, account_id) VALUES (milk, 0, drinks_id, current_user.id)


## Ostoslista

K�ytt�j�n� n�en ostoslistan, johon olen itse lis�nnyt tuotteita ostettavaksi.

K�ytt�j�n� n�en listasta tuotteet ja niiden statuksen, jotta tied�n mit� on tullut ostettua ja mit� ei.

> SELECT Item.id, Item.name, Category.cname, Item.bought FROM Item
JOIN Account ON Item.account_id = Account.id
JOIN Category ON Item.category_id = Category.id
WHERE (Item.account_id = :account)
GROUP BY Item.id

## Ostaminen

K�ytt�j�n� pystyn merkitsem��n ostoslistan tuoteita ostetuksi, jotta tied�n mit� kaikkea olen jo ostanut.

> UPDATE item SET bought=1 WHERE item.id = milk_id

K�ytt�j�n� voin poistaa tuotteita ostoslistasta, jos en en�� tarvitsekkaan jotain tuotetta. 

> DELETE FROM item WHERE item.id = milk_id

## Kategorian luominen

K�ytt�j�n� pystyn luomaan sovelluksessa kategorioita, joiden mukaan ostokset luokitellaan.

Kategorian luominen tapahtuu kategorian luomissivulla, jossa kategorialle annetaan nimi.

> INSERT INTO category (cname, size, account_id) VALUES (snacks, 0, current_user.id) 

K�ytt�j� lis�� ostokselle kategorian ja n�in kasvattaa kategorian kokoa yhdell�.

> UPDATE category SET size=1 WHERE category.id = snacks_id
