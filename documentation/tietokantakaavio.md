# Tietokantakaavio

![alt text](https://github.com/retute/Ostoslista/blob/master/documentation/Ostoslista.ui.png "Tietokantakaavio")

[Tietokantataulut](https://github.com/retute/Ostoslista/blob/master/documentation/tietokantataulut.md)


## Suhteet

- Käyttäjä - Kategoria: yhden suhde moneen
- Käyttäjä - Tuote: yhden suhde moneen
- Kategoria - Tuote: yhden suhde moneen


### Monen suhde moneen taulu puuttuu
Valitettavasti en onnistunut saamaan työhöni monen suhde moneen yhteyksiä ja liitostauluja. Olin kuitenkin ajatellut seuraavia vaihtoehtoja tähän osioon:

#### Kategoria - Käyttäjä
Jokaisella käyttäjällä voisi olla useita kategorioita ja kategorialla voisi olla useita käyttäjiä.
	Tässä hieman ongelmallista olisi toteuttaa se, miten kategorialla voi olla useita käyttäjiä. Käyttäjät voisivat kenties liittyä johonkin kategoriaan.

#### Ryhmälista
Eräs idea oli luoda ryhmälista-luokka, jolla olisi *monen suhde moneen* suhde käyttäjän kanssa. Tässä käyttäjä voisi luoda ryhmän usealle käyttäjälle ja yksittäinen käyttäjä voisi kuulua useaan ryhmään. Jokaisella ryhmällä olisi lista asioita, joita he yhdessä ostavat. Esimerkiksi perheen kesken tehtävät ruoka ostokset.
	Tämän lisäksi olisi kuitenkin pitänyt toteuttaa kullekkin käyttäjälle henkilökohtainen ostoslista tuotelistan lisäksi. Myös tuotelistaa olisi täytynyt muokata niin, että listassa näkyisivät kaikkien lisäämät tuotteet ja tuotteilla ei olisi käyttäjää.