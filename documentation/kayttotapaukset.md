# K‰yttˆtapaukset

## Tunnuksen luominen ja kirjautuminen

K‰ytt‰j‰n‰ pystyn luomaan uuden k‰ytt‰j‰tunnuksen sovellukseen, joilla voin kirjautua sis‰‰n.

> INSERT INTO account (username, password) VALUES (kayttaja, salasana)

K‰ytt‰j‰n‰ voin kirjautua sovellukseen sis‰‰n luomallani k‰ytt‰j‰tunnuksella ja salasanalla, jolloin minulle aukeaa kaikki sovelluksen tarjoamat ominaisuudet.

> SELECT account.id AS account_id, account.username AS account_username, account.password AS account_password
FROM account
WHERE account.username = kayttaja AND account.password = salasana

Kirjautuessa k‰ytt‰j‰tunnuksella saan virheilmoituksen, jos k‰ytt‰j‰tunnut tai salasana on virheellinen.

*"Username or password didn't match. Try again!"*


## Ostosten lis‰‰minen ostoslistaan

K‰ytt‰j‰n‰ pystyn siirtym‰‰n sivulle, jossa pystyn lis‰‰m‰‰n ostoksia ostoslistaan. 

K‰ytt‰j‰n‰ pystyn lis‰‰m‰‰n ostoslistaan tuotteita, jotta muistaisin ostaa ne seuraavan tilaisuuden tullen.

K‰ytt‰j‰n‰ pystyn asettamaan ostokselle kategorian, joka m‰‰rittelee ostoksen k‰yttˆtarkoitusta.

## Ostoslista

K‰ytt‰j‰n‰ n‰en ostoslistan, johon olen itse lis‰nnyt tuotteita ostettavaksi.

> SELECT Item.id, Item.name, Category.cname, Item.bought FROM Item

> JOIN Account ON Item.account_id = Account.id

> JOIN Category ON Item.category_id = Category.id

> WHERE (Item.account_id = :account)

> GROUP BY Item.id

## Ostaminen

K‰ytt‰j‰n‰ pystyn merkitsem‰‰n ostoslistan tuoteita ostetuksi, jotta tied‰n mit‰ kaikkea olen jo ostanut.

K‰ytt‰j‰n‰ voin poistaa tuotteita ostoslistasta, jos en en‰‰ tarvitsekkaan jotain tuotetta. 

K‰ytt‰j‰n‰ n‰en listasta tuotteet ja niiden statuksen, jotta tied‰n mit‰ on tullut ostettua ja mit‰ ei.

## Kategorian luominen

K‰ytt‰j‰n‰ pystyn luomaan sovelluksessa kategorioita, joiden mukaan ostokset luokitellaan.

Kategorian luominen tapahtuu kategorian luomissivulla, jossa kategorialle annetaan nimi. 

K‰ytt‰j‰ lis‰‰ ostokselle kategorian ja n‰in kasvattaa kategorian kokoa yhdell‰.

